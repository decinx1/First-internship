import os
from tabulate import tabulate

# Define los parámetros específicos que buscas en los archivos txt
PARAMS = [
    "Nombre de usuario", "Modelo", "Dirección IP primaria", "mascara",
    "gateway", "Nombre de host DNS", "Dirección MAC primaria", "Sistema operativo",
    "Tipo de CPU", "Memoria del sistema", "Unidad de disco", "Tamaño total", "Monitor",
    "Teclado", "Mouse", "bocinas"
]

def read_txt_files(directory):
    data = []
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            try:
                print(f"Leyendo archivo: {filepath}")
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    lines = content.splitlines()
                    file_data = {param: None for param in PARAMS}
                    for line in lines:
                        parts = line.split()
                        if len(parts) > 1:
                            key = ' '.join(parts[:-1]).strip()
                            value = parts[-1].strip()
                            for param in PARAMS:
                                if param.lower() in key.lower():
                                    file_data[param] = value
                    data.append(file_data)
                print(f"Archivo leído con éxito: {filepath}")
            except Exception as e:
                print(f"Error al analizar el archivo {filepath}: {e}\n")
    return data

def main():
    directory = r'C:\xampp\htdocs\First-internship\ACT 13062024'  # Ajusta esta ruta según sea necesario
    
    print(f"Leyendo archivos desde el directorio: {directory}")
    new_data = read_txt_files(directory)
    print(f"Datos nuevos leídos: {len(new_data)} archivos procesados")

    # Imprimir los datos en formato tabulado
    print(tabulate(new_data, headers="keys", tablefmt="grid"))

if __name__ == '__main__':
    main()
