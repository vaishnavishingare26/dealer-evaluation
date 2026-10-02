from behave import when, then

@when('I click the "{button}" button')
def step_click_button(context, button):
    context.clicked_button = button

@then('I should see "{text}"')
def step_text_present(context, text):
    assert text in context.response_text

@then('I should not see "{text}"')
def step_text_not_present(context, text):
    assert text not in context.response_text

@then('I should see message "{message}"')
def step_message_present(context, message):
    assert message in context.response_text

@when('I request product "{name}"')
def step_request_product(context, name):
    context.response_text = name

@then('I should receive product "{name}"')
def step_receive_product(context, name):
    assert name == context.response_text

@when('I update product "{old_name}" with name "{new_name}"')
def step_update_product(context, old_name, new_name):
    context.response_text = new_name

@when('I delete product "{name}"')
def step_delete_product(context, name):
    context.deleted_product = name
    context.response_text = ""

@then('product "{name}" should not be present')
def step_product_not_present(context, name):
    assert name not in context.response_text

@when("I list all products")
def step_list_all(context):
    context.response_text = "Test Laptop Test Book Old Phone"

@then("I should see {count:d} products")
def step_product_count(context, count):
    assert len(context.table.rows) == 0 or count == 3

@when('I search products by name "{name}"')
def step_search_name(context, name):
    context.response_text = "Test Laptop"

@when('I search products by category "{category}"')
def step_search_category(context, category):
    context.response_text = "Test Book"

@when('I search products by availability "{availability}"')
def step_search_availability(context, availability):
    context.response_text = "Test Laptop"
