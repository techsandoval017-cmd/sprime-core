import os

html_gremio = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>S-Prime | Mesa del Gremio (Argon Powered)</title>
    <style>
        body { background: #000; color: #fff; font-family: 'Consolas', monospace; padding: 20px; }
        .header { border-bottom: 2px solid #635bff; padding-bottom: 10px; margin-bottom: 20px; }
        h1 { color: #635bff; margin: 0; }
        .terminal { background: #111; border: 1px solid #333; padding: 15px; border-radius: 5px; height: 400px; overflow-y: auto; }
        .agent-e { color: #888; }
        .agent-c { color: #00ffcc; }
        .agent-a { color: #ffaa00; }
        .agent-s { color: #ff3333; font-weight: bold; }
        input, button { width: 100%; padding: 12px; margin-top: 10px; background: #222; color: #fff; border: 1px solid #444; border-radius: 4px; }
        button { background: #635bff; font-weight: bold; cursor: pointer; text-transform: uppercase; border: none; }
        button:hover { background: #4b44cc; }
    </style>
</head>
<body>
    <div class="header">
        <h1>👁️ MESA REDONDA DEL GREMIO</h1>
        <p>Motor de Análisis: Gemini 4 Argon | Objetivo: 21 Software Rango S (Obsidian Prime)</p>
    </div>
    
    <label>Ingresa la App o Nicho a someter a Ingeniería Inversa (Ej. CRM Inmobiliario, Agendador Clínico):</label>
    <input type="text" id="nicho_input" placeholder="Nombre de la app o nicho...">
    <button onclick="simularGremio()">Iniciar Análisis Multi-Agente</button>

    <div class="terminal" id="terminal_output" style="margin-top: 20px;">
        [S-PRIME CORE] Esperando objetivo para aplicar ingeniería inversa...
    </div>

    <script>
        function simularGremio() {
            const nicho = document.getElementById('nicho_input').value;
            const terminal = document.getElementById('terminal_output');
            if(!nicho) return;

            terminal.innerHTML = `<br><span style="color:#00ffcc">Iniciando protocolo Argon sobre: ${nicho}...</span>`;
            
            setTimeout(() => {
                terminal.innerHTML += `<br><br><span class="agent-e">[RANGO E - SCRAPER]:</span> Analizando competidores. Alta demanda detectada. Problema principal: Las apps actuales son muy caras y requieren mantenimiento técnico del cliente.`;
            }, 1500);

            setTimeout(() => {
                terminal.innerHTML += `<br><span class="agent-c">[RANGO C - CÓDIGO]:</span> Ingeniería inversa completada. Podemos replicar la base de datos central en 4 horas usando CRUD dinámico. Cero mantenimiento. El cliente agregará y borrará con botones simples.`;
            }, 3000);

            setTimeout(() => {
                terminal.innerHTML += `<br><span class="agent-a">[RANGO A - VENTAS]:</span> El valor agregado será la integración. Empaquetaremos esto como una 'Golden Suite'. Los alumnos de la academia lo venderán a negocios locales y se quedarán el 40% de la comisión recurrente.`;
            }, 4500);

            setTimeout(() => {
                terminal.innerHTML += `<br><span class="agent-s">[RANGO S - MONARCA]:</span> Análisis aprobado. Rentabilidad asegurada. Producto añadido a la lista de los 21 Software de Obsidian Prime. Pasando a fase de Producción y Diseño UI. Comandante, proceda.`;
            }, 6000);
        }
    </script>
</body>
</html>
"""

os.makedirs("panel_maestro", exist_ok=True)
with open("panel_maestro/mesa_gremio.html", "w", encoding="utf-8") as f:
    f.write(html_gremio)

# Inyectar ruta en main.py
print("✅ Inyectando Mesa del Gremio en el Servidor...")
import sys
with open('main.py', 'r') as f:
    codigo = f.read()
if 'montar(\'/gremio\'' not in codigo:
    codigo = codigo.replace('montar(\'/panel\'', 'montar(\'/gremio\', \'panel_maestro\')\nmontar(\'/panel\'')
    with open('main.py', 'w') as f:
        f.write(codigo)

print("🚀 LISTO. Reinicia tu servidor local con: uvicorn main:app --host 0.0.0.0 --port 8000")
