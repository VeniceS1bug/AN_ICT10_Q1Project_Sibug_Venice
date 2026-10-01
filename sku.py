from pyscript import document


def generate_sku(event):
    # Get user input
    category = document.querySelector("#category").value
    product = document.querySelector("#product").value
    stock = document.querySelector("#stock").value

    # Check fields
    if product == "" or stock == "":
        document.querySelector("#sku").innerHTML = "Please fill in all fields."
        return

    # Get first 3 letters in uppercase
    product_code = product[:3].upper()

    # Format stock number to 3 digits (e.g., 25 becomes 025)
    stock_code = str(stock).zfill(3)

    # Create SKU
    sku_code = f"{category}-{product_code}-{stock_code}"

    # Show output
    document.querySelector("#sku").innerHTML = f"""
    Category: {category}<br>
    Product: {product}<br>
    Stock Quantity: {stock}<br><br>
    <strong>Generated SKU: {sku_code}</strong>
    """