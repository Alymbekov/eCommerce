from django.shortcuts import render, redirect
from django.urls import reverse

from apps.cart.cart import Cart
from apps.orders.forms import OrderCreateForm
from apps.orders.models import OrderItem


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save()
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])
                # очистка корзины
                cart.clear()
                # запуск ассинхронной операции
                order_created.delay(order.id)
                # установить заказ в сессии
                request.session['order_id'] = order.id
                # перенаправить на оплату
                return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
    return render(request, 'order_create.html', {'cart': cart,
                                                        'form': form})