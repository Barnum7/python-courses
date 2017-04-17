# Python can interact with extarnal files on your computer
# Does file path needs to be relative to where you are calling the file in terminal. Not relative to the file where the function is called?

my_file = open("test.txt")
print my_file.read()