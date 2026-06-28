from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Satpam khusus: Cuma ngasih izin kalau user udah login DAN role-nya 'ADM'
    """
    def has_permission(self, request, view): #type:ignore
        return bool(
            request.user and 
            request.user.is_authenticated and 
            request.user.role == 'ADM'
        )

# TUGAS LU: Lanjutin di bawah sini buat IsKasir dan IsCustomer!
class IsKasir(BasePermission):
    """
        satpam khusus: cuma ngasih izin kalo user udah login dan role-nya 'KSR'
    """
    
    def has_permission(self, request, view): #type:ignore
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.role == 'KSR'
            
        )
        
class IsCustomer(BasePermission):
    """
        satpam khusus: cuma ngasih izin kalo user udah login dan role-nya 'KST'
    """
    
    def has_permission(self, request, view): #type:ignore
        return bool(
            request.user and
            request.user.is_authenticated and
            request.user.role == 'KST'
            
        )