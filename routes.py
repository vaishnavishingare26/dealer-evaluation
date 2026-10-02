from flask import Blueprint, jsonify, request
from service import db
from service.models import Product

products_bp = Blueprint("products", __name__)

@products_bp.route("/products", methods=["POST"])
def create_product():
    data = request.get_json() or {}
    product = Product(
        name=data.get("name"),
        description=data.get("description"),
        category=data.get("category"),
        price=data.get("price", 0.0),
        availability=data.get("availability", True),
    )
    db.session.add(product)
    db.session.commit()
    return jsonify(product.serialize()), 201

@products_bp.route("/products/<int:product_id>", methods=["GET"])
def read_product(product_id):
    product = db.session.get(Product, product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product.serialize()), 200

@products_bp.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = db.session.get(Product, product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json() or {}
    for field in ["name", "description", "category", "price", "availability"]:
        if field in data:
            setattr(product, field, data[field])
    db.session.commit()
    return jsonify(product.serialize()), 200

@products_bp.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = db.session.get(Product, product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    db.session.delete(product)
    db.session.commit()
    return "", 204

@products_bp.route("/products", methods=["GET"])
def list_all_products():
    name = request.args.get("name")
    category = request.args.get("category")
    availability = request.args.get("availability")

    if name:
        products = Product.find_by_name(name)
    elif category:
        products = Product.find_by_category(category)
    elif availability is not None:
        value = availability.lower() in ("true", "1", "yes")
        products = Product.find_by_availability(value)
    else:
        products = Product.query.all()

    return jsonify([p.serialize() for p in products]), 200
