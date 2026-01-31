class InsufficientStockError(Exception):
    def __init__(self, message="Estoque insuficiente para completar a operação."):
        self.message = message
        super().__init__(self.message)