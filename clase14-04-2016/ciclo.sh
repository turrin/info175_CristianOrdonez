#! /bin/bash
#declarar un arreglo con 4 elementos
ARRY=( 'Debian Linux' 'Redhat Linux' Ubuntu Linux )
#obtener el numero de elementos
ELEMENTS=${#ARRAY[@]}
#imprimir todos los elementos
for (( i=0;i<$ELEMENTS;i++ )); do
	echo ${ARRAY[${i}]}
done