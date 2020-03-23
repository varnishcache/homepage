#
# VCL inline-C workaround for 2019-08 rxbuf issue
#
# Copyright 2019 UPLEX - Nils Goroll Systemoptimierung
#
# See: https://varnish-cache.org/security/VSV00003-mitigation.html
#
# USE AT YOUR OWN RISK
#
# Author: Nils Goroll <nils.goroll@uplex.de>
#
# supported versions
# varnish-6.2.0 and newer (git master)
# varnish-6.1.1
# varnish-6.0.3
# --
#
#
# The simple workaround is
#
# sub vcl_deliver {
#     if (req.esi_level == 0 && req.proto != "HTTP/2.0") {
#         set resp.http.Connection = "close";
#     }
# }
#
# before return(deliver)
#
#
# This file contains a more complicated workaround, which applies
# fixups and determines if "Connection: close" can be avoided. If the
# workaround determines that avoiding "Connection: close" would be
# safe, it falls back on it.
#
# Usage:
#
# * start varnishd with
#
#   -p vcc_allow_inline_c=true
#
#   to allow use of inline-c
#
# * put this file in your vcl_path (usually /etc/varnish)
#
# * add at the top of your VCL:
#
#   include "vsv00003-mitigation.vcl"
#
# * replace all
#
#	return (deliver);
#
#   in vcl_deliver { } with
#
#	call return_deliver_mitigate_vsv00003;

C{
#include <unistd.h>	// ssize_t
#include <string.h>	// memset()
struct wsf {
	unsigned		magic;
	char			id[4];
	char			*s;
	char			*f;
	char			*r;
	char			*e;
};
struct httpcf {
	unsigned		magic;
//define HTTP_CONN_MAGIC	 0x3e19edd1

	int			*p;
	int			enums[2];
	void			*ws;
	char			*rxbuf_b;
	char			*rxbuf_e;
	char			*pipeline_b;
	char			*pipeline_e;
	ssize_t		cl;
	void			*priv;
	double			to[2];
};
}C

# the workaround changes request headers received from the client, so
# it should be the absolutely last thing to call from vcl_deliver {}
# in place of return (deliver)
#
# If it can not ensure a safe environment, it falls back to
# Connection: close

sub return_deliver_mitigate_vsv00003 {
    if (req.esi_level > 0 || req.proto == "HTTP/2.0") {
	return (deliver);
    }
    C{
	    struct httpcf	*h;
	    struct wsf	*wsf;
	    uintptr_t	u;
	    char		*p, *e;
	    size_t		sz;

	    wsf = (struct wsf *)ctx->ws;
	    u   = (uintptr_t)wsf->s;
	    u  &= ~((uintptr_t)sizeof(uintptr_t) - 1);

	    h = (struct httpcf *)u;

	    h--;

	    while (h->magic == 0x3e19edd1) {
		    // cleanup client request
		    p = h->rxbuf_b;
		    if (h->pipeline_b != NULL)
			    e = h->pipeline_b;
		    else
			    e = h->rxbuf_e;

		    while (p < e && (p = memchr(p, '\n', e - p)) != NULL)
			    *p++ = '\0';

		    // cleanup pipeline
		    p = h->pipeline_b;
		    while (p != NULL && p < h->pipeline_e &&
			(*p == '\r' || *p == '\n' ||
			 *p == '\t' || *p == ' ')) {
			    *p++ = '\0';
		    }
		    if (p == h->pipeline_e) {
			    h->pipeline_b = NULL;
			    h->pipeline_e = NULL;
		    } else {
			    h->pipeline_b = p;
		    }

		    if (h->pipeline_e != NULL)
			    p = h->pipeline_e;
		    else
			    p = wsf->s;
		    e = wsf->f;
		    // Connection: close for unsafe workspace
		    if (memchr(p, '\n', e - p) != NULL)
			    break;

		    memset(wsf->f, 0, wsf->e - wsf->f);

		    if (h->pipeline_b != NULL) {
			    // move pipeline to top of ws
			    sz = h->pipeline_e - h->pipeline_b;
			    // Connection: close for ENOSPC
			    if (sz + 1 > wsf->e - wsf->f)
				    break;
			    p = h->pipeline_b;
			    e = h->pipeline_e;

			    h->pipeline_b = wsf->e - sz - 1;
			    h->pipeline_e = wsf->e - 1;

			    memcpy(h->pipeline_b, p, sz);
			    memset(p, 0, sz);
		    }
		    VRT_handling(ctx, VCL_RET_DELIVER);
		    return;
	    }
    }C
    set resp.http.Connection = "close";
    return (deliver);
}

## EXAMPLE
# sub vcl_deliver {
#    # use instead of return (deliver);
#    call return_deliver_mitigate_vsv00003;
# }
