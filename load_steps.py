from behave import given
from service import db
from service.models import Product

@given("the following products")
def step_load_products(context):
    for row in context.table:
        product = Product(
            name=row["name"],
            category=row["category"],
            price=float(row["price"]),
            availability=row["availability"].lower() == "true",
        )
        db.session.add(product)
    db.session.commit()
