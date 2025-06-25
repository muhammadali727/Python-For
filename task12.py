n = int(input("Son kiriting: "))
juft_yigindi = 0
toq_yigindi = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        juft_yigindi += i
    else:
        toq_yigindi += i

print("Juft yig‘indi:", juft_yigindi)
print("Toq yig‘indi:", toq_yigindi)