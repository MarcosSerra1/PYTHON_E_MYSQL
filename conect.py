import mysql.connector

db_connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="pythonsql")
cursor = db_connection.cursor()
sql = "INSERT INTO vendas (cliente, produto, data_venda, preco, quantidade) VALUES (%s, %s, %s, %s, %s)"
values = ('Newt Scamander', 'ANIMAIS FANTASTICOS', '2023-03-08', '6600.65', '2')
cursor.execute(sql, values)

sql = ("SELECT * FROM vendas")
cursor.execute(sql)

for (id_venda, cliente, produto, data_venda, preco, quantidade) in cursor:
  print(id_venda, cliente, produto, data_venda, preco, quantidade)
print("\n")

#sql = ("update vendas set cliente='Ronald Weasley', produto='NOTEBOOK ACER NITRO', data_venda='2023-01-10', preco='3508.99' where quantidade='1'")
cursor.execute(sql)

print(cursor.rowcount, "record updated.")
print("\n")

#sql = ("SELECT id_venda, cliente, produto, data_venda, preco, quantidade FROM vendas") #serve para modificar um cadastro
#cursor.execute(sql) #executa a ultima variavel inserida 

for (id_venda, cliente, produto, data_venda, preco, quantidade) in cursor:
  print(id_venda, cliente, produto, data_venda, preco, quantidade)
  
cursor.close()
db_connection.commit()
db_connection.close()


