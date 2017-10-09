import paypalrestsdk
import logging

paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "<<ID de cliente>>..........",
  "client_secret": "<<Secreto de ID>>......" })

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
