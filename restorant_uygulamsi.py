import random
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time
import datetime
import random
from tkinter import *
from tkinter import messagebox

pencere = Tk()
pencere.title("Restorant Uygulaması")
pencere.configure(background="white")

ana_tablo= Frame(pencere,background="white")
ana_tablo.pack(side=TOP)
baslik=Label(ana_tablo,font=("times",30,"bold"),text="Sipariş Uygulaması",fg="black",bg="white")
baslik.grid(column=0,row=0)

butonlar=Frame(pencere,background="white",padx=100)
butonlar.pack(side=LEFT)

fatura=Frame(pencere,background="white")
fatura.place(y=400,x=100)
sonuc=Frame(pencere,background="white")
sonuc.place(y=450,x=100)
#Menu box

Ana_Menu=Frame(pencere,bd=2,relief=RIDGE)
Ana_Menu.place(y=150,x=100)

Icecek_Menu=Frame(Ana_Menu,padx=50)
Icecek_Menu.pack(side=RIGHT)
st_0=Label(Icecek_Menu,text="İçecekler",font=("times",15,"bold"))
st_0.grid(column=0,row=0)

Yemek_Menu=Frame(Ana_Menu,padx=50)
Yemek_Menu.pack(side=LEFT)
st_1=Label(Yemek_Menu,text="Yemekler",font=("times",15,"bold"))
st_1.grid(column=0,row=0)

Tatli_Menu=Frame(Ana_Menu,background="white",padx=50)
Tatli_Menu.pack(side=LEFT)
st_2=Label(Tatli_Menu,text="Tatlılar",background="white",font=("times",15,"bold"))
st_2.grid(column=0,row=0)

satis_kayit=open("satis_dosyas.txt",W)


#Degiskenler

Toplam_Tutar=IntVar()


Cay_Fiyat=IntVar()
Su_Fiyat=IntVar()
Kahve_Fiyat=IntVar()

Hangel_Fiyat=IntVar()
Piti_Fiyat=IntVar()
Gartof_Fiyat=IntVar()

Sutlac_Fiyat=IntVar()
Kazandibi_Fiyat=IntVar()
Tiramisu_Fiyat=IntVar()

Cay_Fiyat.set(5)
Su_Fiyat.set(4)
Kahve_Fiyat.set(15)

Hangel_Fiyat.set(25)
Piti_Fiyat.set(40)
Gartof_Fiyat.set(7)

Sutlac_Fiyat.set(15)
Kazandibi_Fiyat.set(15)
Tiramisu_Fiyat.set(25)

Cay_Adet=IntVar()
Su_Adet=IntVar()
Kahve_Adet=IntVar()

Hangel_Adet=IntVar()
Piti_Adet=IntVar()
Gartof_Adet=IntVar()

Sutlac_Adet=IntVar()
Kazandibi_Adet=IntVar()
Tiramisu_Adet=IntVar()
Receipt_Ref=StringVar()


#Fonksiyonlar

def Exit():
    aexit=messagebox.askyesno("Sayfadan çıkılsın mı ?", "Çıkmak istiyorsanız onaylayın.")
    if aexit > 0:
        pencere.destroy()
        return


def Sil():
    Toplam_Tutar.set(0)
    Cay_Adet.set(0)
    Su_Adet.set(0)
    Kahve_Adet.set(0)

    Hangel_Adet.set(0)
    Piti_Adet.set(0)
    Gartof_Adet.set(0)

    Sutlac_Adet.set(0)
    Kazandibi_Adet.set(0)
    Tiramisu_Adet.set(0)

    txtCay.configure(state=DISABLED)
    txtSu.configure(state=DISABLED)
    txtKahve.configure(state=DISABLED)

    txtHangel.configure(state=DISABLED)
    txtPiti.configure(state=DISABLED)
    txtGartof.configure(state=DISABLED)

    txtSutlac.configure(state=DISABLED)
    txtKazandibi.configure(state=DISABLED)
    txtTiramisu.configure(state=DISABLED)
    txtReceipt.delete("1.0", END)

