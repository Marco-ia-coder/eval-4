#!/bin/bash

echo "========================================================"
echo "  INICIANDO AUTOMATIZACION COMPLETA - EVALUACION 4"
echo "========================================================"

echo -e "\n---> [1/3] Ejecutando Fase 1: Configuracion con Ansible"
ansible-playbook -i hosts.ini fase1_playbook.yml

echo -e "\n---> [2/3] Ejecutando Fase 2: Validacion con Netmiko"
python3 fase2_validacion.py

echo -e "\n---> [3/3] Ejecutando Fase 3: Respaldo de Configuracion"
python3 fase3_backup.py

echo -e "\n========================================================"
echo "  EJECUCION FINALIZADA CON EXITO"
echo "========================================================"
