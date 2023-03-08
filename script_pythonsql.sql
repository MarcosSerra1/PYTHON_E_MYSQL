create database pythonsql
default character set utf8mb4
default collate utf8mb4_general_ci;

use pythonsql;

create table vendas (
id_venda int not null auto_increment,
cliente varchar(50) not null,
produto varchar(50) not null,
data_venda date not null,
preco decimal(6,2),
quantidade int,
primary key (id_venda)
) default charset = utf8mb4;

insert into vendas
(id, cliente, produto, data_venda, preco, quantidade)
values
(default, 'Harry Potter', 'READMI NOTE 11 PRO 5G', '08/03/2023', '2600.65', '1'),
(default, 'Hermione Granger', 'NOTEBOOK ACER NITRO 5', '03/02/2023', '6600.65', '2'),
(default, 'Ronald Weasley', 'NOTEBOOK ACER NITRO', '03/03/2023', '3508.99', '1');


