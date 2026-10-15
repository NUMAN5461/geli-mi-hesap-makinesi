print("== Gelişmiş Hesap Makinesi ==")
print()
while True:

    secim = input("işlem seçin,1-yeni işlem,2-işlem geçmişi,3-geçmişi temizle,4-çıkış: ")
    print()

    if secim == "1":
        try:
            ılk_sayı = float(input("ilk sayıyı girin: "))
        except ValueError as e:
            print("sistem hatası mesajı:", e)
            break

        islem = input("işlem seçin,+,-,/,*")
        try:
            ıkıncı_sayı = float(input("ikinci sayıyı girin: "))
        except ValueError as e:
            print("sistem hatası mesajı:", e)
            break

        print()
        if islem == "+":
            sonuc = ılk_sayı + ıkıncı_sayı
            print(f"sonuc: {ılk_sayı} + {ıkıncı_sayı}={sonuc}")
        elif islem == "-":
            sonuc = ılk_sayı - ıkıncı_sayı
            print(f"sonuc: {ılk_sayı} - {ıkıncı_sayı}={sonuc}")
        elif islem == "/":
            if ıkıncı_sayı == 0:
                print("hiçbir sayı 0'a bölünmez,hatalı giriş")
                break
            sonuc = ılk_sayı / ıkıncı_sayı
            print(f"sonuc: {ılk_sayı} / {ıkıncı_sayı}={sonuc}")

        elif islem == "*":
            sonuc = ılk_sayı * ıkıncı_sayı
            print(f"sonuc: {ılk_sayı} * {ıkıncı_sayı}={sonuc}")
        else:
            print("hatalı giriş yaptınız")
            break

        with open("işlem_gecmisi.txt", "a", encoding="utf8") as dosya:
            dosya.write(f"Sonuç: {ılk_sayı}{islem}{ıkıncı_sayı}={sonuc}\n")
            print()
            print("kaydedildi")

    elif secim == "2":
        with open("işlem_gecmisi.txt", "r", encoding="utf8") as dosya:
            print(dosya.read())

    elif secim == "3":
        with open("işlem_gecmisi.txt", "w", encoding="utf8") as dosya:
            pass
        print("dosya temizlendi")

    elif secim == "4":
        print("çıkış yaptınız")
        break

    else:
        print("hatalı giriş yaptınız")
        break