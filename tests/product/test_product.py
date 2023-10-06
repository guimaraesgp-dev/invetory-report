from inventory_report.product import Product


def test_create_product() -> None:
    # Instancia
    product = Product(
        id=6,
        company_name="Cantrell Drug Company",
        product_name="Silicea Belladonna",
        manufacturing_date="2021-07-18",
        expiration_date="2025-10-05",
        serial_number="FR57 7414 7254 046O IHVX AV6L H71",
        storage_instructions="instrucao 6",
    )
    # Verificação
    assert product.id == 6
    assert product.company_name == "Cantrell Drug Company"
    assert product.product_name == "Silicea Belladonna"
    assert product.manufacturing_date == "2021-07-18"
    assert product.expiration_date == "2025-10-05"
    assert product.serial_number == "FR57 7414 7254 046O IHVX AV6L H71"
    assert product.storage_instructions == "instrucao 6"
