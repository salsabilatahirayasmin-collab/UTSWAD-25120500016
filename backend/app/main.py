# backend/app/main.py
from fastapi import FastAPI, HTTPException, Query, status
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from .data import sessions_db
from .schemas import SessionCreate

app = FastAPI(title="API Pemesanan Shuttle Kampus")

# Setup CORS agar frontend (localhost:5173) bisa akses
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. GET /sessions (Pagination + Search)
@app.get("/sessions")
def get_sessions(
    page: int = Query(1, ge=1),
    limit: int = Query(100, ge=1),
    search: Optional[str] = None
):
    data = sessions_db
    if search:
        data = [s for s in data if search.lower() in s["rute"].lower()]
    
    start = (page - 1) * limit
    return {
        "total": len(data), 
        "page": page, 
        "limit": limit, 
        "data": data[start:start+limit]
    }

# 2. GET /sessions/{id} (404 jika tidak ada)
@app.get("/sessions/{session_id}")
def get_session(session_id: int):
    for s in sessions_db:
        if s["id"] == session_id:
            return s
    raise HTTPException(status_code=404, detail="Sesi tidak ditemukan")

# 3. POST /sessions (201 Created)
@app.post("/sessions", status_code=status.HTTP_201_CREATED)
def create_session(session: SessionCreate):
    new_id = max([s["id"] for s in sessions_db], default=0) + 1
    new_session = {"id": new_id, **session.model_dump()} # Gunakan .model_dump() untuk Pydantic v2
    sessions_db.append(new_session)
    return new_session

# 4. DELETE /sessions/{id} (204 No Content)
@app.delete("/sessions/{session_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_session(session_id: int):
    global sessions_db
    initial_length = len(sessions_db)
    sessions_db = [s for s in sessions_db if s["id"] != session_id]
    if len(sessions_db) == initial_length:
        raise HTTPException(status_code=404, detail="Sesi tidak ditemukan")
    return

# 5. Health Check (untuk verifikasi dosen)
@app.get("/health")
def health():
    return {"status": "ok"}