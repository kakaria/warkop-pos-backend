import time
from celery import shared_task

# mantra @shared_task, ngasih tau kalo fungsi ini tugas buat si robot Celery bukan Django
@shared_task
def generate_invoice_pdf(order_id):
    print(f"[{order_id}] 🖨️ Memulai proses cetak PDF...")
    
    # simulasi proses berat (generate PDF, kirim email, dll) selama 5 detik
    time.sleep(5)
    
    print(f"[{order_id}] ✅ Selesai! Struk berhasil dicetak di printer kasir!")
    return f"Invoice {order_id} Done"