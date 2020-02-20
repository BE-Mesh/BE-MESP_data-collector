from imports import fileStorage
import os
import sys
import datetime


def main():

    #todo: eventuali altri check alla forma di sys.argv[1]

    file = fileStorage.FileStorage()

    #print(os.path.dirname(os.path.abspath(__file__)))
    for line in sys.stdin:
        sys.stdout.write(line) # i print the monitor line on the stdout,in order to make the script transparent
        __process_line__(str(line))



def __process_line__(line):
    #todo: processing dell'entry
    timestamp = int(datetime.datetime.now().timestamp())

    split_line = line.rstrip().split(" ")

    print("SL: ", split_line)

    if len(split_line) > 3:
        if split_line[0][-1] == 'I' and split_line[2] == 'BenchMark:':
            print("****PROCESSO****")


    pass




if __name__ == "__main__":
    main()