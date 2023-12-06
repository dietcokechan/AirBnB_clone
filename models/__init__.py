#!/usr/bin/python3
"""init"""
from models.engine.file_storage import FileStorage as FS


storage = FS()
storage.reload()
