import Sinif
import Menu

# Sınıf ve Menüyü oluştur
sinif = Sinif.Sinif()
menu = Menu.Menu(sinif)

# 50 Kişilik bir sınıf dosyası oluştur
# Halihazırda var olan sınıf dosyası kullanılmak isteniyorsa alttaki satır yoruma alınabilir
sinif.rastgeleSinifDosyasiOlustur("Sinif.csv",50)

while(True):
    # Menüyü başlat
    menu.kullaniciGirisi()
    