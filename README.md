# vidutil
 A simple wrapper for your FFmpeg scripts. 🐍
 

# Usage
Syntax:
```
vidutil.py -s <script> -v <videos>
```

Scripts:
```
upscale > Upscales your videos using libx264.
compare > Compares 2 videos.
reencode > Reencodes specified videos.
```

# Making your own scripts.
Begin by using this template.

Template:
```py
from subprocess import run

def main(videos):
 cmd = 'ffmpeg {args}'
 args = ''
 run(cmd)
```

`vidutil` scripts must have a `main()` function in it.     
Additionally you will need invoke `ffmpeg` in your script, the `vidutil` wrapper doesn't invoke `ffmpeg`.
