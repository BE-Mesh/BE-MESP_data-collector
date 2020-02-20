from .utilities.singleton import Singleton
from pathlib import Path
import os
import re
from random import randrange
import datetime

import sys


class FileStorage(metaclass=Singleton):

    def __init__(self):

        self.directory_path = ''
        self.file_descriptor = ''

        self.__checkValidityDIRName()

        self.__initializeDIR()

        self.__initializeFile()

        # if res[0] < 0:
        #     # res[0] != 0 means that an error occurred
        #     err_code = '0C'  # C stands for custom
        #     err_mess = 'Undefined'
        #     err_details = 'Generic error'
        #     raise ValueError(err_code, err_mess, err_details)
        #
        # self.db_file_path_str = res[1]
        #
        # #initialize DatabaseManager
        # print("*** PATH: ",self.db_file_path_str)
        # self.dbManager = DatabaseManager(self.db_file_path_str)


    def __checkValidityDIRName(self):

        if len(sys.argv) < 2:
            err_code = '1C'  #C stands for custom
            err_mess = 'NO DIRECTORY PASSED AS ARGUMENT'
            err_details = 'please pass the name of a directory where to store results as argument'
            raise ValueError(err_code,err_mess, err_details)

        dir_name_check = bool(re.match('^[a-zA-Z0-9\-_]+$', str(sys.argv[1])))

        if not dir_name_check:
            err_code = '2C'  # C stands for custom
            err_mess = 'INVALID NAME FOR A DIRECTORY'
            err_details = 'please pass a name containing only letters/numbers/-/_  and no whitespace '
            raise ValueError(err_code, err_mess, err_details)




    def __initializeDIR(self):

        script_root_path_str = str(Path(str(sys.argv[0])).absolute().parent.parent)
        dir_path = Path(script_root_path_str + "/results/1-dc-results/" + str(sys.argv[1])).absolute()
        print("Checking if ./results/1-dc-results/" + str(sys.argv[1]) + " exists...")
        try:
            os.makedirs(dir_path)
        except OSError:
            print("/results/1-dc-results/" + str(sys.argv[1]) + " already exists")

        print("DIR initialized")
        self.directory_path = str(dir_path)


    def __initializeFile(self):
        filename = self.directory_path + "/" + str(int(datetime.datetime.now().timestamp())) + "_" + str(randrange(100)) + str(randrange(100)) + ".txt"
        self.file_descriptor = open(filename, 'a+')

            #
            # if(db_file_path.is_file()):
            #     return 0, str(db_file_path)
            # else:
            #     err_code = '2C'
            #     err_mess = 'NO DB FOUND!'
            #     err_details = 'there is no DB with this path: ' + str(db_file_path) + ' please manually add it in ./results folder'
            #     raise ValueError(err_code,err_mess,err_details)

