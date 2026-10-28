import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

print("🔍 [RANGO S] Escaneando la armería de Google para detectar tu modelo disponible...")

# Autodetección del modelo exacto que tienes habilitado
modelo_elegido = 'gemini-pro' # Arma por defecto
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            nombre_limpio = m.name.replace('models/', '')
            # Nos quedamos con el primero que sirva para generar texto
            if 'gemini' in nombre_limpio:
                modelo_elegido = nombre_limpio
            # Si encuentra el flash o el pro nuevos, los prioriza y rompe el ciclo
            if 'flash' in nombre_limpio or '1.5' in nombre_limpio:
                modelo_elegido = nombre_limpio
                break
except Exception as e:
    print(f"⚠️ Aviso de escaneo: {e}")

print(f"🔫 [RANGO S] Modelo fijado y cargado: {modelo_elegido}")
model = genai.GenerativeModel(modelo_elegido)

print("🐎 Forjando aplicación educativa de Ponys (esto tomará unos segundos)...")

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
