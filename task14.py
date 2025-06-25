yoshlar = input("Yoshlarni kiriting: ").split()
jami = 0 
for y in yoshlar: 
    jami += int(y)

ortacha = jami / len(yoshlar)
print("O‘rtacha yosh:", ortacha)