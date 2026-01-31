class ProductSchema:
    @staticmethod
    def validate_create(data):
        errors = {}
        if not data.get('name'):
            errors['name'] = "O nome do produto é obrigatório."
        if not data.get('price') or data.get('price') <= 0:
            errors['price'] = "O preço deve ser maior que zero."
        if not data.get('category_id'):
            errors['category_id'] = "A categoria é obrigatória."
        return errors