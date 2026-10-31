#!/bin/bash
cd /tmp/work
for p in 1 2; do
  /tmp/tools/venv/bin/python build/part$p.py anim 0 99999 2>&1 | grep --line-buffered -E "Saved:|rror" >> render_p$p.log
done
echo ALLDONE >> render_p2.log
