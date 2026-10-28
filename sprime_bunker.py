import os
import time
import subprocess
import google.generativeai as genai
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from dotenv import load_dotenv

# 1. ABSORBER CLAVES AUTOMÁTICAMENTE DEL SISTEMA
load_dotenv()
console = Console()

# Buscar la API Key en el entorno o en el archivo .env sin preguntar
gemini_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if gemini_key:
    genai.configure(api_key=gemini_key)

def limpiar_pantalla():
    os.system('clear')

def mostrar_menu():
    limpiar_pantalla()
    estado_api = "[bold green]SINCRONIZADA (AUTOMÁTICO)[/bold green]" if gemini_key else "[bold red]NO ENCONTRADA EN .ENV[/bold red]"
    console.print(Panel.fit(
        f"[bold cyan]👁️  S-PRIME CORE: BÚNKER DE MANDO RANGO S[/bold cyan]\n"
        f"[yellow]RAM: 0.02 GB | Motor: Gemini Pro | Conexión: {estado_api}[/yellow]",
        border_style="cyan"
    ))
    
    tabla = Table(show_header=True, header_style="bold magenta", border_style="dim")
    tabla.add_column("Comando", justify="center")
    tabla.add_column("Acción de Guerra")
    tabla.add_row("1", "Auditar Estado de los 7 Cazadores Locales")
    tabla.add_row("2", "Desplegar Fábrica Autónoma (Ejecutar Agentes en Segundo Plano)")
    tabla.add_row("3", "Consultar Bitácora de Inteligencia")
    tabla.add_row("4", "Cerrar Búnker")
    console.print(tabla)

def menu_principal():
    while True:
        mostrar_menu()
        opcion = console.input("\n[bold cyan]DIRECTOR ❯[/bold cyan] ")
        
        if opcion == '1':
            limpiar_pantalla()
            console.print("[bold cyan]Escaneando archivos físicos de los Agentes...[/bold cyan]")
            # Verifica que los archivos reales existan en tu máquina
            archivos_agentes = ["agente_autonomo.py", "orquestador_maestro.py", "agentes_productores_shopify_v1.py"]
            for archivo in archivos_agentes:
                if os.path.exists(archivo):
                    console.print(f"[green]✓ {archivo} ... Listo y armado.[/green]")
                else:
                    console.print(f"[red]✗ {archivo} ... No encontrado.[/red]")
                time.sleep(0.5)
            console.input("\nPresiona ENTER para volver...")
            
        elif opcion == '2':
            limpiar_pantalla()
            console.print(Panel("[bold yellow]DESPLIEGUE AUTÓNOMO INICIADO[/bold yellow]"))
            console.print("[bold magenta]Ordenando a los 7 cazadores que inicien la producción...[/bold magenta]")
            
            # EJECUCIÓN REAL EN SEGUNDO PLANO (Nohup)
            # Esto ejecuta tu agente maestro sin trabar tu terminal y guardando los logs
            if os.path.exists("orquestador_maestro.py"):
                subprocess.Popen(["nohup", "python3", "orquestador_maestro.py"], stdout=open('fabrica_avanzada.log', 'a'), stderr=subprocess.STDOUT)
                console.print("[bold green]✅ Gremio de las Sombras desplegado en segundo plano.[/bold green]")
                console.print("[dim]Puedes cerrar esta terminal o apagar la pantalla. Ellos seguirán trabajando. Los reportes se guardan en 'fabrica_avanzada.log'.[/dim]")
            else:
                console.print("[bold red]❌ No se detectó 'orquestador_maestro.py' para iniciar la cadena.[/bold red]")
            
            console.input("\nPresiona ENTER para volver al menú...")
            
        elif opcion == '3':
            limpiar_pantalla()
            console.print("[bold cyan]Últimos movimientos del Gremio:[/bold cyan]\n")
            if os.path.exists("fabrica_avanzada.log"):
                os.system("tail -n 15 fabrica_avanzada.log")
            else:
                console.print("[dim]Aún no hay reportes en la bitácora.[/dim]")
            console.input("\nPresiona ENTER para volver...")
            
        elif opcion == '4':
            limpiar_pantalla()
            console.print("[bold red]Apagando interfaz de Mando. El Gremio sigue en las sombras... ARISE.[/bold red]")
            break

if __name__ == "__main__":
    menu_principal()
