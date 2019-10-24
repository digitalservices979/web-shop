from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from portada.models import Portada
from django.dispatch import receiver
from django.shortcuts import render, HttpResponse

@receiver(valid_ipn_received, sender=ST_PP_COMPLETED)
def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        
        if ipn_obj.receiver_email != "qwer_jv16@outlook.com":
            return False

        if ipn_obj.item_number != 0:
        	n_objeto = Portada.objects.get(pk=ipn_obj.custom)
        	st = n_objeto.stock
        	a = st-1
            Portada.objects.get(pk=ipn_obj.custom).update(stock=a)
 	else:
 		n_objeto = Portada.objects.get(pk=ipn_obj.custom)
        st = n_objeto.stock
        a = st+1
        Portada.objects.get(pk=ipn_obj.custom).update(stock=a)
