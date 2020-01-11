#!/usr/bin/env python
# coding: utf-8

import os
import shutil

class FileSorter:
    def __init__(self):
        self.cwd = os.getcwd()
        self.file_list = os.listdir()

    def generate_foldernames(self, directory=None):
        foldernames = []
        if directory is None:
            directory = self.cwd
        for entry in os.scandir(directory):
            if entry.is_folder():
                foldernames.append(entry.name)
        
        return foldernames

    def generate_filetypes(self, directory=None):
        filetypes = []
        if directory is None:
            directory = self.cwd
        for entry in os.scandir(directory):
            if entry.is_file():
                filetypes.append('.' + str(entry).split(".")[-1][:-2])
        return filetypes
        
    def generate_folders(self, foldernames, directory=None):
        if directory is None:
            directory = self.cwd
        for foldername in foldernames:
            new_folder_dir = os.path.join(directory, foldername)
            try:    
                os.mkdir(new_folder_dir)
                print("Creating : " + new_folder_dir)
            except FileExistsError:
                print("Folder Already Made : " + new_folder_dir)
                
    def mass_move(self, identifier, destination):        
        for entry in os.scandir(self.cwd):
            if entry.name.find(identifier) > 0 and entry.is_file() and entry.name != __file__[2:]:
                source = os.path.join(self.cwd, entry.name)
                destination = os.path.join(self.cwd, destination)

                if not os.path.isdir(destination):
                    os.mkdir(destination)
                
                shutil.move(source, destination)
                print("Moving : " + source + " To : " + destination )
    
    def recurse_generate_filetypes(self, directory=None):
        if directory==None:
            directory = self.cwd
        

        

        

if __name__ == "__main__" :
    fs = FileSorter()
    '''
    folder_dict = {
        "Compressed":[".iso", ".zip", ".7z", ".jar", ".rar"],
        "Video":[".mkv", ".mp4", ".wav"],
        "Document":[".psd", ".doc", ".py", ".docx", ".epub", ".pdf"],
        "Audio":[".m4b"],
        "Executable":[".exe", ".msi"],
        "Misc":[".torrent", ".apk", ".jpeg", ".lbr", ".part", ".w3x", ".scr", ".aria2", ".log", ".swf"]
    }
    '''

    for classification, identifiers in folder_dict.items():
        for identifier in identifiers:
            fs.mass_move(identifier, classification)
