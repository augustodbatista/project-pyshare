from pydantic import BaseModel
from fastapi import FastAPI, Depends
from .settings import settings
from sqlalchemy.orm import Session
from . import models, schemas, crud, database
import boto3, uuid

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Olá, Mundo! A API PyShare está no ar!"}

@app.post("/shares/generate-upload-url")
async def generate_upload_url(request_data: schemas.S3UploadRequest):
    s3_client = boto3.client('s3', aws_access_key_id = settings.aws_access_key_id, aws_secret_access_key = settings.aws_secret_access_key)
    storage_key = str(uuid.uuid4())
    upload_data = s3_client.generate_presigned_post(Bucket='pyshare-file-uploads', Key=storage_key, ExpiresIn=3600)
    return {"upload_data":upload_data, 'storage_key':storage_key}

@app.post("/shares/register-file")
async def register_file(request_data: schemas.FileRegisterRequest, db: Session = Depends(database.get_db)):
    new_share = crud.create_share(db,request_data)
    print(f"DEBUG: A tentar conectar-se com a URL: {settings.database_url}")
    return new_share
