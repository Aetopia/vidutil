# Simple Upscaler
from os import path
from subprocess import run

def main(videos):
    vf = 'zscale=3840:2160:f=point'
    enc_args = '-c:v libx264 -preset medium -crf 23 -c:a copy'
    out = lambda vid: f'{path.splitext(vid)[0]} - Upscaled.mp4'
    cmd = 'ffmpeg -y -i "{vid}" -loglevel warning -vf {vf} {enc_args} "{out}"'

    for vid in videos:
        print('Rendering:', path.split(vid)[1])
        run(cmd.format(video=vid, output=out(vid),
                       vf=vf, enc_args=enc_args))
        print()
