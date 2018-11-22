# Audio-Stretching
Using python wav package
The audio stretching method is done by resampling the audio signal at a different sampling rate calculated by the original signal’s sampling rate divided by the stretch factor. </br>
So, if the stretch is less the one, the audio is fast played, and if the stretch factor is greater than one the audio is slow played.
the input wav file is opened using python wave library. Important information like the frame rate (sampling rate of the audio signal), number of channels,</br>
sample width, and number of samples are read from the input audio file to be used again to construct the stretched audio signal. 
Then, the sample points of the audio signal are read to be resampled again at a different sampling rate.IV.	Then, the output file that stores the stretched audio </br> 
single is opened and the number of channels and the sample width of the original audio signal are written to it. 
The sampling rate of the audio signal is changed to be sampling rate of the original signal divided by stretch factor. 

