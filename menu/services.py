from rest_framework.exceptions import ValidationError   



def payment(order):
    # cek apakah udah pernah bayar
    if order.status == 'PAID':
        raise ValidationError(f"Bos!, order dengan id {order.id} sudah dibayar!")
    
    order.status = 'PAID'
    order.save()
    
    return order
    