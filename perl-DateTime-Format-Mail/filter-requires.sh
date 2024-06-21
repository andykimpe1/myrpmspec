#!/bin/sh
/usr/lib/rpm/perl.req $* |
 sed -e 's/perl(DateTime) >= 0.1705/perl(DateTime) >= 0.18/'
