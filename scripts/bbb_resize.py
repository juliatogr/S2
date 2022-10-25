import moviepy.editor as mp
clip = mp.VideoFileClip("../originals/bbb.mp4")

sizes = [(720, 720), (480, 480), (360, 240), (160, 120)]
opt = int(input('Choose the new size'
                '\n 1. 720p'
                '\n 2. 480p'
                '\n 3. 360x240'
                '\n 4. 160x120'))

size = sizes[opt-1]
clip_resized = clip.resize(newsize=size)
clip_resized.write_videofile(
    "../results/bbb_resized.mp4")
