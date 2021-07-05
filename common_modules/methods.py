#Purpose of the project
##############################################################################################
#This script has been designed to Validate Google Drive API
##############################################################################################

###############################################################################################
#Below points has been considered in the Script.
###############################################################################################
#1. Generate the Api methods for List, Get, Create, Update, Delete, Export, Emptytrsh and copy.
#2. Use Loggers to print all the information on screen while executing and in log files
###############################################################################################

import sys
import os
sys.path.append("/home/gayathri/Documents/Google_Drive_Api/prerequests")
from quickstart import main
from apiclient import errors
from googleapiclient.errors import HttpError
import pprint
import logging

logging.basicConfig(filename='method.log',
                    format='%(asctime)s %(message)s',
                    filemode='w',level=logging.INFO)
logging.info("Execution of code starts from here.")

service = main()
###############################################################################################################
#Method for list out the file    
def list_files():

    logging.info("Writing a method to get the list of files present in google drive.")
    service = main()
    results = service.files().list(pageSize=20, 
                            fields="nextPageToken, files(id, name)").execute()
    return results.get('files', [])
    logging.info("It Gave the first 10 files present in google drive.")    
###############################################################################################################
# Method to get the particular file.
def get_file():
    logging.info("Method to get the perticular file based on the id.")
    try:
        file_id='1EdDsChtAUMz-1gEwzgkhsugd4GhmhRfmWewog6F6QII'
        results = service.files().get(fileId=file_id).execute()
        return results
        logging.info("Successfully get the file based on id. ")
    except errors.HttpError as error:
        return None
##############################################################################################################
# Method for create a folder  in google drive
def create_folder(name):
    try:
        file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder'
        }
        file = service.files().create(body=file_metadata,
                                            fields='id').execute()
        print ('Folder ID: %s' % file.get('id'))
        return "created successfully"
        logging.info("New folder created successfully")
    except errors.HttpError as error:
        return None
################################################################################################################
#Method to create new file in googledrive
def create_file(name):
    try:
        file_metadata = {
        'name': 'name',
        'mimeType': 'py'
        }
        results=service.files().create(body=file_metadata,fields='id').execute()
        print ('File ID: %s' % results.get('id'))
        return 'file created'
        logging.info("file created successfully")
    except errors.HttpError as error:
        return None
###############################################################################################################
# Method for copying a file
def copy_file():
    logging.info("Creating a method to copy the file from one filr to the other file or folder.")
    try:
        file_id =  '1HVcnb-tQFhfH-4oghMZrK4Kzbh0X3KzH'
        file_metadata = {'name':'Gayathri.docs', 'parents':['1L6ZrsBxtPSWxgapy19iS5_tTuhmRB1tg'],
                                'starred':True,'description':'empty file'}
        results = service.files().copy(fileId=file_id,body=file_metadata).execute()
        logging.info("Successfully copied one file to anothor file. ")
        return 'file copied successfully'
    except errors.HttpError as error:
        return None
#####################################################################################################################################################        
# Method for deleting a file
def delete_file():
    logging.info("Creating method to delete the file.")
    try:
        #ID of the file to delete
        file_id='1awMvXXoU5v9K0_gFLmZAiM7lyoWKTaO8'
        results = service.files().delete(fileId=file_id).execute()
        print(results)
        return results
        logging.info("file deleted successfully")
    except errors.HttpError as error:
        return None
###################################################################################################################
# Method for exporting a file
def export_file():
    logging.info("Creating a method to export the file from document to pdf.")
    try:
        results = service.files().export(fileId='1QSKek-tbgMPftpUdSbafrkjONU50wThTLiG_WD0EkPc',
                                        mimeType='application/pdf',fields='id').execute()
        with open('Gayi_Test.pdf','wb') as fe:
            fe.write(results)
            fe.close()
        return 'file exported sucessfully'
        logging.info("Doc file exported into pdf successfully")
    except errors.HttpError as error:
        return None
##################################################################################################################
# Method for emptyTrash
def emptytrash():
    logging.info("Method for deleting the files from trash.")
    try:
        #deleting files permanently in trash
        results=service.files().emptyTrash(enforceSingleParent=True).execute()
        return results
        logging.info("returns an empty response body")
    except errors.HttpError as error:
        return None
###################################################################################################################
# Method for update the file
def update_file():
    logging.info("Method for update a particular file.")
    try:

        file_id = '1P-T99L71MSa2zz7j_NSyKdzdCq9_6XLoSWII1ZpKdLzYCdnVEUhW9_fJookomyGw3rgWnsIq'
        folder_id = '1L6ZrsBxtPSWxgapy19iS5_tTuhmRB1tg'
        results= service.files().get(fileId=file_id,
                                            fields='id').execute()
        # Move the file to the new folder
        file = service.files().update(fileId=file_id,addParents=folder_id,fields='id').execute()
        return file
        logging.info("file updated successfully")
    except errors.HttpError as error:
        return None

if __name__ == '__main__':
    #pprint.pprint(list_files())
    #pprint.pprint(get_file())
    #pprint.pprint(delete_file())
    #create_folder('python_google')
    #create_file('gayi214')
    #copy_file()
    #pprint.pprint(export_file())
    #pprint.pprint(emptytrash())
    pprint.pprint(update_file())

#####################################  Script Details  #############################################
#Script Name             :         methods.py
#Script Version          :         1.0
#Prepared By             :         Gayathri.Pasupuleti@infinite.com
#Create Date             :         23-06-2021
#Last Modification Date  :         25-06-2021
#####################################################################################################