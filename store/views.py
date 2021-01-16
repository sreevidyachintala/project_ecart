from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.http import HttpResponse


from store.forms import Usreg,Upfle
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder
from store.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def about(request):
	return render(request,'store/about.html')
def contact(request):
	return render(request,'store/contact.html')


def addproduct(request):
	if request.method=="POST":
		print("hi")
		form=AddProductForm(request.POST,request.FILES)
		if form.is_valid():
			print("hi1")
			form.save()
			print("hai2")
			return HttpResponse("data added successfully")
	form=AddProductForm()

	
	
	return render(request,'store/addproduct.html',{'form':form})
	

def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)


def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)

@login_required
def profile(request):
	return render(request,'store/profile.html')


@login_required
def dashboard(request):
	return render(request,'store/dsh.html')
@login_required
def upfle(request):
	if request.method=="POST":
		t=Upfle(request.POST,instance=request.user)
		if t.is_valid():
			t.save()
			messages.success(request,"successfully updated")
			return redirect('/profile')
	t=Upfle(instance=request.user)
	return render(request,'store/update.html',{'y':t})

def signup(request):
	if request.method=='POST':
		form =Usreg(request.POST)
		if form.is_valid():
			form.save()
			#return HttpResponse('<script>alert("user data inserted successfully")</script>')
			messages.success(request,"successfully registered please login")
			return redirect('/log')			
	form = Usreg()
	return render(request,'store/signup.html',{'form':form})

