from bitslib import *
from audiolib import *
from scipy.io import wavfile

# Read
print("[!] Reading from \"in.bin\"...")
file = open("in.bin", "rb")
fileData = file.read()
file.close()
print("[!] Successfully read from \"in.bin\"")

# Write
fileDataAsBits = toBitsStr(fileData)
print("[!] Original Data: " + fileDataAsBits)
print("[!] Encoding data...")
audioSample = toAudioSample(fileDataAsBits)
print("[!] Encoded Data: " + str(audioSample))
print("[!] Writting to \"out.wav\"...")
wavfile.write("out.wav", sampleRate, audioSample)
print("[!] Successfully written to \"out.wav\"")