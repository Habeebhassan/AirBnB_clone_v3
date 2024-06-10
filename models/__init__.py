#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

# Instantiate a unique FileStorage or DBStorage instance based on environment
storage = DBStorage() if os.getenv('HBNB_TYPE_STORAGE') == 'db' else FileStorage()

# Reload the storage
storage.reload()
