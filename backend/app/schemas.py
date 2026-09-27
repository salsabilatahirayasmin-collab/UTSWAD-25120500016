# backend/app/schemas.py
from pydantic import BaseModel

class SessionCreate(BaseModel):
    rute: str
    waktu: str
    kapasitas: int
    terisi: int = 0