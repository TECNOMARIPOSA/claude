#!/bin/bash
# usage: process.sh <slug> <image.png> <cfg.json>
cd /tmp/claude-0/-home-user-claude/3f280c0c-aac6-5fb1-b584-e0838e3758c8/scratchpad/eb
slug=$1; img=$2; cfg=$3; out=work/$slug; mkdir -p $out
export SEG_W=${SEG_W:-1400} SEG_THICK=3 SEG_MINFONT=20 SEG_S1=${SEG_S1:-2.0} SEG_S2=${SEG_S2:-1.4}
python3 -I -u segment.py $img $out ${SEG_K:-32} 400 9 > $out/seg.log 2>&1 || { echo "FAIL seg $slug"; exit 1; }
python3 -I render_color.py $out >> $out/seg.log 2>&1
python3 -I build_pages.py $out $out/color_page.png $cfg >> $out/seg.log 2>&1
node render.js $PWD/$out >> $out/seg.log 2>&1
tail -1 $out/seg.log; grep regions $out/seg.log | tail -1
echo "DONE $slug"
