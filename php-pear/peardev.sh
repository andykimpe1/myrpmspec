#!/bin/sh
exec /usr/bin/php -d memory_limit="-1" -C -q -d include_path=/usr/share/pear \
    -d date.timezone=UTC \
    -d output_buffering=1 /usr/share/pear/pearcmd.php "$@"
