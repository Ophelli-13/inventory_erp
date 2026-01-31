class StockMovementSchema:
    @staticmethod
    def validate_movement(data):
        errors = {}
        if data.get('type') not in ['IN', 'OUT']:
            errors['type'] = "O tipo deve ser 'IN' (Entrada) ou 'OUT' (Saída)."
        if not data.get('quantity') or data.get('quantity') <= 0:
            errors['quantity'] = "A quantidade deve ser maior que zero."
        return errors