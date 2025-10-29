import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# --- Ventana ---
root = tk.Tk()
root.title("Área de Figuras")
root.geometry("550x500")
root.configure(bg="#616161")
root.resizable(False, False)

# --- Variables ---
figura = tk.StringVar(value="rectangulo")
resultado = tk.StringVar(value="Área: ")

# --- CARGAR IMÁGENES ---
def cargar_imagen(ruta, ancho, alto):
    try:
        img = Image.open(ruta)
        img = img.resize((ancho, alto), Image.LANCZOS)  # ← CALIDAD ALTA
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error cargando {ruta}: {e}")
        return None

# ← Usa los nombres EXACTOS de tus archivos
img_rect = cargar_imagen("rectangulo.jpg", 120, 80)
img_tri  = cargar_imagen("triangulo.jpg", 120, 100)
img_circ = cargar_imagen("circulo.png", 100, 100)

# --- Frames ---
frame = tk.Frame(root, bg="#e8f4f8")
frame.pack(expand=True, fill="both", padx=30, pady=25)

# --- Título ---
tk.Label(frame, text="Calculadora de Áreas", bg="#e8f4f8", font=("", 16, "bold"), fg="#2c3e50").grid(row=0, column=0, columnspan=3, pady=(0, 15))

# --- Radio buttons ---
radio_frame = tk.Frame(frame, bg="#e8f4f8")
radio_frame.grid(row=1, column=0, columnspan=3, pady=10)

tk.Radiobutton(radio_frame, text="Rectángulo", variable=figura, value="rectangulo", bg="#e8f4f8", font=("", 11)).pack(side="left", padx=30)
tk.Radiobutton(radio_frame, text="Triángulo", variable=figura, value="triangulo", bg="#e8f4f8", font=("", 11)).pack(side="left", padx=30)
tk.Radiobutton(radio_frame, text="Círculo", variable=figura, value="circulo", bg="#e8f4f8", font=("", 11)).pack(side="left", padx=30)

# --- Imagen ---
label_img = tk.Label(frame, bg="red")
label_img.grid(row=2, column=0, columnspan=3, pady=15)

# --- Entradas ---
entradas_frame = tk.Frame(frame, bg="black")
entradas_frame.grid(row=3, column=0, columnspan=3, pady=10)
entradas = {}

# --- Botones ---
botones_frame = tk.Frame(frame, bg="lightgray")
botones_frame.grid(row=4, column=0, columnspan=3, pady=20)

tk.Button(botones_frame, text="Calcular", command=lambda: calcular(), bg="#3498db", fg="white",font=("", 11, "bold"), relief="flat", cursor="hand2", width=12, height=2).pack(side="left", padx=20)
tk.Button(botones_frame, text="Borrar", command=lambda: borrar(), bg="#e74c3c", fg="white",font=("", 11, "bold"), relief="flat", cursor="hand2", width=12, height=2).pack(side="left", padx=20)

# --- Resultado ---
tk.Label(frame, textvariable=resultado, bg="#e8f4f8", font=("", 13, "bold"), fg="#27ae60").grid(row=5, column=0, columnspan=3, pady=10)

# --- Funciones ---
def cambiar_figura(*args):
    for w in entradas_frame.winfo_children():
        w.destroy()
    entradas.clear()

    f = figura.get()
    if f == "rectangulo":
        label_img.config(image=img_rect or "")
        crear_entrada("Base:", 0)
        crear_entrada("Altura:", 1)
    elif f == "triangulo":
        label_img.config(image=img_tri or "")
        crear_entrada("Base:", 0)
        crear_entrada("Altura:", 1)
    elif f == "circulo":
        label_img.config(image=img_circ or "")
        crear_entrada("Radio:", 0)
    resultado.set("Área: ")

def crear_entrada(texto, fila):
    tk.Label(entradas_frame, text=texto, bg="red", font=("", 11)).grid(row=fila, column=0, sticky="e", padx=10, pady=8)
    entry = tk.Entry(entradas_frame, font=("", 11), width=20)
    entry.grid(row=fila, column=1, padx=10, pady=8)
    entradas[texto.lower().split(":")[0]] = entry

def calcular():
    try:
        f = figura.get()
        if f == "rectangulo":
            area = float(entradas["base"].get()) * float(entradas["altura"].get())
        elif f == "triangulo":
            area = (float(entradas["base"].get()) * float(entradas["altura"].get())) / 2
        elif f == "circulo":
            import math
            area = math.pi * (float(entradas["radio"].get()) ** 2)
        resultado.set(f"Área: {area:.2f} u²")
    except:
        messagebox.showerror("Error", "Ingresa solo números")

def borrar():
    for e in entradas.values():
        e.delete(0, tk.END)
    resultado.set("Área: ")

# --- Iniciar ---
figura.trace("w", cambiar_figura)
cambiar_figura()

root.mainloop()