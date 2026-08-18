from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Product, Cart, CartItem, Order, OrderItem
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db import transaction


def home(request):
    return render(request, 'products/home.html')


def product_list(request):
    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    return render(request, 'products/product_list.html', {
        'products': products
    })


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    return render(request, 'products/product_detail.html', {
        'product': product
    })


def cart(request):
    cart_id = request.session.get('cart_id')

    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id

    total = sum(
        item.product.price * item.quantity
        for item in cart.items.all()
    )

    return render(request, 'products/cart.html', {
        'cart': cart,
        'total': total
    })


def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    cart_id = request.session.get('cart_id')

    if cart_id:
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created and cart_item.quantity < product.stock:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


def increase_quantity(request, id):
    cart_item = get_object_or_404(CartItem, id=id)

    if cart_item.quantity < cart_item.product.stock:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


def decrease_quantity(request, id):
    cart_item = get_object_or_404(CartItem, id=id)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()

    return redirect('cart')


def remove_from_cart(request, id):
    cart_item = get_object_or_404(CartItem, id=id)
    cart_item.delete()

    return redirect('cart')


@login_required
def checkout(request):
    cart_id = request.session.get('cart_id')

    if not cart_id:
        return redirect('cart')

    cart = get_object_or_404(Cart, id=cart_id)

    if not cart.items.exists():
        return redirect('cart')

    total = sum(
        item.product.price * item.quantity
        for item in cart.items.all()
    )

    return render(
        request,
        'products/checkout.html',
        {
            'cart': cart,
            'total': total,
            'shipping': request.session.get('shipping', {})
        }
    )


@login_required
@require_POST
def demo_payment(request):

    cart_id = request.session.get('cart_id')

    if not cart_id:
        return JsonResponse({
            'error': 'Cart is empty'
        }, status=400)

    cart = get_object_or_404(Cart, id=cart_id)

    if not cart.items.exists():
        return JsonResponse({
            'error': 'Cart is empty'
        }, status=400)

    # Check stock before creating the order
    for item in cart.items.all():

        if item.quantity > item.product.stock:
            return JsonResponse({
                'error': f'Not enough stock for {item.product.name}.'
            }, status=400)

    total = sum(
        item.product.price * item.quantity
        for item in cart.items.all()
    )

    try:

        with transaction.atomic():

            # Save shipping information
            request.session['shipping'] = {
                'name': request.POST.get('name'),
                'email': request.POST.get('email'),
                'phone': request.POST.get('phone'),
                'address': request.POST.get('address'),
                'city': request.POST.get('city'),
                'state': request.POST.get('state'),
                'pincode': request.POST.get('pincode'),
            }

            # Create order
            order = Order.objects.create(
                user=request.user,
                name=request.POST.get('name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                address=request.POST.get('address'),
                city=request.POST.get('city'),
                state=request.POST.get('state'),
                pincode=request.POST.get('pincode'),
                total_price=total,
                payment_status='paid'
            )

            # Create order items and reduce stock
            for item in cart.items.all():

                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )

                item.product.stock -= item.quantity
                item.product.save()

            # Empty cart
            cart.items.all().delete()
            del request.session['cart_id']

        return redirect('order_confirmation', order.id)

    except Exception as e:

        return JsonResponse({
            'error': 'Something went wrong while creating the order.'
        }, status=500)


@login_required
def order_confirmation(request, id):
    order = get_object_or_404(
        Order,
        id=id,
        user=request.user
    )

    return render(request, 'products/order_confirmation.html', {
        'order': order
    })


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)

        return redirect('home')

    return render(request, 'products/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'products/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def my_orders(request):
    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request, 'products/my_orders.html', {
        'orders': orders
    })


@login_required
def order_detail(request, id):
    order = get_object_or_404(
        Order,
        id=id,
        user=request.user
    )

    return render(request, 'products/order_detail.html', {
        'order': order
    })