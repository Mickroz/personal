#!/bin/sh
# script to remove wd_tv live stuff.
find /volume1/Movies/. -name '.wd_tv' -delete
find /volume1/Movies/. -name 'flixster_lookup_cache*' -delete
find /volume1/Movies/. -name 'backdrop.jpg' -delete
find /volume1/Movies/. -name '.*.backdrop' -delete
find /volume1/Movies/. -name '*.nfo' -delete
find /volume1/Movies/. -name '*.txt' -delete
find /volume1/Movies/. -name 'Thumbs.db' -delete
find /volume1/Series/. -name '.wd_tv' -delete
find /volume1/Series/. -name 'flixster_lookup_cache*' -delete
find /volume1/Series/. -name 'backdrop.jpg' -delete
find /volume1/Series/. -name '.*.backdrop' -delete
find /volume1/Series/. -name '*.nfo' -delete
find /volume1/Series/. -name '*.txt' -delete
find /volume1/Series/. -name 'Thumbs.db' -delete
find /volume1/. -type d -name '@eaDir' -print0 | xargs -0 rm -rf
