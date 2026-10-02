from service import db
from service.models import Product
from tests.factories import make_product

def add_product():
    product = make_product()
    db.session.add(product)
    db.session.commit()
    return product

def test_read(client, app):
    product = add_product()
    response = client.get(f"/products/{product.id}")
    assert response.status_code == 200
    assert response.get_json()["name"] == "Test Laptop"

def test_update(client, app):
    product = add_product()
    response = client.put(f"/products/{product.id}", json={"name": "Updated"})
    assert response.status_code == 200
    assert response.get_json()["name"] == "Updated"

def test_delete(client, app):
    product = add_product()
    response = client.delete(f"/products/{product.id}")
    assert response.status_code == 204

def test_list_all(client, app):
    add_product()
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.get_json()) == 1

def test_list_by_name(client, app):
    add_product()
    response = client.get("/products?name=Laptop")
    assert response.status_code == 200
    assert len(response.get_json()) == 1

def test_list_by_category(client, app):
    add_product()
    response = client.get("/products?category=Electronics")
    assert response.status_code == 200
    assert len(response.get_json()) == 1

def test_list_by_availability(client, app):
    add_product()
    response = client.get("/products?availability=true")
    assert response.status_code == 200
    assert len(response.get_json()) == 1
