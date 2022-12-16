#Program konversi celcius ke satuan lain

print("\n PROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukan suhu dalam celcius : "))
print("Suhu Adalah : ", celcius)

#Reamur

reamur = (4/5) * celcius
print("Suhu dalam Reamur  : ", reamur, "Reamur")

#Fahrenheit

fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam Fahrenheit : ", fahrenheit, "Fahrenheit")

#Kelvin

kelvin = celcius + 273
print("Suhu dalam Kelvin :", kelvin, "Kelvin")


# Konversi Temperatur Reamur Ke satuan lain

print("==== REAMUR ====")

reamur = float(input("Masukan suhu dalam Reamur : "))
print("Suhu adalah : ", reamur)

#Reamur To Celcius
celcius = (5/4) * reamur
print("Suhu dalam celcius adalah :", celcius, "C")

#Reamur To Fahrenheit
fahrenheit = ((9/4) * reamur) + 32
print("Suhu dalam Fahrenheit :", fahrenheit, "F")

#Reamur To Kelvin
kelvin = ((5/4) * reamur) + 273
print("Suhu dalam Kelvin :", kelvin, "K")


print("==== FAHRENHEIT ====")

fahrenheit = float(input("Masukan Suhu Dalam Fahrenheit : "))
print("Suhu adalah :", fahrenheit, "F")

#Fahrenheit To Celcius
celcius = (fahrenheit - 32) * 5/9
print("Suhu dalam Celcius :", celcius, "C")

#Fahrenheit To Reamur
reamur = (fahrenheit - 32) * 4/9
print("Suhu dalam Reamur :", reamur, "R")

#Fahrenheit To Kelvin
celcius = (fahrenheit - 32) * 5/9
kelvin = celcius + 273
print("Suhu dalam Kelvin:", kelvin, "K")



print("==== KELVIN ====")

kelvin = float(input("Masukan Suhu dalam Kelvin  :"))
print("Suhu Adalah :", kelvin)

#Kelvin To Celcius
celcius = kelvin - 273
print("Suhu dalam celcius adalah :", celcius, "C")

#Kelvin To Reamur
reamur = (kelvin - 273 ) * 4/5
print("Suhu dalam Reamur adalah :", reamur, "R")

#Kelvin To Fahrenheit
celcius = kelvin - 273
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah :", fahrenheit, "F")




