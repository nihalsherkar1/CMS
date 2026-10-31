# Burari 3D explainer reels: finishing on a laptop

The cloud render was stopped about 150 frames into Part 1. Everything except the frame render is done:

- Word timings (`build/p*_words.json`)
- Hinglish captions and on-screen labels (`build/p*.ass`)
- The final audio mix, voice plus effects (`build/p*_mix.flac`)
- Shot stills (`stills/`)

## 1. Set up
- Install **Blender 4.2+** (the scripts were built on 5.2). Alternatively, `pip install bpy` in a Python version that matches it.
- Install **ffmpeg** with libass.
- Install the **Inter** font, which must include *Inter ExtraBold* and *Inter Display Black*.
- The scripts use `/tmp/work` as their working folder. Either create it and copy everything there, or search and replace `/tmp/work` with your own folder:

```
mkdir -p /tmp/work/build /tmp/work/ov
cp build/*.py /tmp/work/build/
cp build/p1.ass build/p2.ass /tmp/work/ov/
ffmpeg -i build/p1_mix.flac /tmp/work/ov/p1_mix.wav
ffmpeg -i build/p2_mix.flac /tmp/work/ov/p2_mix.wav
cp build/compose.sh build/render_all.sh /tmp/work/
```

`lib.py` loads `/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf`. If your font is somewhere else, change that path.

## 2. Render frames
With bpy installed as a Python module:
```
python /tmp/work/build/part1.py anim 0 99999   # Part 1: 1744 frames
python /tmp/work/build/part2.py anim 0 99999   # Part 2: 1266 frames
```
Or run `render_all.sh`, which renders both. Rendering can be resumed, because frames that already exist are skipped.

With a normal Blender install, run:
```
blender -b --python /tmp/work/build/part1.py -- anim 0 99999
```
In that case, change `sys.argv` in `lib.run()` so it reads the arguments that come after `--`.

**On a laptop with a GPU:** in `lib.setup()` you can set `s.cycles.device = 'GPU'` (and enable CUDA, OptiX or Metal in Preferences). You can also raise `res_pct` to 100 and `samples` to about 32 for sharper frames.

To check single frames: `python part1.py stills` writes `still_01..08.png`.

## 3. Assemble the videos
```
/tmp/work/compose.sh p1
/tmp/work/compose.sh p2
```
`compose.sh` writes `OUT` (set inside the script; change it to your output folder) and makes two files per part:
- `partN_final_1080x1920.mp4`: H.264 CRF 18, AAC 192k, with captions and labels burned in.
- `partN_final_720p_whatsapp.mp4`: two-pass encode, under 20 MB.

## Notes
- Frames render at 15 fps and are doubled to 30 fps when assembled. Cuts and label pops are timed to the 15 fps frame grid.
- Word timing came from matching the script to the pauses in the audio, not from the MMS_FA model, which was blocked in the cloud. Phrase starts are accurate to about 0.05 s; individual words to about 0.1–0.2 s.
- On-screen facts that differ from the voiceover: the engagement is shown as "ENGAGED 17 JUNE 2018" (about 14 days before), and the dog walk as "10:57 PM".
