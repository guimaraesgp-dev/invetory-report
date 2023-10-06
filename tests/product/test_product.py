from inventory_report.product import Product


def test_create_product() -> None:
    # Instancia
    product = Product(
        id=1,
        company_name="Gabriel Guimaraes",
        product_name="Dev Jr",
        manufacturing_date="1996-07-24",
        expiration_date="2050-07-24",
        serial_number="22558844jk",
        storage_instructions="test create product",
    )
    # Verificação
    assert product.id == 1
    assert product.company_name == "Gabriel Guimaraes"
    assert product.product_name == "Dev Jr"
    assert product.manufacturing_date == "1996-07-24"
    assert product.expiration_date == "2050-07-24"
    assert product.serial_number == "22558844jk"
    assert product.storage_instructions == "test create product"
