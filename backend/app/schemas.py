from pydantic import BaseModel

class S3UploadRequest (BaseModel):
    filename: str
    filetype: str

class FileRegisterRequest(BaseModel):
    storage_key: str
    original_filename: str
    file_size: int
    mime_type: str