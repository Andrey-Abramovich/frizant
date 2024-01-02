from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect

from nanostroi.models import Order


# Сигнал на создание заказа
@receiver(post_save, sender=Order)
def order_register(sender, instance, created, **kwargs):
    order = instance
    if created:
        send_mail('Что-то заказали',
                  f'{order.name} заказал {order}. Телефон {order.phone}.',
                  'andrey-abtest@yandex.ru',
                  ['andrey-abtest@yandex.ru'])
        return redirect('confirm')
