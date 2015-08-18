pedidos = []


def cria_pedido(nome, sabor, observacao=None):
    pedido = {'nome': nome, 'sabor': sabor, 'observacao': observacao}
    return pedido

pedidos.append(cria_pedido('Mario', 'pepperoni'))
pedidos.append(cria_pedido('Marco', 'bacon', 'sem bacon'))
for pedido in pedidos:
    t = 'Nome: {nome}\nSabor: {sabor}'
    if pedido['observacao']:
        t += '\nObservacao: {observacao}'
    print(t.format(**pedido))
    print('-' * 40)
