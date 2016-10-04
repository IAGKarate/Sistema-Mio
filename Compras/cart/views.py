from django.shortcuts import render, redirect, get_object_or_404
from Tienda.models import Producto
from .cart import Cart
from .forms import CartAddProductForm
from django.views.generic import View


class CardAdd(View):
	def post(self, request, product_id):
		cart=Cart(requiest)
		product=get_object_or_404(Producto,id=producto_id)
		form=CartAddProductForm(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			cart.add(product=product,quantity=cd['quantity'],
				update_quantity=cd['update'])
		return redirect('cart:cart_detail')

class CartRemove(View):
	def get(self,request,product_id):
		cart=Cart(requeste)
		product=get_object_or_404(product,id=product_id)
		cart.remove(product)
		return redirect('cart:car_detaild')

class CartDetail(View):
	def get(self,request):
		car=Car(request)
		template="car/detail.html"
		for item in car:
			item['update_quantity_form']=CartAddProductForm(initial={'quantity':item['quantity'],'update':True})
		contex={
		'cart':cart
		}
		return render (request,template,contex)