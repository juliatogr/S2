from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

input_secs = int(eval(input("Please enter the seconds you want to cut: ")))
ffmpeg_extract_subclip("bbb.mp4", 0, input_secs, targetname="bbb_cut.mp4")
