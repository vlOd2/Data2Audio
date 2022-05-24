from bitslib import *
from audiolib import *
from scipy.io import wavfile

# Read
print("[!] Reading from \"out.wav\"...")
audioRate, audioSample = wavfile.read('out.wav')
print("[!] Successfully read from \"out.wav\"")
print("[!] Audio Rate: " + str(audioRate))
print("[!] Encoded Data: " + str(audioSample))

# Decode
print("[!] Decoding data...")
decoded = fromAudioSample(audioSample)
print("[!] Decoded Data: " + decoded)