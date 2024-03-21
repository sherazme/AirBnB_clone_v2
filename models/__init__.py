#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    s = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    s = FileStorage()
s.reload()
