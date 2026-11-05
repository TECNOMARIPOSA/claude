#!/bin/bash
# usage: process_fine.sh <slug> <image.png> <cfg.json>   (finer detail for portraits)
cd /tmp/claude-0/-home-user-claude/3f280c0c-aac6-5fb1-b584-e0838e3758c8/scratchpad/eb
slug=$1; img=$2; cfg=$3; out=work/$slug; mkdir -p $out
export SEG_W=1700 SEG_THICK=3 SEG_MINFONT=14 SEG_S1=1.0 SEG_S2=0.7 SEG_SP=5 SEG_SR=10
python3 -I -u segment.py $img $out 34 120 5 > $out/seg.log 2>&1 || { echo "FAIL seg $slug"; exit 1; }
python3 -I render_color.py $out >> $out/seg.log 2>&1
python3 -I build_pages.py $out $out/color_page.png $cfg >> $out/seg.log 2>&1
node render.js $PWD/$out >> $out/seg.log 2>&1
grep regions $out/seg.log | tail -1; echo "DONE $slug"
