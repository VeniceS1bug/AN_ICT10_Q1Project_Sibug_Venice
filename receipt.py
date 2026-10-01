from pyscript import document


def create_order(event):
    # Get the customer name
    customer_name = document.querySelector("#customer_name").value

    # Prices
    fondente_price = 480
    latte_price = 450
    bianco_price = 450
    caramel_price = 520
    pistacchio_price = 550

    order_list = ""
    total = 0

    # Get quantities
    fondente_qty = int(document.querySelector("#item1").value or 0)
    latte_qty = int(document.querySelector("#item2").value or 0)
    bianco_qty = int(document.querySelector("#item3").value or 0)
    caramel_qty = int(document.querySelector("#item4").value or 0)
    pistacchio_qty = int(document.querySelector("#item5").value or 0)

    #Calculate total
    if fondente_qty > 0:
        subtotal = fondente_price * fondente_qty
        order_list += f"Cioccolato Fondente x {fondente_qty} - ₱{subtotal}<br>"
        total += subtotal

    if latte_qty > 0:
        subtotal = latte_price * latte_qty
        order_list += f"Cioccolato al Latte x {latte_qty} - ₱{subtotal}<br>"
        total += subtotal

    if bianco_qty > 0:
        subtotal = bianco_price * bianco_qty
        order_list += f"Cioccolato Bianco x {bianco_qty} - ₱{subtotal}<br>"
        total += subtotal

    if caramel_qty > 0:
        subtotal = caramel_price * caramel_qty
        order_list += f"Caramello Salato x {caramel_qty} - ₱{subtotal}<br>"
        total += subtotal

    if pistacchio_qty > 0:
        subtotal = pistacchio_price * pistacchio_qty
        order_list += f"Pistacchio x {pistacchio_qty} - ₱{subtotal}<br>"
        total += subtotal

    # Check name
    if customer_name == "":
        document.querySelector("#result").innerHTML = "Please enter your name."
        return

    # Check order
    if order_list == "":
        document.querySelector("#result").innerHTML = (
            "Please order at least one item."
        )
        return

    # Display receipt
    document.querySelector("#result").innerHTML = f"""
    <strong>Customer:</strong> {customer_name}<br><br>
    <strong>Order Details:</strong><br>
    {order_list}
    <hr>
    <strong>Total: ₱{total}</strong>
    """