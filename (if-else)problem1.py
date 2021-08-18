#Problem 1
 
kilo = int(input("Kilonuzu giriniz: "))

boy = float(input("Boyunuz giriniz (m): "))

BKI = kilo/(boy*boy)

if BKI < 18.5:
    
    print("Zayıf")
    
if 25 > BKI > 18.5:
    
    print("Normal")
    
if 25 < BKI < 30:
    
    print("Fazla kilolu")
    
if BKI > 30:
    
    print("Obez")