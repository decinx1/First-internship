import os
import pandas as pd

def read_txt_files(directory):
    data = {}
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            try:
                print(f"Leyendo archivo: {filepath}")
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    # Procesar el contenido del archivo
                    lines = content.splitlines()
                    for line in lines:
                        # Suponiendo que los datos están separados por comas
                        parts = line.split(',')
                        if len(parts) > 1:
                            key = parts[0].strip()
                            value = ','.join(parts[1:]).strip()
                            if key in data:
                                data[key].append(value)
                            else:
                                data[key] = [value]
                print(f"Archivo leído con éxito: {filepath}")
            except Exception as e:
                print(f"Error al analizar el archivo {filepath}: {e}\n")
    return data

def update_excel_file(excel_file, sheet_name, new_data):
    try:
        # Verificar si el archivo existe y si tiene permisos adecuados
        if not os.access(excel_file, os.W_OK):
            raise PermissionError(f"No se puede escribir en el archivo: {excel_file}")

        # Leer los datos existentes en la hoja de cálculo
        df_existing = pd.read_excel(excel_file, sheet_name=sheet_name)
        
        for key, values in new_data.items():
            if key in df_existing.columns:
                for i, value in enumerate(values):
                    if i < len(df_existing):
                        df_existing.at[i, key] = value
                    else:
                        new_row = pd.Series({key: value})
                        df_existing = pd.concat([df_existing, new_row.to_frame().T], ignore_index=True)
        
        # Guardar el DataFrame actualizado en la hoja de cálculo
        mode = 'a' if os.path.exists(excel_file) else 'w'
        with pd.ExcelWriter(excel_file, engine='openpyxl', mode=mode, if_sheet_exists='replace') as writer:
            df_existing.to_excel(writer, sheet_name=sheet_name, index=False)
    except PermissionError as e:
        print(f"Error de permisos al acceder al archivo: {excel_file}. Asegúrate de que el archivo no esté abierto en otra aplicación y que tengas permisos de lectura y escritura.")
    except Exception as e:
        print(f"Error al actualizar la hoja de cálculo: {excel_file}")
        print(e)

def main():
    directory = r'C:\xampp\htdocs\First-internship\ACT 13062024'
    excel_file = r'C:\Users\decinx\OneDrive\Escritorio\si.xlsx'  # Asegúrate de que la ruta es correcta y que tienes permisos
    sheet_name = 'Hoja1'  # Asegúrate de que este nombre coincida con la hoja en tu archivo Excel
    
    print(f"Leyendo archivos desde el directorio: {directory}")
    new_data = read_txt_files(directory)
    print(f"Datos nuevos leídos: {len(new_data)} filas")
    update_excel_file(excel_file, sheet_name, new_data)
    print("Actualización completada.")

if __name__ == '__main__':
    main()
