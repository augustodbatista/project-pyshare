from pydantic import BaseModel
from fastapi import FastAPI
from .settings import settings
import boto3, uuid

class S3UploadRequest (BaseModel):
    filename: str
    filetype: str

app = FastAPI()

# 3. Define uma rota para a URL raiz ("/").'
# O "@app.get('/')" diz ao FastAPI: "Quando alguém acessar a URL raiz
# com um método GET, execute a função logo abaixo."
@app.get("/")
def read_root():
    # 4. Retorna um dicionário, que o FastAPI converterá para o formato JSON.
    return {"message": "Olá, Mundo! A API PyShare está no ar!"}

@app.post("/shares/generate-upload-url")
async def generate_upload_url(request_data: S3UploadRequest):
    s3_client = boto3.client('s3', aws_access_key_id = settings.aws_access_key_id, aws_secret_access_key = settings.aws_secret_access_key)
    storage_key = str(uuid.uuid4())
    upload_data = s3_client.generate_presigned_post(Bucket='pyshare-file-uploads', Key=storage_key, ExpiresIn=3600)
    return {"upload_data":upload_data, 'storage_key':storage_key}