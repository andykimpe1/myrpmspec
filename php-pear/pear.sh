#!/bin/sh
exec /usr/bin/php -C -d include_path=/usr/share/pear \
    -d date.timezone=UTC \
    -d output_buffering=1 /usr/share/pear/pearcmd.php "$@"
