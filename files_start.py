#
# Read and write files using the built-in Python file methods
#

def main():
    # open a file for writing and create it if it doesnt exist
    #f = open("textfile.txt", "w+")
    # Open the file for appending text to the end
    #f = open("textfile.txt", "a+")

    # write some lines of data to the file
    #for i in range(10):
    #    f.write("this is line %d\r\n" % (i+1))

    f = open("textfile.txt","r")
    if f.mode == 'r': # check to make sure that the file was opened
        # use the read() function to read the entire file
        # contents = f.read()
        # print contents

        fl = f.readlines()
        for x in fl:
            print x 

    #close the file when done
    #f.close()

if __name__ == "__main__":
    main()