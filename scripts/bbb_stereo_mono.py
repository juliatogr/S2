from pydub import AudioSegment

sound = AudioSegment.from_file("../originals/bbb_mono.wav")
sound = sound.set_channels(2)
sound.export("../results/bbb_stereo.wav", format="wav")

sound = AudioSegment.from_file("../results/bbb_stereo.wav")
sound = sound.set_channels(1)
sound.export("../results/bbb_mono.wav", format="wav")
