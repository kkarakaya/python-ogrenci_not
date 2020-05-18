import Ogrenci
import scipy.stats  # İstatistiksel işlemler ve Çan eğrisi dağılımını çizdirmek için
import random       # Rastgele öğrenci listesi oluşturmak için kullanılır
import pandas as pd         # veri dosyasına yazma ve okuma işlemleri için kullanılır
import matplotlib.pyplot as plt      # veri görselleştirme için kullanılır

############ Exception Sınıfı #################
class OgrenciNoHatasi( Exception ): pass

########### Sınıf Class'ı #################
class Sinif:
    # default constructor
    def __init__(self):
        self.sinifListesi = []
    # öğrenci ekle
    def ekle(self, ogrenciNo, ogrenciBilgileri):
        # ogrenciBilgileri = {ad, soyad, vize1, vize2, final}
        # aynı öğrenci no'ya sahip bir öğrenci daha önceden kayıtlıysa öğrenciyi ekleme ve false dön, yoksa ekle ve true dön
        # parametre olarak öğrenci bilgileri listesi alır
        for x in self.sinifListesi:
            if x.ogrenciNo == ogrenciNo:
                ex = OgrenciNoHatasi("{} numaralı öğrenci zaten sistemde kayıtlı. Ekleme yapılamadı.".format(ogrenciNo))
                raise ex
        self.sinifListesi.append(Ogrenci.Ogrenci(ogrenciNo, ogrenciBilgileri))
        print(ogrenciNo, " numaralı öğrencinin kaydı yapıldı.")
    # öğrenci güncelle
    def guncelle(self, ogrenciNo, ogrenciBilgileri):
        # ogrenciBilgileri = [vize1, vize2, final]
        # aynı öğrenci no'ya sahip bir öğrenci daha önceden kayıtlıysa öğrenciyi güncelle, yoksa ekleme ve false dön
        # parametre olarak öğrenci bilgileri listesi alır

        for x in self.sinifListesi:
            if x.ogrenciNo == ogrenciNo:
                x.guncelle(ogrenciBilgileri)
                print(ogrenciNo," numaralı öğrencinin bilgileri güncellendi.")
                return
        ex = OgrenciNoHatasi('{} numaralı öğrenci sistemde kayıtlı değil. Güncelleme yapılamadı.'.format(x.ogrenciNo))     
        raise ex
    # öğrenci sil
    def sil(self, ogrenciNo):
        # öğrenci no'su verilen öğrenci sınıfa kayıtlıysa siler ve true döner. sınıfta yoksa false döner
        for x in self.sinifListesi:
            if x.ogrenciNo == ogrenciNo:
                self.sinifListesi.remove(x)
                print(ogrenciNo, " numaralı öğrencinin kaydı silindi.")
                return
        ex = OgrenciNoHatasi('{} numaralı öğrenci sistemde kayıtlı değil. Silme işlemi yapılamadı.'.format(ogrenciNo))  
        raise ex

    def rastgeleOgrenciOlustur(self):
        # İsim ve soyadı listelerinden rastgele isim seçerek öğrenci oluşturur. 
        # Rastgele olarak oluşturulan ad, soyad, vize1, vize2 ve final notlarından oluşan dict döner.
        isimListesi = ["Ali", "Mehmet", "Veli", "Murat", "Mahmut", "Selin", "Ayşe", "Ebru", "Zehra", "Nisa", "Selen"
                       , "Arzu", "Kemal", "Buket", "Aslı", "Gamze", "Gizem"]
        soyadiListesi = ["Karakaya", "Aydın", "Karaman", "Yıldırım", "Erkoç", "Koç", "Kaya", "Yıldız"
                         , "Doğan", "Öztürk", "Kılıç", "Çetin", "Aslan"]
        return {"Ad":random.choice(isimListesi), "Soyad":random.choice(soyadiListesi), 
                "Vize 1":random.randint(0,100), "Vize 2":random.randint(0,100), "Final":random.randint(0,100)}
        
    def rastgeleSinifDosyasiOlustur(self, dosyaAdi, kisiSayisi):
        # Parametre olarak verilen dosya adına sahip ve içerisinde parametre olarak verilen kişi sayısı kadar 
        # öğrencinin verileri bulunan .csv dosyasını oluşturur.
        # Öğrenci no bu aşamada eklenir. Öğrencilerin hepsi birbirinden farklı öğrenci no'suna sahiptir. Sırayla verilir
        sinifListesi = {}
        for i in range(0,kisiSayisi):
            ogrenciNo = 161101000 + i
            sinifListesi[ogrenciNo] = self.rastgeleOgrenciOlustur()
        df = pd.DataFrame(data=sinifListesi).T
        df.to_csv(dosyaAdi)
              
    def sinifDosyasindanOku(self, dosyaAdi):
        # Parametre olarak verilen dosya adına sahip .csv dosyasını okur ve sınıf listesini döner
        df = pd.read_csv(dosyaAdi, index_col=0)
        self.sinifListesi.clear()
        for ogrenciNo, ogrenciBilgileri in df.iterrows():
            self.sinifListesi.append(Ogrenci.Ogrenci(ogrenciNo, ogrenciBilgileri))
        print("\nVeriler dosyadan okundu.")
    
    def sinifKaydiListele(self):
        # Sınıftaki bütün öğrencilerin bilgilerini listeler
        
        # Başlık yaz
        print("%10s%15s%20s" %("Öğrenci No","Ad","Soyad"))
        print("---------------------------------------------")
        # Öğrenci bilgilerini yaz
        for x in self.sinifListesi:
            print("%10d%15s%20s" %(x.ogrenciNo,x.ad,x.soyad))
    
    def sinifBaşariNotlariniHesapla(self):
        # Sınıftaki bütün öğrencilerin başarı notlarını hesaplar ve bütün bilgilerini listeler
        
        # Başlık yaz
        print("%10s%15s%20s    %s  %s  %s  %s  %s  %s" %("Öğrenci No","Ad","Soyad","Vize1", "Vize2", "Final", "Not Ortalaması", "Harf Notu","Başarı Durumu"))
        print("---------------------------------------------------------------------------------------------------------------")
        # Öğrenci bilgilerini yaz
        for x in self.sinifListesi:
            x.notOrtalamasiHesapla()
            x.harfNotuHesapla()
            x.basariDurumuHesapla()
            print("%10d%15s%20s %7d%7d%7d%12d%13s%17s" %(x.ogrenciNo,x.ad,x.soyad,x.vize1,x.vize2,x.final,x.notOrtalamasi,x.harfNotu,x.basariDurumu))    
        
    def notOrtalamasinaGoreSirala(self):
        # lambda fonksiyonu ile verilen sınıf listesini not ortalamasına göre sıralar. (Parametre olarak verilen liste değişir)
        self.sinifListesi.sort(key=lambda x: x.notOrtalamasi, reverse=True)
        # Başlık yaz
        print("%10s%15s%20s    %s  %s  %s  %s  %s  %s" %("Öğrenci No","Ad","Soyad","Vize1", "Vize2", "Final", "Not Ortalaması", "Harf Notu","Başarı Durumu"))
        print("---------------------------------------------------------------------------------------------------------------")
        # Öğrenci bilgilerini yaz
        for x in self.sinifListesi:
            print("%10d%15s%20s %7d%7d%7d%12d%13s%17s" %(x.ogrenciNo,x.ad,x.soyad,x.vize1,x.vize2,x.final,x.notOrtalamasi,x.harfNotu,x.basariDurumu))                 
        print("\nSinif listesi başarı notlarına göre sıralanmıştır.\n")
        
    def istatistikiBilgileriYaz(self):
        # Öğrenci objelerinin içerisindeki not ortalamaları listesi çıkarılır 
        # istatistiksel işlemler onun üzerinden yapılır
        notOrtalamalari = [x.notOrtalamasi for x in self.sinifListesi]
        
        # istatistikleri hesapla
        enYuksekNotOrtalamasi = max(notOrtalamalari)
        enDusukNotOrtalamasi = min(notOrtalamalari)
        sinifOrtalamasi = scipy.mean(notOrtalamalari)
        ortalamaUzerindeOlanKisiSayisi = sum(x > sinifOrtalamasi for x in notOrtalamalari)
        basariYuzdesi = 100 * ortalamaUzerindeOlanKisiSayisi / len(notOrtalamalari)
        standartSapma = scipy.std(notOrtalamalari)
        
        # Bilgileri Yaz
        print("\n------------------İstatistiksel Bilgiler------------------")
        print("En yüksek not ortalaması \t: " , enYuksekNotOrtalamasi)
        print("En düşük not ortalaması \t: " , enDusukNotOrtalamasi)
        print("Sınıf Ortalaması \t\t: " , sinifOrtalamasi)
        print("Ortalama üzeri kişi sayısı \t: " , ortalamaUzerindeOlanKisiSayisi)
        print("Başarı yüzdesi \t\t\t:  %" , basariYuzdesi)
        print("Standart sapma \t\t\t: " , standartSapma)
        
        # Figür oluştur
        fig, ax = plt.subplots(nrows=1, ncols=2)
        # Sınıf Çan Eğrisi Grafiği 
        fit = scipy.stats.norm.pdf(notOrtalamalari, sinifOrtalamasi, standartSapma)
        ax[0].plot(notOrtalamalari,fit,'-o')
        ax[0].set_title('Sınıf Çan Eğrisi')
        ax[0].set_xlabel('Notlar')
        ax[0].set_ylabel('PDF')
        ax[0].grid()
        
        # Sınıftaki harf notu dağılımlarını hesapla
        harfNotlari = {"FF" : 0, "FD" : 0, "DD" : 0, "DC" : 0, "CC" : 0, "CB" : 0, "BB" : 0, "BA" : 0, "AA" : 0 }  
        for x in self.sinifListesi:
            harfNotlari[x.harfNotu] += 1    # öğrenci hangi harf notuna sahipse onun sayısını 1 arttır
           
        # Harf Notu Dağılımı Grafiği
        ax[1]
        ax[1].bar(list(harfNotlari.keys()), list(harfNotlari.values()), align='center')
        ax[1].set_title('Sınıftaki Harf Notu Dağılımları')
        ax[1].set_xlabel('Harf Notu')
        ax[1].set_ylabel('Kişi Sayısı')
        
        # Grafikleri Ekrana Bas
        plt.show(block=True)
        
    def sinifDosyasinaYaz(self, dosyaAdi):
        # Sınıf listesini verilen dosya adıyla .csv dosyasına kaydeder.
        sinifListesiDict = {}
        for x in self.sinifListesi:
           sinifListesiDict[x.ogrenciNo] = {"Ad":x.ad, "Soyad":x.soyad, "Vize 1":x.vize1, 
                                           "Vize 2":x.vize2, "Final":x.final, "Not Ortalaması":x.notOrtalamasi,
                                           "Harf Notu":x.harfNotu, "Başarı Durumu":x.basariDurumu}
        df = pd.DataFrame(data=sinifListesiDict).T
        df.to_csv(dosyaAdi)            
        print("Sınıf listesi çıktı dosyasına yazıldı.")
    
