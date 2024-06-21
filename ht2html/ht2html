#!/bin/sh
# ht2mtl wrapper script, shamefuly copied from rpmlint
# Guillaume Rousse <g.rousse@linux-mandrake.com>

PYTHONPATH=${PYTHONPATH=.}

PYTHONPATH=${PYTHONPATH}:/usr/share/ht2html

exec python -u -O /usr/share/ht2html/ht2html.py $*
