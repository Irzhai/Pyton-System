import time
import sys
print("Welcome Rashiddows")
register_name = input("Adinizi qeyd edin:")
register_surname = input("Soyadinizi daxil edin:")
register_nickname = input("Istifadeci adinizi daxil edin:")
register_pass = input("Parolunuzu qeyd edin:")
register_security = int(input("4 reqemli guvenlik reqemini daxil edin:"))
length_security = len(str(register_security))
if length_security>4:
     print("4 reqemli eded daxil edin!!")
     sys.exit()
print("Adiniz:",register_name)
print("Soyadiniz",register_surname)
print("Istifadeci adiniz:",register_nickname)
print("Parolunuz:","*"*len(register_pass))
print("Qoruma reqemi","*"*4)
update = input("Deyisiklik etmek isteyirsiniz B(beli)/X(xeyr):")
if update == "B":
     security = int(input("4 reqemli guvenlik reqemi"))
     if security == register_security:
          update_name = input("Yeni Adinizi daxil edin:")
          update_surname = input("Yeni Soyadinizi daxil edin:")
          update_nickname = input("Yeni Nicknamenizi daxil edin:")
          register_name = update_name
          register_surname = update_surname
          register_nickname = update_nickname
          print("Adiniz:",update_name)
          print("Soyadiniz",update_surname)
          print("Istifadeci adiniz:",update_nickname)
     else:
          print("Daxil etdiyiniz Guvenlik reqemi Yanlisdir...")
          print("Lutfen Duzgun daxil edin...")
elif update == "X":
     print("Cox Sagolun,Sisteminiz Basladilir gozleyin.....")

print("Cenab",register_name,"Sisteminiz Basladilir")
time.sleep(2)
print("20")
time.sleep(1)
print("19")
time.sleep(1)
print("18")
time.sleep(1)
print("17")
time.sleep(1)
print("16")
time.sleep(1)
print("15")
time.sleep(1)
print("14")
time.sleep(1)
print("13")
time.sleep(1)
print("12")
time.sleep(1)
print("11")
time.sleep(1)
print("10")
time.sleep(1)
print("9")
time.sleep(1)
print("8")
time.sleep(1)
print("7")
time.sleep(1)
print("6")
time.sleep(1)
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
print("Sistem Basladilir...")
print('''
=====================================================
=              WELCOME RASHIDDOWS                   =                  
=                                                   =
=               1)Kalkulyator                       =             
=                                                   =
=               2)Is meseleleri                     =                           
=                                                   =
=               3)Hendese meseleri                  =                               
=                                                   =
=               4)Kompyuterle sohbet                =                                 
=                                                   =
=               5)Python Dersleri                   =                          
=                                                   =
=                                                   =
=              PYTHON OPERATING SYSTEM              =                                  
=                                                   =
=====================================================                                                   
''')
main = int(input('''
=====================================================
=              WELCOME RASHIDDOWS                   =                  
=                                                   =
=               1)Kalkulyator                       =             
=                                                   =
=               2)Is meseleleri                     =                           
=                                                   =
=               3)Hendese meseleri                  =                               
=                                                   =
=               4)Kompyuterle sohbet                =                                 
=                                                   =
=               5)Python Dersleri                   =                          
=                                                   =
=                                                   =
=              PYTHON OPERATING SYSTEM              =                                  
=                                                   =
=====================================================                                                   
'''))
if main == 1:
     print('''
=====================================================
=              WELCOME RASHIDDOWS                   =                  
=                                                   =
=               1)Kalkulyator                       =             
=               -           -                       =
=               -           -                       =                           
=               -           -                       =
=               -           -                       =                               
=               - --------- -                       =
=                                                   =                                 
=                                                   =
=                                                   =                          
=                                                   =
=                                                   =
=              PYTHON OPERATING SYSTEM              =                                  
=                                                   =
=====================================================                                                   
''')
     sual1 = input('''
=============================================================
=       Toplama == 1                                        = 
=       Cixma   == 2                                        =
=       Vurma   == 3                                        =
=       Bolme   == 4                                        =
=       Ededin %-in tapilmasi == 5                          =
=       Ededin quvvet ustunun tapilmasi == 6                =  
=       Bucagin Sinusunun tapilmasi == 7                    =
=       Bucagin Kosinusunun tapilmasi == 8                  =
=       Bucagin Tangensinin tapilmasi == 9                  =
=                                                           =
=                                                           =  
=============================================================
''')
     
