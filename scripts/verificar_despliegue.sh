
#!/bin/bash

# Detener la ejecución si ocurre algún error
set -e

echo "======================================"
echo " VERIFICANDO DESPLIEGUE DE LA APLICACION"
echo "======================================"

# URL de la aplicación desplegada
URL="${1:-}"

# Validar que se haya proporcionado una URL
if [ -z "$URL" ]; then
    echo "ERROR: Debes proporcionar la URL de la aplicación."
    echo "Uso: bash scripts/verificar_despliegue.sh https://tu-aplicacion.onrender.com"
    exit 1
fi

# Consultar la aplicación
echo "Consultando: $URL"

if curl --fail --silent --show-error "$URL"; then
    echo ""
    echo "======================================"
    echo " DESPLIEGUE VERIFICADO CORRECTAMENTE"
    echo "======================================"
else
    echo ""
    echo "======================================"
    echo " ERROR: LA APLICACION NO RESPONDE"
    echo "======================================"
    exit 1
fi
