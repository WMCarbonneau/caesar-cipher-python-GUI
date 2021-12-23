You will need to run this in its current folder (if you're running from command line) for the text file function to work properly. (Do not simply open it in python, navigate to its directory)
Otherwise, the batch file included will do the job on windows.
The cypher outputs to the console as a bonus, as well as to the GUI.
The output of the cipher can be saved to the text files that the program creates.
The decrytor has a character limit due to window size limitations, you'll have to split larger text documents into packets of 92 characters or less.
The program can compare decrypted text to a built-in dictionnary for ease of use. (The dictionnary will not find everything (due to missspellings and outdated database), it is a guide to find the correct output)
This program requires the string, collections and tkinter packages