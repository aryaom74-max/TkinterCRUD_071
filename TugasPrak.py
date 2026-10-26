import sqlite3
import tkinter as tk
from tkinter import messagebox

def init_db():
  conn = sqlite3.connect("nilai_siswa.db")
  cursor = conn.cursor()
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT,
            biologi REAL,
            fisika REAL,
            inggris REAL,
            prediksi_fakultas TEXT
        )
    """)
  conn.commit()
  conn.close()

def proses_prediksi():
  nama = entry_nama.get().strip()
  val_bio = entry_biologi.get().strip()
  val_fis = entry_fisika.get().strip()
  val_ing = entry_inggris.get().strip()

  if not nama or not val_bio or not val_fis or not val_ing:
    messagebox.showwarning(
        "Peringatan", "Semua kolom data nilai dan nama harus diisi!"
    )
    return

  try:
    biologi = float(val_bio)
    fisika = float(val_fis)
    inggris = float(val_ing)
  except ValueError:
    messagebox.showerror(
        "Error", "Nilai Biologi, Fisika, dan Inggris harus berupa angka valid!"
    )
    return

if biologi > fisika and biologi > inggris:
    prediksi = "Fakultas Kedokteran"
  elif fisika > biologi and fisika > inggris:
    prediksi = "Fakultas Teknik"
  elif inggris > biologi and inggris > fisika:
    prediksi = "Fakultas Bahasa & Sastra"
  else:
    prediksi = "Fakultas Multidisiplin (Terdapat nilai tertinggi yang sama)"

try:
    conn = sqlite3.connect("nilai_siswa.db")
    cursor = conn.cursor()
    cursor.execute(
        """
            INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
            VALUES (?, ?, ?, ?, ?)
        """,
        (nama, biologi, fisika, inggris, prediksi),
    )
    conn.commit()
    conn.close()

    label_hasil_val.config(
        text=f"Nama: {nama}\nHasil Rekomendasi: {prediksi}", fg="darkgreen"
    )
    messagebox.showinfo(
        "Berhasil", f"Data atas nama {nama} berhasil disimpan ke database!"
    )
    clear_form()

  except Exception as e:
    messagebox.showerror(
        "Database Error", f"Gagal menyimpan ke database: {str(e)}"
    )

def clear_form():
  entry_nama.delete(0, tk.END)
  entry_biologi.delete(0, tk.END)
  entry_fisika.delete(0, tk.END)
  entry_inggris.delete(0, tk.END)

init_db()

root = tk.Tk()
root.title("Sistem Rekomendasi Fakultas Siswa")
root.geometry("450x480")
root.config(bg="#f4f6f9")
