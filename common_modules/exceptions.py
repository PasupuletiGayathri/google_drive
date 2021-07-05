from apiclient import errors
import sys
sys.path.append("/home/gayathri/Documents/Google_Drive_Api/prerequests")
from quickstart import main
from methods import (list_files,delete_file,create_file,copy_file,
                        export_file,get_file,emptytrash,update_file)

class NotDeleted(Exception):
    pass
class NegativeIndexError(Exception):
    pass
class Successful(Exception):
    pass
class ValueNotEqual(Exception):
    pass
class NotDeleted(Exception):
    pass
service=main()
def list_files1():
    if len(list_files()) == 0: 
        raise NegativeIndexError('No files are created','list_files')

def get_files1():
    if len(get_file())<0:
        raise ValueNotEqual("The id is not found or not created")
    elif get_file()==None:
        raise TypeError("No file found with given id")
    else:
        msg="Successfully Created"
        return msg
        
def delete_files1():
    file_id='1se1-Ms0qx_XHC2pa-SbPSWQ3Mmh8IqyjIgeEqKiBehJYosN6lEZDPAEPtKakll1tbAN9kYUd'
    files = methods.list_files()
    lst = [file['id'] for file in files]
    if file_id in lst:
        raise Not
