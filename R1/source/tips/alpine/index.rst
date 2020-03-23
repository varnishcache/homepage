.. _alpine:

Compiling on Alpine
===================

There are at least two gotchas on Alpine Linux to compile Varnish.

- `jemalloc` isn't present on that platform so you will need to pass
  `--without-jemalloc` to `configure` so the build system uses the default
  libc's `malloc` functions.
- `libexecinfo` has issues making the panics useless, it is recommended to use
  `libunwind` instead, by passing `--with-unwind` to `configure`.
