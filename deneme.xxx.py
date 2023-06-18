menu={'Mantı' : 25, 'Döner' : 25, 'Lahmacun' : 20, 'İskender' : 20, 'Paça' : 18,
      'Kazandibi' : 15, 'Sütlaç' : 5, 'Künefe' : 20, 'Kete' : 20, 'Dilim Pasta' : 40,
      'Su' : 3, 'Kola' : 25, 'Soda' : 8, 'Çay' : 1, 'Soğuk Çay' : 5, 'Kahve Çeşitleri' : 5}

kodMenu={'0001':'Mantı','0002':'Döner','0003':'Lahmacun' ,'0004':'İskender' ,'0005':'Paça' ,
         '1001' :'Kazandibi','1002': 'Sütlaç','1003':'Künefe' ,'1004': 'Kete','1005': 'Dilim Pasta',
          '2001':'Su','2002':'Kola' ,'2003':'Soda' ,'2004':'Çay' ,'2005' :'Soğuk Çay','2006':'Kahve Çeşitleri'}
printMenu="""--------Menü------"""

for i in kodMenu.keys():
    if kodMenu[i] in menu.keys():
        b=menu[kodMenu[i]]
        printMenu += "\n{} : {} = {}TL".format(i, kodMenu[i], b)


print(printMenu)

