class Pedido:
    estados = [
        'Pedido Realizado',
        'Pedido en Creación',
        'Pedido Enviado',
        'Pedido en Reparto',
        'Pedido Entregado'
    ]

    def __init__(self, id_pedido):
        self.id_pedido = id_pedido
        self.estado_actual = 0  # El índice del estado actual en la lista de estados

    def avanzar_estado(self):
        if self.estado_actual < len(self.estados) - 1:
            self.estado_actual += 1
            print(f"El pedido {self.id_pedido} ha avanzado a: {self.estados[self.estado_actual]}")
        else:
            print(f"El pedido {self.id_pedido} ya se encuentra en el estado final: {self.estados[self.estado_actual]}")

    def obtener_estado_actual(self):
        return self.estados[self.estado_actual]

# Ejemplo de uso
pedido1 = Pedido(12345)

print(f"Estado inicial del pedido {pedido1.id_pedido}: {pedido1.obtener_estado_actual()}")
pedido1.avanzar_estado()
pedido1.avanzar_estado()
pedido1.avanzar_estado()
pedido1.avanzar_estado()
pedido1.avanzar_estado()  # Intento de avanzar más allá del estado final

print(f"Estado final del pedido {pedido1.id_pedido}: {pedido1.obtener_estado_actual()}")
