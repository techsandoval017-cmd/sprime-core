import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Cargando la nueva artillería exigida por la armería de Google
modelo_elegido = 'gemini-3.8-flash'
print(f"🔫 [RANGO S] Modelo fijado y cargado: {modelo_elegido}")
model = genai.GenerativeModel(modelo_elegido)

print("🐎 Forjando aplicación educativa de Ponys con IA de última generación...")

prompt = """Actúa como Ingeniero Frontend Rango S. 
Crea una aplicación web interactiva y sencilla para niños en un solo archivo HTML (con CSS y JS integrados). 
Tema: Caballos y Ponys. 
Objetivo: Aprender las 5 vocales. 
Diseño: Colorido, amigable. Debe tener 5 botones grandes (uno para cada vocal). Al hacer clic en un botón, debe aparecer el dibujo o emoji de un pony junto con una palabra relacionada (ej. A de Alazán, E de Equino) y una pequeña animación.
Entrega SOLO el código HTML final, sin markdown, sin explicaciones previas ni posteriores."""

respuesta = model.generate_content(prompt)
codigo = respuesta.text.replace("```html", "").replace("```", "")

with open("app_ponys.html", "w", encoding="utf-8") as f:
    f.write(codigo)

print("✅ [ÉXITO] Software terminado y guardado como: app_ponys.html")
