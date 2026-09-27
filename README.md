# JUDUL : Aplikasi Pencatat Sesi Pelatihan Shuttle Kampus

## Cara Menjalankan Backend:
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

## Cara Menjalankan Frontend:
cd frontend
npm install
npm run dev

## Persyaratan yang Dipenuhi
- [x] Dataset in-memory 12+ baris (`backend/app/data.py`)
- [x] GET /sessions (pagination + search)
- [x] GET /sessions/{id} (404 jika tidak ada)
- [x] POST /sessions (201 Created, validasi Pydantic)
- [x] DELETE /sessions (204 No Content)
- [x] CORS untuk frontend
- [x] Frontend Vue 3 + Vite (Daftar, 4 state + retry, Form + validasi, Hapus + konfirmasi)

## Catatan:
Saya menggunakan AI (Deepseek) untuk membantu mempercepat penulisan boilerplate kode, debugging, dan penyusunan langkah-langkah setup. Logika utama, integrasi API, dan pengujian aplikasi dikerjakan secara mandiri.