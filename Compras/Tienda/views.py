from django.shortcuts import render
from django.views.generic import View, ListView



class ProductDetailView(View):
	def get(self,request,id,slug):
		product=get_object_or_404(product,id=id,slug=slug,avilable=True)
		template=''
#		cart_produc