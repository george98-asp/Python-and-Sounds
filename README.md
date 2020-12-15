# Python-and-Sounds

In this repository i am writing functions for basic audio operations using Python. 

I am using MGT/sms-tools from https://github.com/MTG/sms-tools. And there you can find the file sounds so as to test your function.

In the first file i wrote a function that reads an audio file and returns 10 consecutive samples of the file starting from the 50001th sample.

The input to the function is the file name (including the path) and the output should be a numpy array 
containing 10 samples.


In the second file I wrote a function that reads an audio file and returns the minimum and the maximum values of the audio 
samples in that file. 

The input to the function is the wav file name (including the path) and the output should be two floating 
point values returned as a tuple.


In the third file I wrote a function that given a numpy array x, returns every Mth element in x, starting from the 
first element.  

The input arguments to this function are a numpy array x and a positive integer M such that M < number of 
elements in x. The output of this function should be a numpy array.

If you run your code with x = np.arange(10) and M = 2, the function should return the following output: 
array([0, 2, 4, 6, 8]).
