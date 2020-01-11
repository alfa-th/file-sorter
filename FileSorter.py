#!/usr/bin/env python
# coding: utf-8

import os
import shutil

"""
TO DO:

1.  MAKE DICT GENERATOR
    E.G. :
    IF 
    ->  FOLDER 'DOCUMENTS' HAS FILES WITH FORMAT .DOCX, .DOC, .PDF, ETC.
    THEN
    ->  CREATE NEW DICT {DOCUMENTS:[".DOCX",".DOC", ".PDF", .ETC]}
"""


class FileSorter:
    @staticmethod
    def generate_foldernames(directory):
        foldernames = []
        for entry in os.scandir(directory):
            if entry.is_folder():
                foldernames.append(entry.name)

        return foldernames

    @staticmethod
    def generate_filetypes(directory):
        filetypes = []
        for entry in os.scandir(directory):
            if entry.is_file():
                filetypes.append('.' + str(entry).split(".")[-1][:-2])
        return filetypes

    @staticmethod
    def generate_folders(foldernames, directory):
        for foldername in foldernames:
            new_folder_dir = os.path.join(directory, foldername)
            try:
                os.mkdir(new_folder_dir)
                print("Creating : " + new_folder_dir)
            except FileExistsError:
                print("Folder Already Made : " + new_folder_dir)

    @staticmethod
    def mass_move(origin, identifier, destination):
        for entry in os.scandir(origin):
            if entry.name.find(identifier) > 0 and entry.is_file() and entry.name != __file__[2:]:
                file_origin = os.path.join(origin, entry.name)
                actual_destination = os.path.join(origin, destination)

                if not os.path.isdir(actual_destination):
                    os.mkdir(actual_destination)

                shutil.move(file_origin, actual_destination)
                print("Moving : " + file_origin + " To : " + actual_destination)


    def generate_dict(self, directory):
        filetypes = set(self.generate_filetypes(directory))
        parent_dir = os.path.dirname(directory)

        return {parent_dir, filetypes}

    @staticmethod
    def combine_dicts(dictionaries):
        new_dict = {}
        for dictionary in dictionaries:
            for key, value in dictionary.items():
                new_dict.setdefault(key, []).append(value)

        return new_dict


if __name__ == "__main__" :
    fs = FileSorter()
    directory = "filetest"

    folder_dict = {
        "Compressed": [".iso", ".zip", ".7z", ".jar", ".rar"],
        "Video": [".mkv", ".mp4", ".wav"],
        "Document": [".psd", ".doc", ".py", ".docx", ".epub", ".pdf", ".xd"],
        "Audio": [".m4b"],
        "Executable": [".exe", ".msi"],
        "Misc": [".torrent", ".apk", ".jpeg", ".lbr", ".part", ".w3x", ".scr", ".aria2", ".log", ".swf"],
        "Image": [".png"]
    }

    for classification, identifiers in folder_dict.items():
        for identifier in identifiers:
            fs.mass_move(directory, identifier, classification)
