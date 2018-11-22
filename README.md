# Audio-Stretching
Using python wav package

The audio stretching method is done by resampling the audio signal at a different sampling rate calculated by the original signal’s sampling rate divided by the stretch factor. </br>

So, if the stretch is less the one, the audio is fast played, and if the stretch factor is greater than one the audio is slow played.
The input wav file is opened using python wave library. Important information like the frame rate (sampling rate of the audio signal), number of channels,sample width, and number of samples are read from the input audio file to be used again to construct the stretched audio signal. </br>

![caa](https://user-images.githubusercontent.com/25064257/48902925-bbd05b00-ee62-11e8-9e4e-16cca3e1dffc.PNG)

Then, the sample points of the audio signal are read to be resampled again at a different sampling rate. </br>

![acc](https://user-images.githubusercontent.com/25064257/48903016-fcc86f80-ee62-11e8-8f32-23fad2fc16b5.PNG)

Then, the output file that stores the stretched audio single is opened and the number of channels and the sample width of the original audio signal are written to it. </br>

![acc](https://user-images.githubusercontent.com/25064257/48903062-26819680-ee63-11e8-9e34-4ce7c796a551.PNG)

The sampling rate of the audio signal is changed to be sampling rate of the original signal divided by stretch factor. </br>

![acc](https://user-images.githubusercontent.com/25064257/48903089-38633980-ee63-11e8-8f7b-16b79a3cdc2f.PNG)


