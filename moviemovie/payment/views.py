from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
import json
from payment.models import payment_info, payment_info_form, stock, stock_form, shipping, shipping_form, payment_detailForm
import paypalrestsdk
from moviemovie.settings import PAYPAL_MODE, PAYPAL_CLIENT_ID, PAYPAL_CLIENT_SECRET
#made by Licheng Yu
def store(request):#load the page of store
    return render(request, 'payment/store.html')

def cart(request):#load the page of cart
    return render(request, 'payment/cart.html')

def checkout(request):#process the checkout
    check_valid=0
    unit_price=0
    if request.method == 'POST':
        form=payment_info_form(request.POST)#create data to database
        if form.is_valid():
            user_id = form.cleaned_data['user_id']# the [] is the name of field in html file
            item_id = form.cleaned_data['item_id']
            quantity = form.cleaned_data['quantity']
            notes = form.cleaned_data['notes']
            stock_detail = stock.objects.all().order_by('item_id')
            for i in stock_detail:#check the quantity of our stock
                if (i.item_id == item_id):
                    item = i
                    unit_price = i.price
                    check_valid=1
                    break
            total_price = unit_price * quantity
            if check_valid == 0:
                return cart(request)
            if (item.quantity < quantity):
                messages.error(request, 'Quantity you require exceed our stock. Please reduce the quantity. Thanks.')
                return cart(request)
            else:
                item.quantity = item.quantity-quantity#reduce the quantity of item stock
                item.save()
                form.save()#have to save, the data will be update
            payment_detail = payment_info.objects.all().order_by('id')
            for j in payment_detail:#record the payment_info_id
                if (j.user_id == user_id):
                    payment_info_id = j.id
                    payment_detail = get_object_or_404(payment_info, pk=payment_info_id)
    payment_detail.total_price=total_price
    payment_detail.save()
    return render(request, 'payment/payment.html', {'payment_detail': payment_detail})

def create_payment(request, payment_info_id):#the page of processing payment
    payment_detail = get_object_or_404(payment_info, pk=payment_info_id)
    api=paypalrestsdk.configure({
        "mode": PAYPAL_MODE,
        "client_id": PAYPAL_CLIENT_ID,
        "client_secret": PAYPAL_CLIENT_SECRET })
    if request.method == 'POST':
        form = payment_detailForm(request.POST)
        if form.is_valid():
            payment = paypalrestsdk.Payment({#use paypaly to process payment
                "intent": "sale",
                "payer": {
                    "payment_method": "credit_card",
                    "funding_instruments": [{
                        "credit_card": {
                            "type": form.cleaned_data['cardtype'],
                            "number": form.cleaned_data['cardnumber'],
                            "expire_month": form.cleaned_data['expire_month'],
                            "expire_year": form.cleaned_data['expire_year'],
                            "cvv2": form.cleaned_data['cvv2'],
                            "first_name": form.cleaned_data['first_name'],
                            "last_name": form.cleaned_data['last_name']}}]},
                "transactions": [{
                    "amount": {
                    "total": payment_detail.total_price,
                    "currency": "CAD"}}]})
            if payment.create():#payment success will make website to record shipping info
                firstname = form.cleaned_data['firstname']
                lastname = form.cleaned_data['lastname']
		address1 = form.cleaned_data['address1']
		address2 = form.cleaned_data['address2']
		city = form.cleaned_data['city']
		state = form.cleaned_data['state']
		zipcode = form.cleaned_data['zipcode']
		country = form.cleaned_data['country']
		phone = form.cleaned_data['phone']
                contactemail = form.cleaned_data['contactEmail']
    		#full_name is used to save in shipping table
		full_name = firstname+" "+lastname
                #final_address is used to save in shipping table
                final_address = address1+" "+address2+" "+city+" "+state+" "+zipcode+" "+country
		payment_detail.notes = form.cleaned_data['notes']#update payment detail info to payment_info table
		payment_detail.transaction_id = payment.id#save transaction id
		payment_detail.save()
		#save shipping info to shipping table include transaction id and address
		shipping_info = shipping(transaction_id = payment.id, shipping_address = final_address)
		shipping_info.save()
                return render(request, 'payment/index.html')
            else:#go back to payment page
                messages.error(request, 'We are sorry but something went wrong. We could not process your payment.')
                return render(request, 'payment/payment.html', {'payment_detail': payment_detail})
        else:
            return HttpResponse(form.errors)
    return -1
