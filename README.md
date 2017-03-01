# de_scientific_notationize
Turn a Matlab vector workspace variable from scientific notation to regular float.


In case this is useful to anyone else, here is how I use this tool:
This tool is meant for 1 by X vectors (i.e. a list of values) not for matrices.

Open your Matlab workspace after running your Matlab script and double click on your vector, then select all the values in the vector (hold shift and press End, for example, or shift and the arrow keys) and then copy the values. Paste them into the Matlab console, this will format them between square brackets and separate the values with commas. Then, reselect the values in the input of the console (without pressing enter) and copy them into a text file. Remove the square brackets at the beginning and end and name the text file input.txt. Then, place the input file in the same directory as this script and run the script. An output.txt file will be created which will have your values with zeroes in the appropriate places and no scientific notation anywhere, and the values will be between two curly brackets and separated by commas (so you can copy the entire thing and paste it right into an array initialization, such as for filter coefficients, the reason I wrote this in the first place.)
