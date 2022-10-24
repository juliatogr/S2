import subprocess

subprocess.call(
    ['ffplay', 'bbb.mp4', '-vf',
     'split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay'])
