#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
conn = sqlite3.connect("pos_empresa.db")
cursor = conn.cursor()

# Total de ventas año 2013
cursor.execute("select sum(gross_total) from sale where [date] between '2013-01-01' and '2013-12-31'")
print "////////////////////////////////////////////////"   
for i in cursor:
	print "Total ventas 2013: ", i[0]


cursor.execute("select product.name, avg(net_unit_price) from sale_product join product on sale_product.product_id = product.id group by product.name limit 10")
print "////////////////////////////////////////////////"
print "nombre del producto   :   precio promedio venta"
print "////////////////////////////////////////////////" 
for i in cursor:
	print i[0],"   :   ", i[1]

cursor.execute("select entity.names, sum(gross_total) from sale join entity on sale.entity_id = entity.id group by entity.names limit 20;")
print "////////////////////////////////////////////////"
print "nombre cliente   :   promedio ventas"
print "////////////////////////////////////////////////"
for i in cursor:
	print i[0],"   :   ", i[1]

cursor.execute("select entity.names, sum(gross_total) from sale join entity on sale.entity_id = entity.id group by entity.names limit 20;")
print "////////////////////////////////////////////////"
print "nombre cliente   :   ventas 2014 "
print "////////////////////////////////////////////////"
for i in cursor:
	print i[0],"   :   ",i[1]

cursor.execute("select count(*), sum(gross_total) from sale where sale.[date]  between '2013-11-01' and '2013-11-31' group by sale.[date]  limit 10;")
print "////////////////////////////////////////////////"
print " cantidad de articulos   :   total venta diaria"
print "////////////////////////////////////////////////"
for i in cursor:
	print i[0],"   :   ",i[1]

cursor.execute("select product.name, sale_product.quantity, sum(gross_total) from sale_product join product on sale_product.product_id = product.id group by product.name order by sale_product.quantity desc limit 10")
print "////////////////////////////////////////////////"
print " nombre del porducto   :   cantidad   :   total"
print "////////////////////////////////////////////////"
for i in cursor:
	print i[0],"   :   ", i[1],"   :   ",i[2]




conn.close()
