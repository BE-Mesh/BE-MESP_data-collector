from imports import fileStorage
import re
import sys
import datetime
import string




def main():

    global file_stor
    file_stor = fileStorage.FileStorage()

    for line in sys.stdin:
        sys.stdout.write(line) # print the monitor line on the stdout,in order to make the script transparent
        __process_line__(str(line))



def __process_line__(line):
    global file_stor
    timestamp = int(datetime.datetime.now().timestamp()*1000000)


    split_line = line.rstrip().split(" ")

    if len(split_line) > 4:
        if split_line[0][-1] == 'I' and split_line[2] == 'BenchMark:':
            # the line corresponds to a benchmark entry
            entry_to_store = str(timestamp)
            #todo: check on split_line[3] which must contain the ID of the ESP32
            for field in split_line[3:]:
                processed_field = ''.join(list(filter(lambda x: x in string.printable, field))) #remove non-printable characters
                processed_field = re.sub('[,]|(\[0m)$', '', processed_field)
                if len(processed_field) > 0:
                    entry_to_store = entry_to_store + ',' + processed_field
            entry_to_store = entry_to_store + '\n'
            file_stor.saveOnFile(entry_to_store)

    pass




if __name__ == "__main__":
    main()