def siparis(menu,kodMenu):
    #islemler uzadikca ayni toplam degerini kullanmak mumkun olmuyor.
    toplam=0
    toplam_1=0
    toplam_2=0
    toplam_3=0
    toplam_4=0

    sListesi = []
    siparisler="Siparis"
    while True:
        global donut


        a = input("Siparisinizin urun kodunu giriniz : ")

        if a in kodMenu.keys():
            sListesi.append(a)

        elif a == "e" or a == "E":
            for i in sListesi:
                if i in kodMenu.keys():

                    c=kodMenu[i]
                    toplam+=menu[c]
                    siparisler+="\n{} = {}".format(c,menu[c])
                else:
                    print("kodlar hatalı")
            siparisler+="\nToplam Tutar : {}".format(toplam)
            print(siparisler)
            donut=input("Siparisi Onayliyor musunuz ? E/H")

            if donut == "e" or donut == "E":
                #yarın dosya kayıt işlemlerine çalışıp bu sipariş verilerini bir dosyaya kaydet
                toplam-=toplam
                siparisler=siparisler.replace(siparisler[:len(siparisler)],"")
                newList = sListesi.clear()
                print("Onaylandi")


            elif donut == "h" or donut == "H":
                donut_1=input("Yapmak istediğiniz işlemi seçiniz: Iptal(I) / Duzenleme(D)")

                if donut_1=="I" or donut_1=="ı":
                    toplam -= toplam
                    siparisler=siparisler.replace(siparisler[:len(siparisler)], "")
                    newList_1=sListesi.clear()
                    print("İptal islemi basarili")


                elif donut_1 =="d" or donut_1=="D":

                    new=input("Yapmak istediginiz islemi secin : Urun Ekleme(U) / Urun Silme(S)")

                    if new == "u" or new == "U":
                        adet_1=int(input("Kac adet urun eklemek istiyorsunuz : "))
                        if adet_1>20 and adet_1<0 :
                            print("Gecersiz veri girisi yaptiniz. Tekrar deneyiniz !!!")

                        elif adet_1<20 and adet_1>0:

                            for h in range(0,adet_1):
                                a = input("Siparisinizin urun kodunu giriniz : ")
                                sListesi.append(a)
                            siparisler = siparisler.replace(siparisler[:len(siparisler)], "")
                            for i in sListesi:
                                if i in kodMenu.keys():
                                    c = kodMenu[i]
                                    toplam_2 += menu[c]
                                    siparisler += "\n{} = {}".format(c, menu[c])

                            arti=toplam_2-toplam
                            toplam+=arti
                            siparisler += "\nToplam Tutar : {}".format(toplam_2)
                            print(siparisler)
                            donut_u = input("Siparisi Onayliyor musunuz ? E/H")

                            if donut_u=="e" or donut_u=="E":
                                toplam -= toplam
                                siparisler = siparisler.replace(siparisler[:len(siparisler)], "")
                                newList_2 = sListesi.clear()
                                print("Onaylandi")


                            elif donut_u=="h" or donut_u=="H":
                                donut_u_1=input("yapmak istediginiz islemi giriniz : Iptal(I) / Duzenleme(D)")

                                if donut_u_1 == "I" or donut_u_1=="ı":
                                    toplam-=toplam
                                    siparisler = siparisler.replace(siparisler[:len(siparisler)], "")
                                    newList_1 = sListesi.clear()
                                    print("İptal islemi basarili")

                                elif donut_u_1=="d" or donut_u_1=="D":
                                    donut_u_1_a=input("Yapmak istediginiz islemi giriniz : Urun ekleme(U) / Urun Silme(S)")

                                    if donut_u_1_a=="U" or donut_u_1_a=="u":
                                        adet_1_da = int(input("Kac adet urun eklemek istiyorsunuz : "))
                                        for h in range(0, adet_1_da):
                                            at = input("Siparisinizin urun kodunu giriniz : ")
                                            sListesi.append(at)
                                        siparisler = siparisler.replace(siparisler[:len(siparisler)], "")

                                        for i in sListesi:

                                            if i in kodMenu.keys():
                                                c = kodMenu[i]
                                                toplam_3 += menu[c]
                                                siparisler += "\n{} = {}".format(c, menu[c])
                                        arti_1 = toplam_3 - toplam
                                        toplam += arti_1
                                        siparisler += "\nToplam Tutar : {}".format(toplam_3)
                                        print(siparisler)
                                        son=input("İslemi onayliyor musunuz ? : E/H")

                                        if son == "e" or son =="E":
                                            toplam -= toplam
                                            siparisler = siparisler.replace(siparisler[:len(siparisler)], "")
                                            newList_2 = sListesi.clear()
                                            print("Onaylandi")

                                        elif son == "h" or son == "H":
                                            toplam -= toplam
                                            siparisler = siparisler.replace(siparisler[:len(siparisler)], "")
                                            newList_1 = sListesi.clear()
                                            print("Cok fazla hatali islem yaptiniz. Islem iptal edildi")

                                    elif donut_u_1_a == "s" or donut_u_1_a=="S":
                                        adet_2_da = int(input("Kac adet urun sileceksiniz : "))

                                        for j in range(0, adet_2_da):
                                            sil = input("Silinecek elemanın kodunu giriniz : ")
                                            sEleman = sListesi.index(sil)
                                            sListesi.pop(sEleman)
                                            siparisler = siparisler.replace(siparisler[:len(siparisler)], "")

                                        for i in sListesi:

                                            if i in kodMenu.keys():

                                                c = kodMenu[i]
                                                toplam_4 += menu[c]
                                                siparisler += "\n{} = {}".format(c, menu[c])
                                            else:
                                                print("kodlar hatalı")

                                        fark = toplam - toplam_4
                                        toplam = toplam - fark
                                        siparisler += "\nToplam Tutar : {}".format(toplam_4)
                                        print(siparisler)
                                        donut = input("Siparisi Onayliyor musunuz ? E/H")

                                    else:
                                        print("Hatali islem yaptiniz.")
                                        break


                    elif new == "s" or new == "S":
                        adet=int(input("Kac adet urun sileceksiniz : "))
                        for j in range(0,adet):
                            sil=input("Silinecek elemanın kodunu giriniz : ")
                            sEleman=sListesi.index(sil)
                            sListesi.pop(sEleman)
                            siparisler=siparisler.replace(siparisler[:len(siparisler)], "")

                        for i in sListesi:
                            if i in kodMenu.keys():

                                c = kodMenu[i]
                                toplam_1 += menu[c]
                                siparisler += "\n{} = {}".format(c, menu[c])
                            else:
                                print("kodlar hatalı")
                        fark=toplam-toplam_1
                        toplam=toplam-fark
                        siparisler += "\nToplam Tutar : {}".format(toplam)
                        print(siparisler)
                        donut_s = input("Siparisi Onayliyor musunuz ? E/H")
                        if donut_s == "e" or donut_s == "E":
                            toplam -= toplam
                            siparisler = siparisler.replace(siparisler[:len(siparisler)], "")
                            newList_2 = sListesi.clear()
                            print("Onaylandi")


                        elif donut_s == "h" or donut_s == "H":
                            donut_s_1 = input("yapmak istediginiz islemi giriniz : Iptal(I) / Duzenleme(D)")

                            if donut_s_1 == "I" or donut_s_1 == "ı":
                                toplam -= toplam
                                siparisler = siparisler.replace(siparisler[:len(siparisler)], "")
                                newList_1 = sListesi.clear()
                                print("İptal islemi basarili")

                            elif donut_s_1 == "d" or donut_s_1 == "D":
                                donut_s_1_a = input("Yapmak istediginiz islemi giriniz : Urun ekleme(U) / Urun Silme(S)")

                                if donut_s_1_a == "U" or donut_s_1_a == "u":
                                    adet_1_da = int(input("Kac adet urun eklemek istiyorsunuz : "))
                                    for h in range(0, adet_1_da):
                                        at = input("Siparisinizin urun kodunu giriniz : ")
                                        sListesi.append(at)
                                    siparisler = siparisler.replace(siparisler[:len(siparisler)], "")

                                    for i in sListesi:

                                        if i in kodMenu.keys():
                                            c = kodMenu[i]
                                            toplam_3 += menu[c]
                                            siparisler += "\n{} = {}".format(c, menu[c])
                                    arti_1 = toplam_3 - toplam
                                    toplam += arti_1
                                    siparisler += "\nToplam Tutar : {}".format(toplam_3)
                                    print(siparisler)
                                    son = input("İslemi onayliyor musunuz ? : E/H")

                                    if son == "e" or son == "E":
                                        toplam -= toplam
                                        siparisler = siparisler.replace(siparisler[:len(siparisler)], "")
                                        newList_2 = sListesi.clear()
                                        print("Onaylandi")

                                    elif son == "h" or son == "H":
                                        toplam -= toplam
                                        siparisler = siparisler.replace(siparisler[:len(siparisler)], "")
                                        newList_1 = sListesi.clear()
                                        print("Cok fazla hatali islem yaptiniz. Islem iptal edildi")

                                elif donut_s_1_a == "s" or donut_s_1_a == "S":
                                    adet_2_da = int(input("Kac adet urun sileceksiniz : "))

                                    for j in range(0, adet_2_da):
                                        sil = input("Silinecek elemanın kodunu giriniz : ")
                                        sEleman = sListesi.index(sil)
                                        sListesi.pop(sEleman)
                                        siparisler = siparisler.replace(siparisler[:len(siparisler)], "")

                                    for i in sListesi:

                                        if i in kodMenu.keys():

                                            c = kodMenu[i]
                                            toplam_4 += menu[c]
                                            siparisler += "\n{} = {}".format(c, menu[c])
                                        else:
                                            print("kodlar hatalı")

                                    fark = toplam - toplam_4
                                    toplam = toplam - fark
                                    siparisler += "\nToplam Tutar : {}".format(toplam_4)
                                    print(siparisler)
                                    donut = input("Siparisi Onayliyor musunuz ? E/H")

                                else:
                                    print("Hatali islem yaptiniz.")
                                    break



        else:
            print("Hatali veri girisi yaptiniz.")
            break

#Guvenlik ve daha saglikli bir islem yapabilmek icin "adet" elemanlerini kisitlanabilir. ancak uzun olcagı icin ugrasmadim.
#zaten baslangic duzeyi bir uygulama.
#daha profesyonel bir tasarimi yine ayni klasörde yazacagim.
siparis(menu,kodMenu)



