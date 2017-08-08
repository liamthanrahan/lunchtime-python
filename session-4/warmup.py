def word_count():
    ## write some content into a file
    f = open("example.txt", "w")
    f.write("To write or not to write\nthat is the question!\n")
    f.close()

    ## open and read some content in a file
    f = open("example.txt", "r")
    lines = f.readlines() # reads all lines in a file into a list of strings
    for line in lines:
        # remove \n from your lines using
        line = line.replace('\n', '')

        ### your code here ###
        words = line.split(' ')
        print(len(words))

    f.close()

word_count()