def yazdir():
    txtReceipt.delete("1.0", END)
    txtReceipt.insert(END,"\t\tFiyat\t\t\tAdet"+"\n\n")
    txtReceipt.insert(END, "Hangel :\t\t{}TL\t\t\t{}\n".format(Hangel_Fiyat.get(),Hangel_Adet.get()))
    txtReceipt.insert(END, "Piti:\t\t{}TL\t\t\t{}\n" .format(Piti_Fiyat.get() ,Piti_Adet.get()) )
    txtReceipt.insert(END, "Gartof:\t\t{}TL\t\t\t{}\n" .format(Gartof_Fiyat.get() , Gartof_Adet.get()))
    txtReceipt.insert(END, "Sütlaç:\t\t{}TL\t\t\t{}\n".format(Sutlac_Fiyat.get() , Sutlac_Adet.get()))
    txtReceipt.insert(END, "Kazandibi:\t\t{}TL\t\t\t{}\n".format(Kazandibi_Fiyat.get() , Kazandibi_Adet.get()))
    txtReceipt.insert(END, "Tiramisu:\t\t{}TL\t\t\t{}\n".format(Tiramisu_Fiyat.get() , Tiramisu_Adet.get()))
    txtReceipt.insert(END, "Çay:\t\t{}TL\t\t\t{}\n" .format(Cay_Fiyat.get() , Cay_Adet.get()))
    txtReceipt.insert(END, "Su:\t\t{}TL\t\t\t{}\n".format(Su_Fiyat.get() , Su_Adet.get()))
    txtReceipt.insert(END, "Kahve:\t\t{}TL\t\t\t{}\n\n".format(Kahve_Fiyat.get() , Kahve_Adet.get()))
    txtReceipt.insert(END,"Toplam Tutar : \t\t\t\t\t{} TL".format(Toplam_Tutar.get()))


def Toplam():
    global Toplam_Tutar
    Item_1=int(Cay_Adet.get())
    Item_2=int(Su_Adet.get())
    Item_3=int(Kahve_Adet.get())
    Item_4=int(Hangel_Adet.get())
    Item_5=int(Piti_Adet.get())
    Item_6=int(Gartof_Adet.get())
    Item_7=int(Sutlac_Adet.get())
    Item_8=int(Kazandibi_Adet.get())
    Item_9=int(Tiramisu_Adet.get())

    Toplam_icecek=int((5 * Item_1) + (4 * Item_2) + (15 * Item_3))
    Toplam_Yemek=int((25 * Item_4) + (40 * Item_5) + (7* Item_6))
    Toplam_Tatli= int((15 * Item_7) + (15 * Item_8)+(25 * Item_9))


    Tt=Toplam_Tatli+Toplam_Yemek+Toplam_icecek
    Toplam_Tutar.set(Tt)


def Onay():
    onay=messagebox.askyesno("İşlemi Onaylıyor Musun ?", "Evetse Onaylayın")
    if onay==YES:
        yes=messagebox.showinfo(title="Başarılı", message="Başarıyla kaydedildi")
        satis_kayit.write(txtReceipt)
        return Sil()
    elif onay==NO:
        no=messagebox.showwarning(title="Başarısız",message="Kayıt işlemi gerçekleşmedi")
        return Sil()


#Yerlestirme. Ogeleri Menudeki yerlerine Koyacagız

