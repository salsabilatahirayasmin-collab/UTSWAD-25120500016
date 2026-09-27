JUDUL : Aplikasi Pencatat Sesi Pelatihan Shuttle Kampus

Cara Menjalankan Backend:
cd backend
python -m venv venv
# Windows: venv\Scripts\activate
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload 

Cara Menjalankan Frontend:
cd frontend
npm install
npm run dev

Catatan:
Saya menggunakan AI (Deepseek) untuk membantu mempercepat penulisan boilerplate kode, debugging, dan penyusunan langkah-langkah setup. Logika utama, integrasi API, dan pengujian aplikasi dikerjakan secara mandiri.