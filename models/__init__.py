#!/usr/bin/python3
"""Package initializer containing
    Unique Filestorage instance for the application
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
