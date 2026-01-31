class SupplierSchema:
    @staticmethod
    def validate_create(data):
        errors = {}
        if not data or not data.get('name'):
            errors['name'] = "O nome do fornecedor é obrigatório."
        if not data.get('contact_email'):
            errors['contact_email'] = "O e-mail de contato é obrigatório."
        return errors