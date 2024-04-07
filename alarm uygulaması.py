import tkinter as tk
import datetime 
import winsound
import time



pencere=tk.Tk()
pencere.title("alarm")

def merkez_ekran( pencere,genişlik,uzunluk):
    ekranx=pencere.winfo_screenwidth()
    ekrany=pencere.winfo_screenheight()
    x=(ekranx-genişlik)/2
    y=(ekrany-uzunluk)/2
    pencere.geometry(f"{genişlik}x{uzunluk}+{int(x)}+{int(y)}")

merkez_ekran(pencere,450,450)

def zamanigoster():
    
       simdiki_zaman=datetime.datetime.now().time()
       la.config(
           text=simdiki_zaman
        )
       pencere.after(10,zamanigoster)
def yazı_efekt():
       if alarmlabel.cget("foreground") == "red":
           alarmlabel.config(foreground="blue")
       else:
          alarmlabel.config(foreground="red")
    
       pencere.after(100, yazı_efekt)

def ses_efekt():
    frequency = 500 
    duration = 1000 
    winsound.Beep(frequency, duration) 
      


def zilcal( ): 
    ses_efekt()
    pencere.after(100, yazı_efekt)

    a=saat.get()
    b=dakika.get()
    c=saniye.get()

    alarmzamanı=datetime.time(int(a),int(b),int(c))
    simdizaman=datetime.datetime.now().time() 
    while simdizaman<alarmzamanı:  
        simdizaman=datetime.datetime.now().time()
 
   

la=tk.Label(
    pencere,
    width=15,
    height=2,
    font="Helvetica 24",
    wraplength=300,
    bg="white",
    fg="black",
    
)

la.pack()
la.place(x=80,y=30)

alarmlabel=tk.Label(
    pencere,
    width=10,
    height=2,
    text="Alarm",
    foreground="red",
    font="Helvetica 24",
    wraplength=300,
    bg="white",
    fg="black",
)
alarmlabel.pack()
alarmlabel.place(x=130,y=120)

zamanbuton=tk.Button(
    pencere,
    text="Zamanı Göster",
    width=12,
    height=2,
    background="white",
    foreground="black",
    font="ariel 16",
    cursor="hand2",
    command= zamanigoster
    

)
zamanbuton.pack()
zamanbuton.place(x=50,y=375)

alarmbuton=tk.Button(
    pencere,
    text="Alarm Kur",
    width=12,
    height=2,
    background="white",
    foreground="black",
    font="ariel 16",
    cursor="hand2",
    command= zilcal
)
alarmbuton.pack()
alarmbuton.place(x=250,y=375)


saat=tk.Entry(
     pencere,
     width=13,
     background="white"
)
saat.pack()
saat.place(x=50,y=275)

saatkur=tk.Label(
    pencere,
    width=4,
    height=1,
    text="Saat",
    font="Helvetica 16",
    wraplength=50,
    bg="white",
    fg="black",
    
)

saatkur.pack()
saatkur.place(x=65,y=230)



dakika=tk.Entry(
     pencere,
     width=15,
     background="white"
)
dakika.pack()
dakika.place(x=185,y=275)

dakikakur=tk.Label(
    pencere,
    width=5,
    height=1,
    text="Dakika",
    font="Helvetica 16",
    wraplength=100,
    bg="white",
    fg="black",
    
)

dakikakur.pack()
dakikakur.place(x=200,y=230)


saniye=tk.Entry(
     pencere,
     width=15,
     background="white"
)
saniye.pack()
saniye.place(x=330,y=275)

saniyekur=tk.Label(
    pencere,
    width=5,
    height=1,
    text="Saniye",
    font="Helvetica 16",
    wraplength=100,
    bg="white",
    fg="black",
    
)

saniyekur.pack()
saniyekur.place(x=340,y=230)



pencere.mainloop()






