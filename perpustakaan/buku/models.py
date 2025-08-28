from django.db import models
from django.contrib.auth.models import User

class Buku(models.Model):
    judul= models.CharField(max_length= 200)
    penulis = models.CharField(max_length= 100)
    stok= models.PositiveIntegerField(default=0)
    deskripsi = models.TextField()
    
    def __str__(self):
        return self.judul
    
class Peminjaman(models.Model):
    user =models.ForeignKey(User, on_delete= models.CASCADE)
    buku = models.ForeignKey(Buku, on_delete= models.CASCADE)
    tanggal_pinjam = models.DateTimeField(auto_now_add= True)
    tanggal_kembali = models.DateTimeField(null=True, blank=True)
    sudah_dikembalikan = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username} - {self.buku.judul}"

# Create your models here.
