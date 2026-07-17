import threading
from pathlib import Path
import customtkinter as ctk
from tkinter import filedialog, messagebox
from core import redimensionar_imagen, ErrorValidacion, ErrorImagen

class Ventana(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Redimensionador de Fotos")
        self.geometry("480x300")
        self.resizable(False, False)

        self.ruta = ctk.StringVar()
        self.ancho = ctk.IntVar(value=800)

        titulo = ctk.CTkLabel(self, text="Reducir tamaño de fotos", font=ctk.CTkFont(size=18, weight="bold"))
        titulo.pack(pady=15)

        marco = ctk.CTkFrame(self)
        marco.pack(padx=20, pady=10, fill="x")

        btn_sel = ctk.CTkButton(marco, text="Elegir foto", command=self.elegir)
        btn_sel.pack(side="left", padx=10, pady=10)

        lbl = ctk.CTkLabel(marco, textvariable=self.ruta, width=250, anchor="w")
        lbl.pack(side="left", padx=5)

        marco2 = ctk.CTkFrame(self)
        marco2.pack(padx=20, pady=5, fill="x")
        ctk.CTkLabel(marco2, text="Ancho máximo (px):").pack(side="left", padx=10)
        ctk.CTkEntry(marco2, textvariable=self.ancho, width=80).pack(side="left")

        btn_ok = ctk.CTkButton(self, text="Redimensionar", command=self.en_hilo)
        btn_ok.pack(pady=15)

        self.estado = ctk.CTkLabel(self, text="Selecciona una imagen", text_color="gray")
        self.estado.pack()

    def elegir(self):
        archivo = filedialog.askopenfilename(
            filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg")]
        )
        if archivo:
            self.ruta.set(archivo)
            self.estado.configure(text="Listo para redimensionar", text_color="white")

    def en_hilo(self):
        if not self.ruta.get():
            messagebox.showwarning("Aviso", "Primero elige una foto.")
            return
        self.estado.configure(text="Procesando...", text_color="orange")
        threading.Thread(target=self.procesar, daemon=True).start()

    def procesar(self):
        entrada = Path(self.ruta.get())
        salida = entrada.with_name(entrada.stem + "_pequeña.jpg")

        try:
            redimensionar_imagen(str(entrada), str(salida), self.ancho.get())
            tam_in = entrada.stat().st_size / 1024
            tam_out = salida.stat().st_size / 1024
            msg = "Guardado: " + salida.name + "\nAntes: %.1f KB\nDespués: %.1f KB" % (tam_in, tam_out)
            self.after(0, self.exito, msg)
        except (ErrorValidacion, ErrorImagen) as e:
            self.after(0, self.fallo, str(e))

    def exito(self, msg):
        self.estado.configure(text="Listo", text_color="green")
        messagebox.showinfo("Correcto", msg)
        self.ruta.set("")

    def fallo(self, msg):
        self.estado.configure(text="Error", text_color="red")
        messagebox.showerror("Error", msg)

if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    Ventana().mainloop()
