from audiolib import *

def toBitsStr(data):
    finalBitString = ""
    
    for dataEntry in data:
        byte = dataEntry.to_bytes(2, 'big')
        byteAsBit = "{:08b}".format(int(byte.hex(),16))
        finalBitString += byteAsBit

    return finalBitString

def fromBitsStr(bitsStr):
    return int(bitsStr, 2).to_bytes((len(bitsStr) + 7) // 8, byteorder='big')
    
def toAudioSample(bitsStr):
    audioSample = None

    if bitsStr[0] == '1':
        audioSample = generateOneBitAudio()
    else:
        audioSample = generateZeroBitAudio()

    for bitChar in bitsStr:
        if bitChar == '1':
            audioSample = numpy.concatenate([audioSample, generateOneBitAudio()])
        else:
            audioSample = numpy.concatenate([audioSample, generateZeroBitAudio()])
    
    return audioSample
    
def fromAudioSample(audioSample):
    finalBitsStr = ""
    bitsDone = 0
    
    for audioBit in audioSample:
        # Skips every 1 byte (ex: \x00 \x01 -> \x01)
        # Because numpy adds an \x00 to every freq written
        # Due to the formula used
        if not bitsDone % 2:
            bitsDone += 1
            continue

        if audioBit > 0:
            # This audiobit is equal to a one
            finalBitsStr += "1"
        else:
            # This audiobit is equal to a zero
            finalBitsStr += "0"
        
        bitsDone += 1
    
    # I have no fucking clue why it adds a 0 at the beginning
    return finalBitsStr[1:]