txtCay=Entry(Icecek_Menu,font=("times", 13, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED,textvariable=Cay_Fiyat)
txtCay.grid(column=1,row=1)
txtSu=Entry(Icecek_Menu,font=("times", 13, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED,textvariable=Su_Fiyat)
txtSu.grid(column=1,row=2)
txtKahve=Entry(Icecek_Menu,font=("times", 13, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED,textvariable=Kahve_Fiyat)
txtKahve.grid(column=1,row=3)

txtHangel=Entry(Yemek_Menu,font=("times", 13, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED,textvariable=Hangel_Fiyat)
txtHangel.grid(column=1,row=1)
txtPiti=Entry(Yemek_Menu,font=("times", 13, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED,textvariable=Piti_Fiyat)
txtPiti.grid(column=1,row=2)
txtGartof=Entry(Yemek_Menu,font=("times", 13, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED,textvariable=Gartof_Fiyat)
txtGartof.grid(column=1,row=3)

txtSutlac=Entry(Tatli_Menu,font=("times", 13, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED,textvariable=Sutlac_Fiyat)
txtSutlac.grid(column=1,row=1)
txtKazandibi=Entry(Tatli_Menu,font=("times", 13, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED,textvariable=Kazandibi_Fiyat)
txtKazandibi.grid(column=1,row=2)
txtTiramisu=Entry(Tatli_Menu,font=("times", 13, "bold"), bd=9, width=7, justify=LEFT, state=DISABLED,textvariable=Tiramisu_Fiyat)
txtTiramisu.grid(column=1,row=3)

"""Ögelerin isimlerini ekleyeceğiz"""
nameTatli_1=Label(Tatli_Menu,text="Sütlaç",font=("times",13),background="White").grid(row=1)
nameTatli_2=Label(Tatli_Menu,text="Kazandibi",font=("times",13),background="White").grid(row=2)
nameTatli_3=Label(Tatli_Menu,text="Tiramisu",font=("times",13),background="White").grid(row=3)

nameYemek_1=Label(Yemek_Menu,text="Hangel",font=("times",13)).grid(row=1)
nameYemek_2=Label(Yemek_Menu,text="Piti",font=("times",13)).grid(row=2)
nameYemek_3=Label(Yemek_Menu,text="Gartof",font=("times",13)).grid(row=3)

nameIcecek_1=Label(Icecek_Menu,text="Çay",font=("times",13)).grid(column=0,row=1)
nameIcecek_2=Label(Icecek_Menu,text="Su",font=("times",13)).grid(row=2)
nameIcecek_3=Label(Icecek_Menu,text="Kahve",font=("times",13)).grid(row=3)

"""Ögelerin adet kutularını ekleyeceğiz"""
adet_1=Entry(Yemek_Menu,font=("times",13,"bold"),bd=9, width=7, justify=LEFT,textvariable=Hangel_Adet).grid(column=2,row=1)
adet_2=Entry(Yemek_Menu,font=("times",13,"bold"),bd=9, width=7, justify=LEFT,textvariable=Piti_Adet).grid(column=2,row=2)
adet_3=Entry(Yemek_Menu,font=("times",13,"bold"),bd=9, width=7, justify=LEFT,textvariable=Gartof_Adet).grid(column=2,row=3)

adet_4=Entry(Tatli_Menu,font=("times",13,"bold"),bd=9, width=7, justify=LEFT, textvariable=Sutlac_Adet).grid(column=2,row=1)
adet_5=Entry(Tatli_Menu,font=("times",13,"bold"),bd=9, width=7, justify=LEFT, textvariable=Kazandibi_Adet).grid(column=2,row=2)
adet_6=Entry(Tatli_Menu,font=("times",13,"bold"),bd=9, width=7, justify=LEFT, textvariable=Tiramisu_Adet).grid(column=2,row=3)

adet_7=Entry(Icecek_Menu,font=("times",13,"bold"),bd=9, width=7, justify=LEFT, textvariable=Cay_Adet).grid(column=2,row=1)
adet_8=Entry(Icecek_Menu,font=("times",13,"bold"),bd=9, width=7, justify=LEFT, textvariable=Su_Adet).grid(column=2,row=2)
adet_9=Entry(Icecek_Menu,font=("times",13,"bold"),bd=9, width=7, justify=LEFT, textvariable=Kahve_Adet).grid(column=2,row=3)

"""Butonları Yerleştireceğiz"""

buton_sil=Button(butonlar,text="Sil",font=("times",13,"bold"),command=Sil).grid(column=0,row=0)
buton_toplam=Button(butonlar,text="Topla", font=("times",13,"bold"),command=Toplam).grid(column=1,row=0)
buton_onay=Button(butonlar,text="Onay", font=("times",13,"bold"),command=Onay).grid(column=2,row=0)
buton_yazdir=Button(butonlar,text="Yazdır",font=("times",13,"bold"),command=yazdir).grid(column=3,row=0)
butonc_cik=Button(butonlar,text="Çık",font=("times",13,"bold"),command=Exit).grid(column=4,row=0)

"""Toplam tutarı görmek için değişkeni ekrana yazdırıyoruz"""

value=Label(fatura,text="Toplam Tutar = ",font=("times",13,"bold"),background="White",).grid(column=0,row=0)
toplam_tutar=Label(fatura,font=("times",13,"bold"),background="White",bd=9, width=7,state=DISABLED,textvariable=Toplam_Tutar).grid(column=1,row=0)

txtReceipt=Text(sonuc, width=50, height=9, bg="#AEB6BF", bd=4, font=("times", 12, "bold"))
txtReceipt.grid(column=0,row=0)








pencere.mainloop()

