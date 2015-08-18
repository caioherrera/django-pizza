pedidos = []


def cria_pedido(nome, sabor, observacao='Sem observacoes'):
    pedido = {'nome': nome, 'sabor': sabor, 'observacao': observacao}
    return pedido

pedidos.append(cria_pedido('Mario', 'pepperoni'))
pedidos.append(cria_pedido('Marco', 'bacon'))
for pedido in pedidos:
    t = 'Nome: {0}\nSabor: {1}\nObservacao: {2}\n'
    print(t.format(pedido['nome'], pedido['sabor'], pedido['observacao']))
