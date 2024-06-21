#!/bin/sh
exec /usr/bin/php -C -n -q -d include_path=/usr/share/pear \
    -d date.timezone=UTC \
    -d output_buffering=1 /usr/share/pear/peclcmd.php "$@"
