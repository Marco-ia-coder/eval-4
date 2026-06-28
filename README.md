# Evaluación 4: Automatización de Redes

Este repositorio contiene la entrega de la **Evaluación 4** de la asignatura, enfocada en la automatización de infraestructura de redes utilizando **Ansible**, **Python (Netmiko)** y **Bash**.

## Estructura del Proyecto
* `fase1_playbook.yml`: Playbook de Ansible para la configuración base (Hostname, NTP, SSH, Logging de seguridad) y despliegue de interfaces lógicas (VLAN 10, 20, 30).
* `hosts.ini`: Inventario de dispositivos para Ansible.
* `ansible.cfg`: Configuración personalizada para evitar avisos de advertencia y verificación de llaves SSH.
* `fase2_validacion.py`: Script de Python que valida la conectividad y el estado del servicio NTP, exportando los resultados a un archivo `.json`.
* `fase3_backup.py`: Script de Python para realizar el respaldo automático de la `running-config` del router.
* `fase4_orquestador.sh`: Script en Bash que ejecuta de forma secuencial todas las fases del proyecto.

## Requisitos de Ejecución
* Cisco CSR1000v (GNS3, EVE-NG o VirtualBox).
* Ansible 2.9+.
* Python 3.8+ con librerías `netmiko` y `paramiko`.

## Bitácora de Resolución de Problemas
Durante el desarrollo se presentaron los siguientes desafíos:
1. **Error SSH (`host_key_checking`):** Solucionado configurando `ansible.cfg` para desactivar la verificación de llaves.
2. **Interfaz no reconocida:** El router no detectaba `GigabitEthernet2`. Se solucionó cambiando el adaptador de red en VirtualBox a "Red paravirtualizada (virtio-net)".
3. **Error SSH (`authenticity of host`):** Solucionado con `host_key_checking = False` en `ansible.cfg`.
4. **Error `externally-managed-environment` en Python:** Solucionado mediante el uso de entornos virtuales (`venv`) y la instalación correcta de librerías.

---
*Autor: Marco-ia-coder*
