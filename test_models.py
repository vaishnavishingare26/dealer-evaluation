from service import db
from service.models import Product
from tests.factories import make_product

def test_read(app):
    product = make_product()
    db.session.add(product)
    db.session.commit()
    found = db.session.get(Product, product.id)
    assert found.name == "Test Laptop"

def test_update(app):
    product = make_product()
    db.session.add(product)
    db.session.commit()
    product.name = "Updated Laptop"
    db.session.commit()
    assert db.session.get(Product, product.id).name == "Updated Laptop"

def test_delete(app):
    product = make_product()
    db.session.add(product)
    db.session.commit()
    product_id = product.id
    db.session.delete(product)
    db.session.commit()
    assert db.session.get(Product, product_id) is None

def test_list_all(app):
    db.session.add_all([make_product(name="A"), make_product(name="B")])
    db.session.commit()
    assert Product.query.count() == 2

def test_find_by_name(app):
    db.session.add_all([make_product(name="Apple Phone"), make_product(name="Dell Laptop")])
    db.session.commit()
    result = Product.find_by_name("Apple")
    assert len(result) == 1
    assert result[0].name == "Apple Phone"

def test_find_by_category(app):
    db.session.add_all([make_product(category="Books"), make_product(category="Electronics")])
    db.session.commit()
    result = Product.find_by_category("Books")
    assert len(result) == 1

def test_find_by_availability(app):
    db.session.add_all([make_product(availability=True), make_product(availability=False)])
    db.session.commit()
    result = Product.find_by_availability(True)
    assert len(result) == 1
    assert result[0].availability is True
