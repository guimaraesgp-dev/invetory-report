from inventory_report.product import Product


def test_product_report() -> None:
    # Instancia
    product = Product(
        id="1",
        company_name="Gabriel Guimaraes",
        product_name="Dev Jr",
        manufacturing_date="1996-07-24",
        expiration_date="2050-07-24",
        serial_number="22558844jk",
        storage_instructions="test create product",
    )

    expected_report = (
        f"The product {product.id} - {product.product_name}"
        f" with serial number {product.serial_number}"
        f" manufactured on {product.manufacturing_date}"
        f" by the company {product.company_name}"
        f" valid until {product.expiration_date}"
        f" must be stored according to the following instructions: "
        f"{product.storage_instructions}."
    )

    assert str(product) == expected_report
