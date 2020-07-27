num = 0
sum = 0
nr_input = 0
av_value = 0

print("")
print("Introduceti cate un numar pozitiv intreg (pentru iesire tastati orice litera)")
print("*numerele negative si numerele zecimale vor fi excluse din calcul")

while num >= 0:
    try:
        num = int(input("VALOARE >>> "))
        if num >= 0:
            sum += num
            nr_input += 1
            av_value = sum / nr_input
        else:
            print("Eroare. Introduceti un numar pozitiv intreg!!!")
    except ValueError:
        num = -1

print("Suma numerelor introduse este: ", sum)
print("Au fost introduse " + str(nr_input) + " valori")
print("Media aritmetica a valorilor introduse: " + str(int(av_value)))
print("Media aritmetica (cu virgula) a valorilor introduse: " + str(round(av_value, 2)))
