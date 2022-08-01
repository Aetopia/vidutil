# Reencoding Script s/o Atzur 🐈
# https://raw.githubusercontent.com/atzuur/scripts/main/reenc.bat

from subprocess import run
from os import path

def main(videos):
    cmd = 'ffmpeg -i "{vid}" -loglevel warning -stats'\
         ' -c:v libx264 -c:a aac -preset slower -x264-params aq-mode=3 -crf 18'\
         ' -b:a 256k -pix_fmt yuv420p "{out}"'
    for vid in videos:
        print('Rendering:', path.split(vid)[1])
        out = f'{path.splitext(vid)[0]} - Reencoded.mp4'
        run(cmd.format(vid=vid, out=out))
        print()