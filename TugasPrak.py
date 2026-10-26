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
