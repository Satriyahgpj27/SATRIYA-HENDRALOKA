#import library
import time
import math

#scoring
nilaiBahasaIndonesia = int(input("masukkan nilai bahasa indonesia anda disini"))
time.sleep(1)
if(nilaiBahasaIndonesia>0) and (nilaiBahasaIndonesia<100): 
    if(nilaiBahasaIndonesia < 60):
        print("anda tidak lulus")
    elif(nilaiBahasaIndonesia >= 60):
        print("anda Lulus")
else:(nilaiBahasaIndonesia < 0) print('invalid')
    
time.sleep(2)

nilaiIPA = int(input("masukkan nilai IPA anda disini"))
time.sleep(1)
if(nilaiIPA>0) and (nilaiIPA<100):
    if(nilaiIPA < 60):
        print("anda tidak lulus")
    elif(nilaiIPA >= 60):
        print("anda Lulus")
else:(nilaiIPA < 0)
print('invalid')

time.sleep(2)

nilaiMatematika = int(input("masukkan nilai Matematika anda disini"))
time.sleep(1)
if(nilaiMatematika>0) and (nilaiMatematika<100):
    if(nilaiMatematika < 70):
        print("anda tidak lulus")
    elif(nilaiMatematika >= 70):
        print("anda Lulus")
else:(nilaiMatematika < 0)
print('invalid')
