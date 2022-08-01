# Compare
from subprocess import run
from os import path

def main(videos):
    if len(videos) > 2:
        print('Input 2 videos only.')
        return

    vid1, vid2 = videos
    out= f'{path.split(vid1)[1]} - {path.split(vid2)[1]} - Compared.mkv'
    fc = '"[0:v]scale=1920:1080[bef];[1:v]scale=1920:1080[aft];[bef][aft]"hstack=shortest=1"[v]"'
    cmd = 'ffmpeg -loglevel error -stats -i "{vid1}" -i "{vid2}"'\
         ' -filter_complex {fc} -map "[v]"'\
         ' -vsync 2 -c:v libx264 -preset medium -crf 23 -movflags +faststart "{out}"'

    run(cmd.format(vid1=vid1, vid2=vid2, fc=fc, out=out))