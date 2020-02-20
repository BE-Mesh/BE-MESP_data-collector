from imports import fileStorage
import os
import sys


def main():

    #todo: eventuali altri check alla forma di sys.argv[1]

    file = fileStorage.FileStorage()

    #print(os.path.dirname(os.path.abspath(__file__)))
    for line in sys.stdin:
        sys.stdout.write(line) # i print the monitor line on the stdout,in order to make the script transparent
        __process_line__(line)



def __process_line__(line):
    #todo: processing dell'entry
    pass


if __name__ == "__main__":
    main()