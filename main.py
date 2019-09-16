#!/usr/bin/env python
# coding: utf-8

import os
import shutil

class FileSorter:
    def __init__(self, filetype_filters, filename_filters):
        self.cwd = os.getcwd()
        self.file_list = os.listdir()
        self.typefilters = filetype_filters
        self.namefilters = filename_filters
    
    def generate_filetypes_from_cwd(self):
        for entry in os.scandir(self.cwd):
            if entry.is_file():
                yield '.' + str(entry).split(".")[-1][:-2]
        
    def generate_folders(self, filetype):
        if not os.path.exists(filetype):
            folder_path = os.path.join(self.cwd, filetype)
            os.mkdir(filetype)
                
    def mass_move(self, filetype):        
        for entry in os.scandir(self.cwd):
            if entry.name.endswith(filetype) and entry.is_file():
                source = os.path.join(self.cwd, entry.name)
                destination = os.path.join(self.cwd, filetype, entry.name)
                shutil.move(source, destination)

if __name__ == "__main__" :
    filesorter = FileSorter()
    for filetype in filesorter.generate_filetypes():
        filesorter.generate_folders(filetype)
        filesorter.mass_move(filetype)



