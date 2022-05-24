import numpy

sampleVolume = 1.0
sampleRate = 22050 

def generateOneBitAudio():
    sampleDuration = 0.00009
    sampleFreq = 1000.0

    sample = numpy.sin(2 * numpy.pi * numpy.arange(sampleRate * sampleDuration) * sampleFreq / sampleRate)
    sample *= 32767
    sample = numpy.int16(sample)

    return sample
    
def generateZeroBitAudio():
    sampleDuration = 0.00009
    sampleFreq = 0.0

    sample = numpy.sin(2 * numpy.pi * numpy.arange(sampleRate * sampleDuration) * sampleFreq / sampleRate)
    sample *= 32767
    sample = numpy.int16(sample)

    return sample