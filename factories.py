from service.models import Product

def make_product(**kwargs):
    data = {
        "name": "Test Laptop",
        "description": "A product created for testing",
        "category": "Electronics",
        "price": 999.99,
        "availability": True,
    }
    data.update(kwargs)
    return Product(**data)

def make_products(count=5):
    return [make_product(name=f"Test Product {i}") for i in range(count)]
