fonk1 = input("fonksiyonu giriniz:")
türev1 = input("fonksiyonun türevini giriniz:")
x1 = float(input("başlangıç değerini giriniz:"))
tolerans = float(input("hata toleransını giriniz:"))  

def NewtonRaphson(fonk, türev, x, tol):
    iterasyon = 0
    def f(x):
        f = eval(fonk) 
        return f
    
    def df(x):
        df = eval(türev)
        return df
    
    while True:
        i = x - (f(x) / df(x))   #Newton Raphson metodunun formülü
        print(f'{iterasyon}. iterasyon sonucu = {i}')
        if abs(f(i)) < tol:  
            break
        x = i
        iterasyon += 1
    
    print(f'kök {iterasyon} iterasyondan sonra {x} olarak bulundu.')

NewtonRaphson(fonk1, türev1, x1, tolerans)