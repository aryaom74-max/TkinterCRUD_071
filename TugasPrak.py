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

header_frame = tk.Frame(root, bg="#2c3e50", pady=10)
header_frame.pack(fill=tk.X)

lbl_title = tk.Label(
    header_frame,
    text="Sistem Prediksi Fakultas Siswa",
    font=("Helvetica", 14, "bold"),
    fg="white",
    bg="#2c3e50",
)
lbl_title.pack()


form_frame = tk.Frame(root, bg="#f4f6f9", padx=20, pady=15)
form_frame.pack(fill=tk.BOTH, expand=True)


tk.Label(
    form_frame,
    text="Nama Lengkap Siswa:",
    font=("Helvetica", 10),
    bg="#f4f6f9",
    anchor="w",
).grid(row=0, column=0, sticky="w", pady=8)
entry_nama = tk.Entry(form_frame, font=("Helvetica", 10), width=25)
entry_nama.grid(row=0, column=1, pady=8, padx=5)

tk.Label(
    form_frame,
    text="Nilai Biologi:",
    font=("Helvetica", 10),
    bg="#f4f6f9",
    anchor="w",
).grid(row=1, column=0, sticky="w", pady=8)
entry_biologi = tk.Entry(form_frame, font=("Helvetica", 10), width=25)
entry_biologi.grid(row=1, column=1, pady=8, padx=5)

tk.Label(
    form_frame,
    text="Nilai Fisika:",
    font=("Helvetica", 10),
    bg="#f4f6f9",
    anchor="w",
).grid(row=2, column=0, sticky="w", pady=8)
entry_fisika = tk.Entry(form_frame, font=("Helvetica", 10), width=25)
entry_fisika.grid(row=2, column=1, pady=8, padx=5)

tk.Label(
    form_frame,
    text="Nilai Bahasa Inggris:",
    font=("Helvetica", 10),
    bg="#f4f6f9",
    anchor="w",
).grid(row=3, column=0, sticky="w", pady=8)
entry_inggris = tk.Entry(form_frame, font=("Helvetica", 10), width=25)
entry_inggris.grid(row=3, column=1, pady=8, padx=5)

btn_proses = tk.Button(
    form_frame,
    text="Proses & Simpan Data",
    command=proses_prediksi,
    bg="#27ae60",
    fg="white",
    font=("Helvetica", 10, "bold"),
    width=22,
    pady=5,
)
btn_proses.grid(row=4, column=0, columnspan=2, pady=15)
output_frame = tk.LabelFrame(
    form_frame, text=" Hasil Prediksi ", font=("Helvetica", 10, "bold"), bg="#f4f6f9", padx=10, pady=10
)
output_frame.grid(row=5, column=0, columnspan=2, sticky="we", pady=5)

label_hasil_val = tk.Label(
    output_frame,
    text="Belum ada data diproses.",
    font=("Helvetica", 9),
    bg="#f4f6f9",
    fg="#555",
    justify="left",
)
label_hasil_val.pack(anchor="w")

root.mainloop()
