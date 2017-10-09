import paypalrestsdk
import logging

paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "Aei_eyReR0PM8caNOXAQb652HWiLrFSHkzvkkScdd2jhPcRQhlWtwpCbmrYoD099PRR..........",
  "client_secret": "EPd7-vTl7rFqZWf2oS7X8xAVHlU14HziCGZLRY6-ujVUc_gfJ8dXDmDXb5jD9gdiAz67AApz3REr......" })

payment = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {
        "payment_method": "paypal"},
    "redirect_urls": {
        "return_url": "http://localhost:3000/payment/execute",
        "cancel_url": "http://localhost:3000/"},
    "transactions": [{
        "item_list": {
            "items": [{
                "name": "item",
                "sku": "item",
                "price": "1.00",
                "currency": "USD",
                "quantity": 1}]},
        "amount": {
            "total": "1.00",
            "currency": "USD"},
        "description": "Esta es una transaccion de pago de ejemplo."}]})

if payment.create():
  print("Pago creado con exito")
else:
  print(payment.error)
