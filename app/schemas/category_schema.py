class CategorySchema:
    @staticmethod
    def validate_create(data):
        errors = {}
        if not data or not data.get('name'):
            errors['name'] = "O nome da categoria é obrigatório."
        return errors