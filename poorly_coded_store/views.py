from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    product = Product.objects.get(id=request.POST["product_id"])
    price_from_form = product.price
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    new_order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect(f'display_checkout/{new_order.id}')

def display_checkout(request, id):
    new_order = Order.objects.get(id=id)
    all_orders = Order.objects.all()
    total_items = 0
    grand_total = 0
    for order in all_orders: 
        total_items += order.quantity_ordered
        grand_total += order.total_price
    context = {
        "new_order": new_order,
        "grand_total": grand_total,
        "total_items": total_items
    }
    return render(request, "store/checkout.html", context)
