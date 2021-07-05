##############################################################################################
# Purpose of the Script
#############################################################################################

# This script is designed for testing the google drive methods
# like COPY, CREATE, DELETE, EMPTYTRASH, EXPORT, GET, LIST and UPDATE on Googledrive_api

#############################################################################################
# Below points has been considered in the Script
#############################################################################################

# 1.Created a Google_drive api with Object-Oriented Programming.

# 2.Given respective credentials and permissions to it.

# 3.Testing various method of copy, create, delete, emptytrash, export, get, list and update 
#   with different test cases

# 4.A log file created with the current date time along with message specified.

# 5.Created Custom Exception for erroneous conditions

######################################################################################################
import pytest
import sys
import os
sys.path.append("/home/gayathri/Documents/Google_Drive_Api/common_modules")

from methods import (list_files,delete_file,create_folder,copy_file,
                        export_file,get_file,emptytrash,update_file)

from exceptions import NegativeIndexError,NotDeleted
from exceptions import list_files1,get_files1,delete_files1

import logging
logger=logging.getLogger(__name__)

######################################################################################################################

#Test Case to check possible test cases for list method
def test_list_files():
    #Id to check in list
    id = '1yDze98ItMU8ocwUFTSLkhL35sMFobjuV'
    files = list_files()
    #stores the id's in list
    lst = [file['id'] for file in files]
    assert id in lst,'provided id is not present in list of files'
    logging.info("Id present in list")
    assert type(files)==list
    logging.info("Type of files is list type")
    assert len(files)!=0
    logging.info("Length of files is not equal to Zero")

#Test Case to check negative test cases for list method
def test_list_negative_lst():
    logging.info("Negative test case for list out the files.")
    with pytest.raises(Exception) as exp_info:
        res=exceptions.list_files1()
        logging.info(str(exp_info.value))
    print(str(exp_info.value))   
#################################################################################################################

#Test Case to check possible test cases for Get method
def test_get_file():
    #file_id='1be4zAt_9M3rxtK51yeo1Ox-Zw_mvP3Jz0r94a0HVrIUNknyUi0HxTV6A'
    res=get_file()
    assert res!='py'
    assert res!=0
    logging.info("fileId is not equal to zero")
    assert len(res)>0
    logging.info("length of file is greater than zero")

#Test Case to check negative test cases for Get method
def test_negative_get_file():
    with pytest.raises(Exception) as exp_info:
        res=exceptions.get_files1()
        logging.info(str(exp_info.value))
    print(str(exp_info.value)) 
########################################################################################################################

#Test Case to check possible test cases for copy method
def test_copy_file():
    copied_id='1djaVEocz2oEeQ7RQSKJNVMrsN1AB9-fy'
    files = list_files()
    lst = [file['id'] for file in files]
    assert copied_id  in lst
    logging.info("copied file present in list")
    files1=copy_file()
    assert files1=='file copied successfully'

#Test Case to check negative test cases for copy method
def test_copy_negative():
    with pytest.raises(Exception) as exp_info:
        res=exceptions.copy_files1()
    print(str(exp_info.value))
    logging.info(str(exp_info.value))
#########################################################################################################################

#Test Case to check possible test cases for create method
def test_create():
    res = get_file()
    assert dict == type(res), 'return type is not dict'
    logging.info("type of files list is dict")
    assert create_folder('python_google')=='created successfully'
    logging.info("folder created successfully")

#Test Case to check negative test cases for create method
def test_create_negative():
    with pytest.raises(Exception) as exp_info:
        res=exceptions.create_files1()
    print(str(exp_info.value))
    logging.info(str(exp_info.value)) 

#########################################################################################################################

#Test Case to check possible test cases for delete method
def test_delete_file():
    # Deleted ID to check in list
    file_id='1zxB37Oq4ZhpBVttRKvJcRtC37mn29kI-'
    files = list_files()
    lst = [file['id'] for file in files]
    assert file_id not in lst, 'File not Deleted'
    logging.info("file deleted successfully")

def test_negative_delete_negative():
    with pytest.raises(Exception) as exinfo:
        assert exceptions.delete_files1()
        logging.info(str(exinfo.value))
    print(str(exinfo.value))
#################################################################################################################

#Test Case to check possible test cases for emptyTrash method
def test_emptytrash():
    assert emptytrash()==''
    logging.info('Files deleted permanently in trash')

#Test Case to check negative test cases for emptytrash method
def test_emptytrash_negative():
    with pytest.raises(Exception) as exp_info:
        res=exceptions.emptytrash1()
    print(str(exp_info.value))
    logging.info(str(exp_info.value)) 
#################################################################################################################

#Test Case to check possible test cases for update method
def test_update():
    updated_id='1be4zAt_9M3rxtK51yeo1Ox-Zw_mvP3Jz0r94a0HVrIUNknyUi0HxTV6A'
    res = update_file(updated_id)
    assert type(res) == dict
    assert type(res['parents']) == list 
    logging.info('file updated successfully')
#######################################################################################################################

#Test Case to check possible test cases for export method
def test_export():
    assert export_file()=='file exported sucessfully'
    logging.info("doc exported into pdf successfully")

#Test Case to check negative test cases for update method
def test_export_negative():
    with pytest.raises(Exception) as exp_info:
        res=exceptions.update_files1()
    print(str(exp_info.value))
    logging.info(str(exp_info.value)) 
########################################################################################################################   
if __name__=='__main__':
    pytest.main(args=['-s', os.path.abspath(__file__)])

#####################################  Script Details  #############################################
#Script Name             :         testcases_googledrive.py
#Script Version          :         1.0
#Prepared By             :         Gayathri.Pasupuleti@infinite.com
#Create Date             :         25-06-2021
#Last Modification Date  :         28-06-2021
#####################################################################################################