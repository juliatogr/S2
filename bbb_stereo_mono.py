from pydub import AudioSegment

sound = AudioSegment.from_file("bbb_stereo.wav")
sound = sound.set_channels(1)
sound.export("bbb_mono.wav", format="wav")

sound = AudioSegment.from_file("bbb_mono.wav")
sound = sound.set_channels(2)
sound.export("bbb_stereo.wav", format="wav")
