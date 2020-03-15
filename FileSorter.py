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

    def __init__(self):
        pass

    @staticmethod
    def fdnames_of_dir(directory):
        fdnames = []
        for entry in os.scandir(directory):
            if not entry.is_file():
                fdnames.append(entry.name)

        return fdnames

    @staticmethod
    def ftypes_of_dir(directory):
        ftypes = []
        for entry in os.scandir(directory):
            if entry.is_file():
                filetype = str(entry.name).split(".")[-1]
                if filetype == entry.name:
                    break

                ftypes.append('.' + filetype)
        return ftypes

    @staticmethod
    def gen_fd(fdnames, directory):
        for fdname in fdnames:
            new_folder_dir = os.path.join(directory, fdname)
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

                try:
                    shutil.move(file_origin, actual_destination)
                except shutil.Error:
                    shutil.move(file_origin, actual_destination + "copy")

                print("Moving : " + file_origin + " To : " + actual_destination)

    def gen_dict_from_dir(self, directory):
        ftypes = set(self.ftypes_of_dir(directory))

        return {directory: ftypes}

    def gen_dict_from_folderlist(self, directory_list):
        for directory in directory_list:
            yield self.gen_dict_from_dir(directory)


if __name__ == "__main__":
    fs = FileSorter()
    directory = "."

    folders = ["Compressed",
               "Video",
               "Document",
               "Audio",
               "Executable",
               "Misc",
               "Image"
               ]

    folder_dict = {}

    for dict in fs.gen_dict_from_folderlist(folders):
        folder_dict.update(dict)

    # folder_dict = {
    #     "Compressed": [".iso", ".zip", ".7z", ".jar", ".rar", ".tar", ".tgz"],
    #     "Video": [".mkv", ".mp4", ".wav"],
    #     "Document": [".psd", ".doc", ".docx", ".epub", ".pdf", ".xd", ".pptx"],
    #     "Audio": [".m4b"],
    #     "Executable": [".exe", ".msi"],
    #     "Misc": [".torrent", ".apk", ".jpeg", ".lbr", ".part", ".w3x", ".scr", ".aria2", ".log", ".swf"],
    #     "Image": [".png", ".jpg"]
    # }

    # print(folder_dict)
    for classification, identifiers in folder_dict.items():
        for identifier in identifiers:
            fs.mass_move(directory, identifier, classification)
