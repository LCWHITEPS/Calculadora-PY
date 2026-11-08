
#!/bin/bash

# Detener la ejecución si ocurre algún error
set -e

echo "======================================"
echo " INICIANDO PRUEBAS DEL PROYECTO"
echo "======================================"

# Instalar dependencias
echo "Instalando dependencias..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Ejecutar pruebas
echo "Ejecutando pruebas automatizadas..."
python -m pytest -v

# Resultado
echo "======================================"
echo " TODAS LAS PRUEBAS FINALIZARON CORRECTAMENTE"
echo "======================================"
