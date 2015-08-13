from django.contrib import admin

# Register your models here.
from payment.models import stock, payment_info, shipping

class stockDetailAdmin(admin.ModelAdmin):# manage row display in admin
    list_display = ("item_id", "item_name", "quantity", "price", "provider_id")

class paymentDetailAdmin(admin.ModelAdmin):# manage row display in admin
    list_display = ("transaction_id", "user_id", "item_id", "transaction_date", "quantity", "total_price", "notes")

class shippingDetailAdmin(admin.ModelAdmin):# manage row display in admin
    list_display = ("transaction_id", "shipping_address")

admin.site.register(stock, stockDetailAdmin)#put the model and display into admin
admin.site.register(payment_info, paymentDetailAdmin)#put the model and display into admin
admin.site.register(shipping, shippingDetailAdmin)#put the model and display into admin
