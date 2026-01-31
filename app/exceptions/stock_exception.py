class InsufficientStockError(Exception):
    def __init__(self, message="Estoque insuficiente para esta operação"):
        self.message = message
        super().__init__(self.message)