#! /bin/bash

VALID_PASSWORD="secret"

echo "ingrese una VALID_PASSWORD "
read PASSWORD
# importante los espacios al inicio y al final
#de los corchetes
if ["$PASSWORD" == "VALID_PASSWORD" ]; then
	echo "Acceso concedido"
else
	echo "Acceso denegado"
fi
