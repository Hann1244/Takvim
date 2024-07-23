from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import datetime
import time
import locale
import pytz  


class Zaman():
    __anaPencere = ""
    __dilAyari = ""
    __gosterimSekli = "%d %B %Y %A %X"
    __hafizaZaman = datetime.timedelta(days=0, weeks=0, hours=0, minutes=0, seconds=0)
    __kullanilanUTC = "Sistemin yerel UTC'sini kullan"
    __degistirilenUTC = "Sistemin yerel UTC'sini kullan"
    __dosya = open("TkinterTimeApplication_ErrorFile.txt", "w+")

    def __init__(self):
        try:
            locale.setlocale(locale.LC_ALL, self.__dilAyari)
            self.anaPencereYap()
            self.anaPencereNesneleri()
            self.calistir()
            self.__anaPencere.mainloop()
        except Exception as hata:
            print("Sistem yerel zamanına göre => {} => {}".format(datetime.datetime.now(), hata), file=self.__dosya)

    def anaPencereYap(self):
        self.__anaPencere = Tk()
        self.__anaPencere.title("Tkinter zaman uygulaması (Tkinter Time Application)")           
        self.__anaPencere.geometry("600x400")
        self.__anaPencere.resizable(width=FALSE, height=FALSE)

    def anaPencereNesneleri(self):
        self.etiketZaman = Label(self.__anaPencere, font="Time 15")    
        menu1 = Menu(self.__anaPencere)
        self.__anaPencere.config(menu=menu1)
        menuAyarlar = Menu(menu1, tearoff=0)
        menu1.add_cascade(label="Ayarlar", menu=menuAyarlar)
        menuAyarlar.add_command(label="Dil Ayarı", command= self.dilAyari)
        menuAyarlar.add_command(label="Zaman Ayarı", command= self.zamanAyari)
        menuAyarlar.add_command(label="Gösterim Ayarı", command= self.gosterimAyari)
        menuAyarlar.add_command(label="Standart Ayarlara Dön", command= self.standartAyarlar)
        menuYardim = Menu(menu1, tearoff=0)
        menu1.add_cascade(label= "Yardım", menu=menuYardim)
        menuYardim.add_command(label="Hakkımda", command=self.hakkimda)
        menuYardim.add_command(label="Açıklamalar", command=self.acikla)
        self.etiketZaman.place(relx=0.3, rely=0.30)

    def hakkimda(self):
        showinfo("Hakkımda", "İbrahim Orhan tarafından yapıldı\n(Created by: İbrahim Orhan)\n\n{}\n\n{}".format(
            "https://github.com/Hann1244", "https://github.com/Hann1244"))    
        
    def acikla(self):
        aciklamaMetni = """  Tercih ettiğin dilde tercih ettiğin gösterimde,
zamanı gösteren bir uygulamadır. Ayrıca zamanı ayarlama özelliği de bulunmaktadır.
    Karşılaşılan hataları, oluşturacağı TkinterTimeAppliqation_ErrorFile.txt dosyasına yazmaktadır."""    
        showinfo ("Açıklamalar", aciklamaMetni) 

    def standartAyarlar(self):
        self.__dilAyari = ""
        locale.setlocale(locale.LC_ALL, self.__dilAyari)
        self.__gosterimSekli = "%d %B %Y %A %X"
        self.__hafizaZaman = datetime.timedelta(days=0, hours=0, minutes=0, seconds=0)
        self.__kullanilanUTC = "Sistemin yerel UTC'sini kullan"
        self.__degistirilenUTC = "Sistemin yerel UTC'sini kullan"
        showinfo("Bilgilendirme", 'Standart Ayarlara Dönüldü!')

    def dilAyari(self):
        self.pencere = Toplevel(self.__anaPencere)
        self.pencere.title("Uygulamanın Dil Ayar Penceresi")
        self.pencere.geometry("375x200")
        self.pencere.resizable(width=FALSE, height=FALSE)
        etiketDil= Label(self.pencere, text= "Bir dil seçiniz=>")
        self.seceneklerDil = {
            "Sistem Dili": "",
            "Türkçe": "turkish",
            "İtalyanca": "italian",
            "İngilizce": "english",
            "Fransızca": "french",
            "Almanca": "german",
            "İspanyolca": "spanish"
        }
        self.comboDiller = ttk.Combobox(self.pencere, state='readonly', values=[*self.seceneklerDil.keys()])
        indeks= 0
        for anahtar, deger in self.seceneklerDil.items():
            if deger == self.__dilAyari:
                self.comboDiller.current(indeks)
                break
            indeks += 1
        buttonOnay = Button(self.pencere, text="Değişiklikleri Onayla", command=self.dilUygula)
        etiketDil.grid(row=0, column=0, pady=12, padx=2)
        self.comboDiller.grid(row=0, column=1, pady=12, padx=2)
        buttonOnay.grid(row=0, column=2, pady=12, padx=2)
        self.pencere.mainloop()

    def dilUygula(self):
        self.__dilAyari = self.seceneklerDil[self.comboDiller.get()]
        locale.setlocale(locale.LC_ALL, self.__dilAyari)
        showinfo("Bilgilendirme", "Saatin dil ayarı '{}' olarak değiştirildi !".format(self.comboDiller.get()))
        self.pencere.destroy()

    def gosterimAyari(self):
        self.pencere1 = Toplevel(self.__anaPencere)
        self.pencere1.title("Uygulamanın Zaman Gösterme Ayar Penceresi")
        self.pencere1.geometry("465x200")
        self.pencere1.resizable(width= FALSE, height=FALSE)
        etiketGosterim = Label(self.pencere1, text="Bir gösterim şekli seçiniz =>")
        self.an = datetime.datetime.now()
        self.seceneklerGosterim = {
            datetime.datetime.strftime(self.an, "%c"): "%c",
            datetime.datetime.strftime(self.an, "%x"): "%x",
            datetime.datetime.strftime(self.an, "%X"): "%X",
            datetime.datetime.strftime(self.an, "%d %B %Y"): "%d %B %Y",
            datetime.datetime.strftime(self.an, "%d %B %Y %X"): "%d %B %Y %X",
            datetime.datetime.strftime(self.an, "%d %b %Y"): "%d %b %Y",
            datetime.datetime.strftime(self.an, "%d %b %Y %X"): "%d %b %Y %X",
            datetime.datetime.strftime(self.an, "%d %B %Y %A"): "%d %B %Y %A",
            datetime.datetime.strftime(self.an, "%d %B %Y %A %X"): "%d %B %Y %A %X",
            datetime.datetime.strftime(self.an, "%d %b %Y %A"): "%d %b %Y %A",
            datetime.datetime.strftime(self.an, "%d %b %Y %A %X"): "%d %b %Y %A %X",
            datetime.datetime.strftime(self.an, "%d %B %A "): "%d %B %A ",
            datetime.datetime.strftime(self.an, "%d %b %A %X"): "%d %b %A %X",
            datetime.datetime.strftime(self.an, "%x %H %M"): "%x %H %M",
            datetime.datetime.strftime(self.an, "%x %A %X"): "%x %A %X",
        }
        self.comboSekiller = ttk.Combobox(self.pencere1, state='readonly', values=[*self.seceneklerGosterim.keys()])
        indeks = 0
        for anahtar, deger in self.seceneklerGosterim.items():
            if deger == self.__gosterimSekli:
                self.comboSekiller.current(indeks)
                break
            indeks += 1
        buttonOnay = Button(self.pencere1, text="Değişiklikleri Onayla", command= self.gosterimUygula)
        etiketGosterim.grid(row=0, column=0, pady=12, padx=2)
        self.comboSekiller.grid(row=0, column=1, pady=12, padx=2)
        buttonOnay.grid(row=0, column=2, pady=12, padx=2)
        self.pencere1.mainloop()

    def gosterimUygula(self):
        self.__gosterimSekli = self.seceneklerGosterim[self.comboSekiller.get()]
        showinfo("Bilgilendirme", "Zamanın gösterim şekli '{}' olarak değiştirildi !".format(self.comboSekiller.get()))
        self.pencere1.destroy()

    def zamanAyari(self):
        self.pencere2 = Toplevel(self.__anaPencere)
        self.pencere2.title("Uygulamanın Zaman Ayar Penceresi")
        self.pencere2.geometry("585x300")
        self.pencere2.resizable(width=FALSE, height=FALSE)
        etiketZaman = Label(self.pencere2, text="Saatin kaç saniye ileri/geri olacağını belirleyiniz.\nBir UTC seçiniz.\nSistem yerel UTC'si UTC'yi alır.")
        etiketZaman.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.girisSaat = Entry(self.pencere2)
        self.comboUTC = ttk.Combobox(self.pencere2, state='readonly', values=pytz.all_timezones)
        self.comboUTC.set(self.__degistirilenUTC)
        self.girisSaat.grid(row=1, column=1, pady=12, padx=2)
        self.comboUTC.grid(row=1, column=2, pady=12, padx=2)
        buttonOnay = Button(self.pencere2, text="Değişiklikleri Onayla", command=self.zamanUygula)
        buttonOnay.grid(row=1, column=3, pady=12, padx=2)
        self.pencere2.mainloop()

    def zamanUygula(self):
        try:
            saniye = int(self.girisSaat.get())
            self.__hafizaZaman = datetime.timedelta(seconds=saniye)
            self.__degistirilenUTC = self.comboUTC.get()
            showinfo("Bilgilendirme", "Saat dilimi '{}' olarak değiştirildi !".format(self.comboUTC.get()))
            self.pencere2.destroy()
        except Exception as hata:
            showerror("Hata", hata)
            
    def saatGuncelle(self):
        try:
            if self.__degistirilenUTC == self.__kullanilanUTC:
                an = datetime.datetime.now()
            else:
                an = datetime.datetime.now(pytz.timezone(self.__degistirilenUTC))
            an += self.__hafizaZaman
            zaman = an.strftime(self.__gosterimSekli)
            self.etiketZaman.config(text=zaman)
            self.__anaPencere.after(1000, self.saatGuncelle)
        except Exception as hata:
            print("Sistem yerel zamanına göre => {} => {}".format(datetime.datetime.now(), hata), file=self.__dosya)
            
    def calistir(self):
        try:
            self.saatGuncelle()
        except Exception as hata:
            print("Sistem yerel zamanına göre => {} => {}".format(datetime.datetime.now(), hata), file=self.__dosya)


Zaman()
