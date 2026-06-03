from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sympy as sp

app = FastAPI()

# Mengizinkan Frontend (HTML/JS) berkomunikasi dengan Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Format data yang akan diterima dari Frontend
class SoalLimit(BaseModel):
    fungsi: str      # Contoh: "(x**2 - 1)/(x - 1)"
    variabel: str    # Contoh: "x"
    menuju: str      # Contoh: "1" atau "oo" (untuk tak hingga)

@app.post("/hitung-limit")
async def hitung_limit(soal: SoalLimit):
    try:
        # --- 1. TAMBAHKAN BARIS INI ---
        # Membersihkan input user: ubah otomatis tanda ^ menjadi **
        teks_fungsi_bersih = soal.fungsi.replace("^", "**")
        
        # Mengubah string menjadi simbol matematika SymPy
        var = sp.Symbol(soal.variabel)
        
        # --- 2. UBAH BARIS INI ---
        # Masukkan 'teks_fungsi_bersih' ke dalam sympify, bukan 'soal.fungsi' lagi
        fungsi_matematika = sp.sympify(teks_fungsi_bersih) 
        
        nilai_tujuan = sp.sympify(soal.menuju)
        
        # Menghitung limit
        hasil = sp.limit(fungsi_matematika, var, nilai_tujuan)
        
        # (Opsional/Tingkat Lanjut) Membuat logika step-by-step sederhana
        substitusi = fungsi_matematika.subs(var, nilai_tujuan)
        langkah = f"Substitusi langsung {soal.variabel} = {soal.menuju}."
        
        # PERBAIKAN: Mengecek error menggunakan string agar lebih kebal error
        hasil_substitusi_str = str(substitusi).lower()
        
        # Mengecek apakah hasilnya tak tentu (nan), tak hingga (oo), atau pembagian nol (zoo)
        if hasil_substitusi_str in ["nan", "zoo", "oo", "-oo"]:
            langkah = "Substitusi langsung menghasilkan bentuk tak tentu. Dievaluasi lebih lanjut dengan algoritma limit."
            
        return {
            "sukses": True,
            "hasil": str(hasil),
            "langkah_awal": langkah,
            "fungsi_latex": sp.latex(fungsi_matematika) # Berguna untuk dirender di UI
        }
    except Exception as e:
        return {"sukses": False, "pesan_error": str(e)}

# Jalankan server dengan perintah terminal: uvicorn main:app --reload