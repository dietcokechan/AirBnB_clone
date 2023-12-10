#!/usr/bin/python3
"""init"""
import models.engine.file_storage


storage = models.engine.file_storage.FileStorage()
storage.reload()
