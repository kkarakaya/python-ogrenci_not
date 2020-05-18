import sys         # Programdan çıkış yapmak için


class Menu(object):
    def __init__(self,sinif):
        # yapıcı fonksiyon
        # verilen sınıf parametresini alır
        self.sinif = sinif
        
    def kullaniciGirisi(self):
        """Değer giris fonksiyonu"""
        self.menuYaz()
        deger = input("İşlem seçiniz: ")
        islemAdi = 'islem_' + str(deger)
        # self 'in fonksiyonuna eriş.
        islem = getattr(self, islemAdi, lambda: "gecersiz")
        # Fonksiyonu dönerken aynı zamanda çağır
        return islem()
    
    def menuYaz(self):
        print("\n ############### MENU ###############")
        print("1- Dosyadan Oku")
        print("2- Yeni Kayıt Ekle")
        print("3- Kayıt Güncelle")
        print("4- Kayıt Sil")
        print("5- Kayıtları Listele")
        print("6- Sınıf Başarı Notlarını Hesapla")
        print("7- Kayıtları Başarı Notuna Göre Sırala")
        print("8- İstatistiki Bilgiler")
        print("9- Dosyaya Yaz")
        print("10- Çıkış")   
    
    def islem_1(self):
        # Dosyadan Oku
        self.sinif.sinifDosyasindanOku('Sinif.csv')
        
    def islem_2(self):
        # Sınıfa kayıt ekle
        ogrenciNo = input("\nSınıfa eklenecek kişinin Öğrenci Numarası: ")
        ad = input("Adı: ")
        soyad = input("Soyadı: ")
        vize1 = input("1. Vize notu: ")
        vize2 = input("2. Vize notu: ")
        final = input("Final notu: ")
        self.sinif.ekle(int(ogrenciNo), {"Ad":ad, "Soyad":soyad, "Vize 1":int(vize1),
                        "Vize 2":int(vize2), "Final":int(final)})      
 
    def islem_3(self):
        # Sınıfa kaydı güncelle
        ogrenciNo = input("\nGüncellenecek kişinin Öğrenci Numarası: ")
        vize1 = input("1. Vize notu: ")
        vize2 = input("2. Vize notu: ")
        final = input("Final notu: ")
        self.sinif.guncelle(int(ogrenciNo), {"Vize 1":int(vize1),
                        "Vize 2":int(vize2), "Final":int(final)})       
        
    def islem_4(self):
       # Sınıftan kayıt sil
       ogrenciNo = input("\nKaydı silinecek kişinin Öğrenci Numarası: ")
       self.sinif.sil(int(ogrenciNo))
 
    def islem_5(self):
        # Kayıtları listele
        # Sınıfa kayıtlı kişilerin öğrenci no'ları adları ve soyadları listelenir
        self.sinif.sinifKaydiListele()
 
    def islem_6(self):
        # Sınıf Başarı Notlarını Hesapla
        self.sinif.sinifBaşariNotlariniHesapla()
        
    def islem_7(self):
        # Kayıtları başarı notlarına göre sırala
        self.sinif.notOrtalamasinaGoreSirala()
        self.sinif.sinifBaşariNotlariniHesapla()
 
    def islem_8(self):
        # İstatistiki Bilgiler
        self.sinif.istatistikiBilgileriYaz()
        
    def islem_9(self):
        # Dosyaya Yaz
        self.sinif.sinifDosyasinaYaz("Output.csv") 
        
    def islem_10(self):
        sys.exit("\nProgram sonlandırıldı.")