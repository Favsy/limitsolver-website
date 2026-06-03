# LIMIT SOLVER

LIMIT SOLVER adalah  web yang dirancang khusus untuk menyelesaikan soal-soal kalkulus, khususnya limit fungsi matematika. 
Proyek ini merupakan proyek iseng dan kemungkinan masih banyak bug yang terkandung di dalamnya

## Teknologi yang Digunakan

* **Frontend:** HTML5, CSS3 dan Vanilla JavaScript.
* **Backend:** Python 3, FastAPI 
* **Mesin Matematika:** SymPy 
* **Server ASGI:** Uvicorn.

## Cara Menjalankan Proyek Secara Lokal

Karena proyek ini bergantung pada pemrosesan server Python, file `index.html` tidak dapat langsung mengeksekusi perhitungan tanpa backend yang berjalan. langkah-langkah  yang perlu dilakukan untuk menjalankan server di lingkungan lokal:

### 1. Persiapan Sistem (Prerequisites)
Pastikan Python 3 sudah terinstal di komputer Anda. Saat melakukan instalasi Python di sistem operasi Windows, sangat disarankan untuk memastikan opsi **"Add Python to PATH"** telah dicentang.

### 2. Instalasi Dependensi
Buka terminal (Command Prompt atau PowerShell), navigasikan ke direktori proyek ini, lalu instal semua pustaka (library) Python yang dibutuhkan dengan menjalankan perintah berikut:

```bash
pip install fastapi uvicorn sympy pydantic
