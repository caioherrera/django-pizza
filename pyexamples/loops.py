pedidos = [
    {
        'nome': 'Mario',
        'sabor': 'portuguesa'
    },
    {
        'nome': 'Marco',
        'sabor': 'presunto'
    }
]

for pedido in pedidos:
    print('--------------------------\nNome: {0}\nSabor: {1}'.format(pedido['nome'], pedido['sabor']))
print('--------------------------')
