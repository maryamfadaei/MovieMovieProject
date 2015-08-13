from django.conf.urls import patterns, url
from payment import views
urlpatterns = patterns('',
    url(r'^store/$', views.store, name='store'),#page of store
    url(r'^cart/$', views.cart, name='cart'),#page of cart
    url(r'^cart/checkout/$', views.checkout, name='checkout'),#the action of go to payment and create payment
    url(r'^cart/checkout/createpayment/(?P<payment_info_id>\d+)$', views.create_payment, name='create payment'),#the action of finish payment
)
