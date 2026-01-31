import unittest
from app.services.product_service import ProductService
from app.exceptions.stock_exception import InsufficientStockError
from run import app

class TestBusinessRules(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()

    def test_insufficient_stock_validation(self):
        
        product_id = "seu-uuid-de-teste-aqui" 
        
        with self.assertRaises(InsufficientStockError):
        
            ProductService.update_stock(
                product_id=product_id, 
                quantity=15, 
                movement_type='OUT', 
                reason="Teste de falha"
            )

if __name__ == '__main__':
    unittest.main()