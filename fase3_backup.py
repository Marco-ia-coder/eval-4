from netmiko import ConnectHandler
import json
from datetime import datetime

# Usamos las mismas credenciales que validaste en la Fase 2
router_m_castillo = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.101',
    'username': 'admin',
    'password': 'cisco123',
    'secret': 'cisco123',
}

def realizar_backup():
    print("Iniciando Fase 3: Respaldo de Configuracion...")
    
    try:
        conexion = ConnectHandler(**router_m_castillo)
        conexion.enable()
        
        print("Extrayendo 'running-config' del router...")
        configuracion = conexion.send_command("show running-config")
        
        # Obtener fecha y hora actual para cumplir con el requerimiento
        ahora = datetime.now()
        fecha_hora_str = ahora.strftime("%Y-%m-%d_%H-%M-%S")
        fecha_hora_json = ahora.strftime("%Y-%m-%d %H:%M:%S")
        
        # Estructurar los datos del backup para el JSON
        datos_backup = {
            "dispositivo": "M-Castillo",
            "fecha_respaldo": fecha_hora_json,
            "tipo_respaldo": "running-config",
            "configuracion": configuracion
        }
        
        # Guardar en archivo JSON
        nombre_archivo = f'backup_config_{fecha_hora_str}.json'
        with open(nombre_archivo, 'w') as archivo_json:
            json.dump(datos_backup, archivo_json, indent=4)
            
        print(f"¡Respaldo exitoso! Archivo guardado como: {nombre_archivo}")
        
        conexion.disconnect()
        
    except Exception as e:
        print(f"Ocurrio un error durante el respaldo: {e}")

if __name__ == "__main__":
    realizar_backup()
