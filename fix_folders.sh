#!/bin/sh
# script to remove wd_tv live stuff.
find /volume1/. -type d -name '@eaDir' -print0 | xargs -0 rm -rf
find /volume1/films/. -name '.wd_tv' -delete
find /volume1/films/. -name 'flixster_lookup_cache*' -delete
find /volume1/films/. -name 'backdrop.jpg' -delete
find /volume1/series/. -name '*.banner.jpg' -delete
find /volume1/series/. -name '*.background.jpg' -delete
find /volume1/films/. -name '.*.backdrop' -delete
find /volume1/films/. -name '*.nfo' -delete
find /volume1/films/. -name '*.txt' -delete
find /volume1/films/. -name 'Thumbs.db' -delete
find /volume1/films/. -name '*.jpg' -delete
find /volume1/films/. -name '*.xml' -delete
find /volume1/films/. -name '*.bif' -delete
find /volume1/films/. -name '*.idx' -delete
find /volume1/films/. -type f -name '*.srt.random*' -exec bash -c 'mv "$1" "${1%.srt.random*}".nl.srt' - '{}' \;
find /volume1/series/. -name '.wd_tv' -delete
find /volume1/series/. -name 'flixster_lookup_cache*' -delete
find /volume1/series/. -name 'backdrop.jpg' -delete
find /volume1/films/. -name '*.banner.jpg' -delete
find /volume1/films/. -name '*.background.jpg' -delete
find /volume1/series/. -name '.*.backdrop' -delete
find /volume1/series/. -name '*.nfo' -delete
find /volume1/series/. -name '*.txt' -delete
find /volume1/series/. -name 'Thumbs.db' -delete
