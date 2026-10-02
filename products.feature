Feature: Product management
  As a product service user
  I want to manage products
  So that I can maintain the product catalog

  Background:
    Given the following products
      | name          | category    | price  | availability |
      | Test Laptop   | Electronics | 999.99 | true         |
      | Test Book     | Books       | 25.50  | true         |
      | Old Phone     | Electronics | 150.00 | false        |

  Scenario: Read a product
    When I request product "Test Laptop"
    Then I should receive product "Test Laptop"

  Scenario: Update a product
    When I update product "Test Laptop" with name "Updated Laptop"
    Then I should receive product "Updated Laptop"

  Scenario: Delete a product
    When I delete product "Old Phone"
    Then product "Old Phone" should not be present

  Scenario: List all products
    When I list all products
    Then I should see 3 products

  Scenario: Search by Name
    When I search products by name "Laptop"
    Then I should see product "Test Laptop"

  Scenario: Search by Category
    When I search products by category "Books"
    Then I should see product "Test Book"

  Scenario: Search by Availability
    When I search products by availability "true"
    Then I should see product "Test Laptop"
