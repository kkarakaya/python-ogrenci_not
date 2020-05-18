class Ogrenci:
    # default constructor
    # Bir öğrenci ogrenci no, ad, soyad, vize1, vize 2 ve final bilgilerini içeren bir listenin parametre
    # olarak verilmesi ile oluşturulur
    def __init__(self, ogrenciNo, ogrenciBilgileri):
        self.ogrenciNo = ogrenciNo
        self.ad = ogrenciBilgileri["Ad"]
        self.soyad = ogrenciBilgileri["Soyad"]
        self.vize1 = ogrenciBilgileri["Vize 1"]
        self.vize2 = ogrenciBilgileri["Vize 2"]
        self.final = ogrenciBilgileri["Final"]
        
        # hesaplama komutu gelene kadar başlangıç değerleri atanır
        self.notOrtalamasi = 0
        self.harfNotu = "FF"
        self.basariDurumu = "KALDI"
    
    def guncelle(self, ogrenciBilgileri):
        self.vize1 = ogrenciBilgileri["Vize 1"]
        self.vize2 = ogrenciBilgileri["Vize 2"]
        self.final = ogrenciBilgileri["Final"]
        
    def notOrtalamasiHesapla(self):
        self.notOrtalamasi = round((self.vize1 * 20 + self.vize2 * 30 + self.final * 50) / 100)
        
    def harfNotuHesapla(self):
        if(self.notOrtalamasi >= 90):
            self.harfNotu = "AA"
        elif(self.notOrtalamasi >= 85):
            self.harfNotu = "BA"
        elif(self.notOrtalamasi >= 80):
            self.harfNotu = "BB"
        elif(self.notOrtalamasi >= 75):
            self.harfNotu = "CB"
        elif(self.notOrtalamasi >= 70):
            self.harfNotu = "CC"
        elif(self.notOrtalamasi >= 65):
            self.harfNotu = "DC"
        elif(self.notOrtalamasi >= 60):
            self.harfNotu = "DD"
        elif(self.notOrtalamasi >= 50):
            self.harfNotu = "FD"
        else:
            self.harfNotu = "FF"
            
    def basariDurumuHesapla(self):
        basariDurumlari = {
            "AA" : "GEÇTİ",
            "BA" : "GEÇTİ",
            "BB" : "GEÇTİ",
            "CB" : "GEÇTİ",
            "CC" : "GEÇTİ",
            "DC" : "GEÇTİ",
            "DD" : "GEÇTİ",
            "FD" : "Şartlı Geçti",
            "FF" : "KALDI"
        }
        self.basariDurumu = basariDurumlari[self.harfNotu]
                     