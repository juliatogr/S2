import moviepy.editor as mp
clip = mp.VideoFileClip("bbb.mp4")
clip_resized = clip.resize(newsize=(360, 240))
clip_resized.write_videofile("bbb_resized.mp4")
