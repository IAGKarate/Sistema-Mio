from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.CartDetail.as_view(),name="cart_detail"),
	url(r'^add/(?P<product_id>\d+)/$',views.CardAdd.as_view(),name="Add"),
	url(r'^remove/(?P<product_id>\d+)/$',views.CartRemove.as_view(),name="car_remove"),
]