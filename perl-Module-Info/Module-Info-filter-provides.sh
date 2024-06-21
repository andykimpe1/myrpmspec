#!/bin/sh

@@PERL_PROV@@ "$@" | sed -e '/^perl(B::Utils)/d'
