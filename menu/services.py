from rest_framework.exceptions import ValidationError   
from .tasks import generate_invoice_pdf


def payment(order):
    # cek apakah udah pernah bayar
    if order.status == 'PAID':
        raise ValidationError(f"Bos!, order dengan id {order.id} sudah dibayar!")
    
    order.status = 'PAID'   
    order.save()
    
    # panggil si celery
    generate_invoice_pdf.delay(order.id)
    
    return order
    