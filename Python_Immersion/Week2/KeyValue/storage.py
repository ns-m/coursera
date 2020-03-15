import os
import tempfile

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'a') as f:
    pass