import time

from celery import shared_task

@shared_task
def laporkan_pusat(instance):
    time.sleep(10000)
    instance.lapor_pusat = True
    instance.save()

    return None
