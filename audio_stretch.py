# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 19:28:20 2018

@author: Dell
"""

import wave


def main():
    stretch('audio.wav', 0.5)

def stretch( fname,  factor ):
 infile=wave.open( fname, 'rb')
 rate= infile.getframerate()
 channels=infile.getnchannels()
 swidth=infile.getsampwidth()
 nframes= infile.getnframes()
 audio_signal= infile.readframes(nframes)
 outfile = wave.open('stretched.wav', 'wb')
 outfile.setnchannels(channels)
 outfile.setsampwidth(swidth)
 outfile.setframerate(rate/factor)
 outfile.writeframes(audio_signal)
 outfile.close()
 return;

main()
