import os
from celery import Celery

# ngasih tau Celery dimana letak settingan Django kita
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# bikin robot pekerja (nama aplikasinya bebas)
app = Celery('core')

# nyuruh Celery baca settingan yang ada awalan 'CELERY_' di settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# nyuruh Celery nyari otomatis file task.py di semua folder aplikasi
app.autodiscover_tasks()