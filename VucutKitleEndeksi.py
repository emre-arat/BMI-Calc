import tkinter

window = tkinter.Tk()
window.title("BMI")
window.minsize(250,200)

label1 = tkinter.Label(text="Boyunuzu giriniz.(metre cinsinden)")
label1.place(x=35,y=10)
kutu1 =tkinter.Entry()
kutu1.place(x=35,y=30)


label2 = tkinter.Label(text="Kilonuzu giriniz.")
label2.place(x=35,y=50)
kutu2 =tkinter.Entry()
kutu2.place(x=35,y=70)


def index_hesapla():
    sonuç_label = tkinter.Label(text="")
    try:
        boy = float(kutu1.get())
        kilo = float(kutu2.get())
        sonuç = kilo / boy ** 2

        if sonuç >= 25:
            cevap = "Kilonuz fazla!!"
        elif sonuç <25 and sonuç > 18.5:
            cevap = "Normal kilodasınız"
        elif sonuç <= 18.5  and 0 < sonuç:
            cevap = "Kilonuz çok düşük!!!"
        else:
            sonuç_label.config(text="")
            sonuç_label.config(text="Lütfen düzgün bir değer giriniz")
            sonuç_label.place(x=35, y=110)

        sonuç_label.config(text="")
        sonuç_label.config(text=cevap)
        sonuç_label.place(x=35,y=110)
    except ValueError:
        sonuç_label.config(text="")
        sonuç_label.config(text="Lütfen düzgün bir değer giriniz")
        sonuç_label.place(x=35, y=110)




button = tkinter.Button(text="Hesapla",command=index_hesapla)
button.place(x=35,y=90)


window.mainloop()

