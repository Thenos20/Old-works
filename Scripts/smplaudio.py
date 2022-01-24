import simpleaudio.functionchecks as fc

import simpleaudio as sa

a = int(input('choose song '))
if a == 1:
    wave_obj = sa.WaveObject.from_wave_file(r"C:\Users\askth\OneDrive\Skrivbord\mp3sound\100_BouncyDrums_849.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

