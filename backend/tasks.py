import time

from celery import shared_task

@shared_task
def laporkan_pusat(pk):
    time.sleep(10)
    laporan = Laporan.objects.get(pk=pk)
    laporan.lapor_pusat = True
    laporan.save()

    return 'masuk sini'
