from inventory_report.product import Product


def test_product_report() -> None:
    # Instancia
    product = Product(
        id="6",
        company_name="Cantrell Drug Company",
        product_name="Silicea Belladonna",
        manufacturing_date="2021-07-18",
        expiration_date="2025-10-05",
        serial_number="FR57 7414 7254 046O IHVX AV6L H71",
        storage_instructions="instrucao 6",
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
