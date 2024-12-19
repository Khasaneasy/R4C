from django.core.mail import send_mail
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from orders.models import Order
from robots.models import Robot


@receiver(post_save, sender=Robot)
def robot_in_stock_notify(sender, instance, created, **kwargs):
    if instance.is_in_stock:
        orders = Order.objects.filter(robot=instance, status_order=False)
        for order in orders:
            custom_email = order.customer.email
            send_mail(
                f'Добрый день!\n\nНедавно вы интересовались нашим роботом модели {instance.model}, версии {instance.version}.'
                f'Этот робот теперь в наличии.'
                f'Если вам подходит этот вариант, пожалуйста, свяжитесь с нами.',
                settings.DEFAULT_FROM_EMAIL,
                [custom_email],
                fail_silently=False,
            )
            order.status_order = True
            order.save
