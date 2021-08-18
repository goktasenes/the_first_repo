#Problem 3

vize1 = int(input("Vize 1 sonucunu giriniz: "))
vize2 = int(input("Vize 2 sonucunu giriniz: "))
final = int(input("Final sonucunu giriniz: "))

toplam_not = (vize1*3 + vize2*3 + final*4)/10

print("")

if toplam_not >= 90:
    
    print("Harf notu: AA" )
    
elif toplam_not >= 85:
    
    print("Harf notu: BA" )
    
elif toplam_not >= 80:
    
    print("Harf notu: BB" )
    
elif toplam_not >= 75:
    
    print("Harf notu: CB" )
    
elif toplam_not >= 70:
    
    print("Harf notu: CC" )
    
elif toplam_not >= 65:
    
    print("Harf notu: DC" )
    
elif toplam_not >= 60:
    
    print("Harf notu: DD" )
    
elif toplam_not >= 55:
    
    print("Harf notu: FD" )
    
else:
    
    print("Harf notu: FF" )


