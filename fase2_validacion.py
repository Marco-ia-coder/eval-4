from netmiko import ConnectHandler
import json
from datetime import datetime

# Definir los parametros de conexion al router
router_m_castillo = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.101', # Asegurate de que esta sea la IP correcta
    'username': 'admin',
    'password': 'cisco123',
    'secret': 'cisco123',     # Contrasena de modo privilegiado (enable)
}

def validar_red():
    print("Iniciando Fase 2: Validacion de Red con Netmiko...")
    
    try:
        # 1. Establecer conexion
        print(f"Conectando a {router_m_castillo['host']}...")
        conexion = ConnectHandler(**router_m_castillo)
        conexion.enable()
        
        # 2. Ejecutar comandos de validacion
        print("Obteniendo estado de las interfaces...")
        salida_interfaces = conexion.send_command("show ip interface brief")
        
        print("Obteniendo estado del servicio NTP...")
        salida_ntp = conexion.send_command("show ntp associations")
        
        # 3. Estructurar los datos para el reporte
        datos_reporte = {
            "fecha_validacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "dispositivo": "M-Castillo",
            "resultados_validacion": {
                "estado_interfaces": salida_interfaces,
                "estado_ntp": salida_ntp
            },
            "estado_general": "Exitoso"
        }
        
        # 4. Generar archivo JSON
        nombre_archivo = 'reporte_validacion_fase2.json'
        with open(nombre_archivo, 'w') as archivo_json:
            json.dump(datos_reporte, archivo_json, indent=4)
            
        print(f"\n¡Validacion completada! Reporte generado exitosamente en: {nombre_archivo}")
        
        # Cerrar conexion
        conexion.disconnect()
        
    except Exception as e:
        print(f"Ocurrio un error durante la validacion: {e}")

if __name__ == "__main__":
    validar_red()
