# Aplikasi Pencatat Sesi Pelatihan Shuttle Kampus

## 1. Prasyarat
- Python 3.9 atau lebih baru
- Node.js 18 atau lebih baru
- Git

## 2. Layanan
Aplikasi ini terdiri dari dua layanan utama:
- Backend (FastAPI): Berjalan di http://localhost:8000 untuk mengelola data sesi shuttle (GET, POST, DELETE).
- Frontend (Vue 3 + Vite): Berjalan di http://localhost:5173 untuk antarmuka pengguna.

## 3. Cara Menjalankan
Backend:
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

Frontend:
cd frontend
npm install
npm run dev

## 4. Cara Memverifikasi
1. Buka http://localhost:8000/docs di browser untuk memastikan API berjalan (uji endpoint GET /sessions).
2. Buka http://localhost:5173 di browser.
3. Pastikan tabel menampilkan data awal.
4. Coba tambahkan data baru melalui form, pastikan data muncul di tabel.
5. Coba hapus data, pastikan muncul konfirmasi dan data terhapus dari tabel.
6. Matikan backend, refresh browser, pastikan muncul pesan error dan tombol "Coba Lagi (Retry)".

## 5. Masalah yang Sering Muncul
- Data tidak muncul: Pastikan backend berjalan dan limit pagination di backend cukup besar (misal 100).
- CORS Error: Pastikan konfigurasi CORS di main.py mengizinkan http://localhost:5173.
- Error saat menjalankan venv: Gunakan Command Prompt (CMD) alih-alih PowerShell jika terjadi masalah Execution Policy.

## Catatan
Saya menggunakan AI (Deepseek) untuk membantu mempercepat penulisan boilerplate kode, debugging, dan penyusunan langkah-langkah setup. Logika utama, integrasi API, dan pengujian aplikasi dikerjakan secara mandiri.