#!/bin/bash

echo "Ingrese carpeta a respaldar: "
read Fuente
echo "Ingrese ubicacion de respaldo: "
read Destino
fecha=`date +%Y-%m-%d_`
nom="${Fuente##*/}"
archivo="$fecha$nom.tar"


tar -cf $Destino/$archivo $Fuente

