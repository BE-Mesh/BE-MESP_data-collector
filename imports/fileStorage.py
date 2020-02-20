from .utilities.singleton import Singleton
from pathlib import Path
import os

import sys


class FileStorage(metaclass=Singleton):

    def __init__(self):


        self.storage_dir = ''

        res = self.__checkDIRexistence()

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


    def __checkDIRexistence(self):

        if len(sys.argv) < 2:
            err_code = '1C'  #C stands for custom
            err_mess = 'NO DIRECTORY PASSED AS ARGUMENT'
            err_details = 'please pass the name of a directory where to store results as argument'
            raise ValueError(err_code,err_mess, err_details)
        else:
            script_root_path_str = str(Path(str(sys.argv[0])).absolute().parent.parent)

            #print("AAAAhhh: ",script_root_path_str)
                #todo:sanity check sul parametro sys.argv[1]
            # db_file_path = Path(script_path_parent_str + "/results/" + sys.argv[1] + '.db').absolute()
            #
            # if(db_file_path.is_file()):
            #     return 0, str(db_file_path)
            # else:
            #     err_code = '2C'
            #     err_mess = 'NO DB FOUND!'
            #     err_details = 'there is no DB with this path: ' + str(db_file_path) + ' please manually add it in ./results folder'
            #     raise ValueError(err_code,err_mess,err_details)

