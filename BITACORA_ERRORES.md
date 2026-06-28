# Bitácora de Errores y Soluciones - Evaluación 4

Este documento registra los desafíos técnicos encontrados y resueltos durante el desarrollo de la automatización del router Cisco CSR1000v.

| Fase / Tarea | Error Reportado | Solución Aplicada |
| :--- | :--- | :--- |
| **Conexión SSH** | `The authenticity of host... can't be established` | Se creó un archivo `ansible.cfg` con `host_key_checking = False` para permitir la conexión desatendida. |
| **Interfaz Física** | `Invalid input detected at '^' marker` (GigabitEthernet2 no encontrada) | Se cambió el tipo de adaptador en VirtualBox a "Red paravirtualizada (virtio-net)" para compatibilidad con el kernel de Cisco. |
| **Python** | `error: externally-managed-environment` | Se implementó un entorno virtual de Python (`python3 -m venv`) para gestionar librerías de forma aislada. |
| **Ansible** | `ansible-pylibssh not installed` | Se ignoró la advertencia (warning) ya que Ansible redirige automáticamente la conexión a la librería `paramiko`, la cual estaba instalada correctamente. |
| **Git** | `Authentication failed` (Password authentication not supported) | Se generó un Token de Acceso Personal (PAT) clásico en GitHub con permisos de `repo` para autenticar la subida del código. |

---
