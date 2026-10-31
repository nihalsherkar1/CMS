#!/bin/bash
# usage: compose.sh p1|p2
set -e
p=$1; WORK=${BURARI_WORK:-/tmp/work}; cd $WORK; OUT=${BURARI_OUT:-$(cd "$(dirname "$0")/.." && pwd)}; mkdir -p $OUT
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 ov/${p}_mix.wav)
N=$([ $p = p1 ] && echo part1 || echo part2)
ffmpeg -v error -y -framerate 15 -i $p/frames/%04d.png -i ov/${p}_mix.wav \
  -filter_complex "[0:v]scale=1080:1920:flags=lanczos,fps=30,ass=ov/$p.ass,format=yuv420p[v];[1:a]volume=1.5dB,alimiter=limit=0.89[a]" \
  -map "[v]" -map "[a]" -t $D -c:v libx264 -preset veryfast -crf 18 -c:a aac -b:a 192k -movflags +faststart $OUT/${N}_final_1080x1920.mp4
# WhatsApp copy < 20 MB, two-pass
VB=$(python3 -c "print(int((19*8*1024*1024/$D - 128000)/1000))")
for pass in 1 2; do
  A=$([ $pass = 1 ] && echo "-an -f mp4 /dev/null" || echo "-c:a aac -b:a 128k -movflags +faststart $OUT/${N}_final_720p_whatsapp.mp4")
  ffmpeg -v error -y -i $OUT/${N}_final_1080x1920.mp4 -vf scale=720:1280:flags=lanczos -c:v libx264 -preset medium -b:v ${VB}k -maxrate $((VB*2))k -bufsize $((VB*2))k -pass $pass -passlogfile $WORK/x264_$p -pix_fmt yuv420p $A
done
ls -l $OUT/${N}_final_*
