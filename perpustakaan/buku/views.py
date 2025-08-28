from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from .models import Buku, Peminjaman
from django.contrib import messages
from django.utils import timezone



def daftar_buku(request):
    buku_list= Buku.objects.all()
    return render(request, "buku/daftar_buku.html", {"buku_list": buku_list})

def detail_buku(request, buku_id):
    buku = get_object_or_404(Buku, id=buku_id)
    return render(request, "buku/detail_buku.html", {"buku": buku})

@login_required
def pinjam_buku(request, buku_id):
    buku = get_object_or_404(Buku, id=buku_id)
    sudah_pinjam = Peminjaman.objects.filter(
        user=request.user,
        buku=buku,
        tanggal_kembali__isnull=True
    ).exists()

    if request.method == "POST":
        if sudah_pinjam:
            messages.error(request, "Kamu sudah meminjam buku ini dan belum mengembalikannya.")
            return redirect("daftar_buku")

        if buku.stok > 0:
            buku.stok -= 1
            buku.save()
            Peminjaman.objects.create(user=request.user, buku=buku)
            messages.success(request, "Berhasil Meminjam Buku!")
            return redirect("daftar_buku")
        else:
            return render(request, "buku/pinjam_buku.html", {
                "buku": buku,
                "error": "Stok habis"
            })

    # Jika GET dan user sudah pinjam, beri warning (tapi tidak redirect, biar pesan muncul di halaman buku)
    if sudah_pinjam:
        messages.warning(request, "Kamu sudah meminjam buku ini dan belum mengembalikannya.")

    return render(request, "buku/pinjam_buku.html", {"buku": buku})
    # buku = get_object_or_404(Buku, id= buku_id)
    # sudah_pinjam = Peminjaman.objects.filter(user=request.user, buku=buku, tanggal_kembali__isnull=True, ).exists()
    # if request.method == "GET":
    #     if sudah_pinjam :
    #         messages.error(request, "Kamu sudah meminjam buku ini dan belum mengembalikannya.")
    #         return redirect("daftar_buku")

    # if request.method == "POST":
    #     if buku.stok > 0:
    #         buku.stok -= 1
    #         buku.save()
    #         peminjaman = Peminjaman(user= request.user, buku=buku)
    #         peminjaman.save()
    #         return redirect("daftar_buku")
        
    #     return render(request , "buku/pinjam_buku.html", {"buku": buku, "error":"Stok habis"})

@login_required
def daftar_peminjaman(request):
    peminjaman_list = Peminjaman.objects.filter(user=request.user).select_related("buku")
    return render(request, "buku/daftar_peminjam.html",{"peminjaman_list": peminjaman_list})

@login_required
def hapus_peminjaman(request, pk):
    peminjaman = get_object_or_404(Peminjaman, pk=pk)
    if request.method == 'POST':
        if not peminjaman.sudah_dikembalikan:
            peminjaman.buku.stok += 1
            peminjaman.buku.save()
        peminjaman.delete()
        return redirect('daftar_peminjaman_user')  
    
    return redirect('daftar_peminjaman_user')

# @login_required
# def hapus_peminjaman(request, pk):
#     peminjaman = get_object_or_404(Peminjaman, pk=pk, user=request.user)
#     if not peminjaman.sudah_dikembalikan:
#         # Kembalikan stok buku sebelum dihapus
#         peminjaman.buku.stok += 1
#         peminjaman.buku.save()

#     peminjaman.delete()
#     return redirect('daftar_peminjaman_user')



# Create your views here.
