# -*- coding: utf-8 -*-

""" Read data from file """
import os


def read_data(file_name, format='string'):
    data = ""
    folder_with_files = "./../expected/" + format

    dir_path = os.path.abspath(__file__)
    file_path = os.path.join(dir_path, folder_with_files, file_name)

    with open(file_path, 'r') as f:
        data = f.readlines()

    return "".join(data)
