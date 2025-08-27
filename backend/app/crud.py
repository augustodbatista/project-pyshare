from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime, timedelta

def create_share(db: Session, share: schemas.FileRegisterRequest):
    db_share = models.Share(**share.model_dump())
    db_share.expires_at= datetime.utcnow()+timedelta(days=1)
    db.add(db_share)
    db.commit()
    db.refresh(db_share)
    return db_share