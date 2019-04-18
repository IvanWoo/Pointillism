import subprocess

# video => sequence of images
subprocess.check_output(['ffmpeg', '-i', 'input.mp4', 'inputs/input_%03d.png'])

for i in range(1, 181):
    uuid = str(i).zfill(3)
    subprocess.check_output(['python', 'main.py', f'inputs/input_{uuid}.png', uuid])
