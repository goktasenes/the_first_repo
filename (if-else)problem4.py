#Problem 4

sual = input("Üçgen mi dörtgen mi bulmak istersiniz? : ")

#Dörtgenin açılarını bilmeden kare yahut dikdörtgen olduğunu anlayamayız.

'''if sual.lower() == "dörtgen": 
    
    kenar1 = int(input("Birinci kenarı giriniz: "))
    kenar2 = int(input("İkinci kenarı giriniz: "))
    kenar3 = int(input("Üçüncü kenarı giriniz: "))
    kenar4 = int(input("Dördüncü kenarı giriniz: "))''' 
    
    
    
if sual.lower() == "üçgen":
    
    kenar1 = int(input("Birinci kenarı giriniz: "))
    kenar2 = int(input("İkinci kenarı giriniz: "))
    kenar3 = int(input("Üçüncü kenarı giriniz: "))
    
    if not abs(kenar1-kenar2) < kenar3 < kenar1+kenar2:
        
        print("Girdiğiniz değerler bir üçgen belirtmiyor!!!")
    
    elif not abs(kenar2-kenar3) < kenar1 < kenar3+kenar2:
        
        print("Girdiğiniz değerler bir üçgen belirtmiyor!!!")

    elif not abs(kenar1-kenar3) < kenar2 < kenar1+kenar3:
        
        print("Girdiğiniz değerler bir üçgen belirtmiyor!!!")

    else:
        
        if kenar1 == kenar2 == kenar3:
        
            print("Üçgen tipi: Eşkenar üçgen")
        
        elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3:
        
            print("Üçgen tipi: İkizkenar üçgen")
        
        else:
        
            print("Sıradan üçgen")
        
    
    

