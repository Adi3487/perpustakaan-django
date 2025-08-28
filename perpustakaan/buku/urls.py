from django.urls import path
from . import views

urlpatterns = [
    path("", views.daftar_buku, name="daftar_buku"),
    path("peminjaman/", views.daftar_peminjaman,name= "daftar_peminjaman_user"),
    path('hapus-peminjaman/<int:pk>/', views.hapus_peminjaman, name='hapus_peminjaman'),
    path("buku/<int:buku_id>/", views.detail_buku, name= "detail_buku"),
    path("buku/<int:buku_id>/pinjam/", views.pinjam_buku, name="pinjam_buku"),#bagian ketiga ini berfungsi untuk membuat path ini dipanggil oleh template lain
    #jadi nanti template yang memanggil path ini memanggil nya  melalui bagian ketiga nya 
    #bagian tengah menghubungkan fungsi di views.py dengan path ini 
    
]