import os

textfile = open(os.path.abspath("./textfile.txt"), "w") # open(“filename”, “mode”)

text = "This is the content that will be written to the text file."

textfile.write(text)