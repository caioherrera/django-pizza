pedidos = []


def adiciona_pedido(nome, sabor):
    pedido = {'nome': nome, 'sabor': sabor}
    return pedido

pedidos.append(adiciona_pedido('Mario', 'pepperoni'))
pedidos.append(adiciona_pedido('Marco', 'bacon'))
for pedido in pedidos:
    print('Nome: {0}\nSabor: {1}\n'.format(pedido['nome'], pedido['sabor']))
