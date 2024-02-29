import subprocess

try:
    result = subprocess.run(['pip', 'show', 'pyinstaller'], capture_output=True, text=True)
    output_lines = result.stdout.split('\n')
    for line in output_lines:
        if line.startswith('Location:'):
            pyinstaller_location = line.split(':', 1)[1].strip()
            print("La ubicación de PyInstaller es:", pyinstaller_location)
            break
    else:
        print("PyInstaller no está instalado.")
except Exception as e:
    print("Ocurrió un error al intentar obtener la ubicación de PyInstaller:", e)
