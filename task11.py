sonlar = input("Sonlarni vergul bilan kiriting: ").split(',')
kichik = float(sonlar[0])
katta = float(sonlar[0])

for s in sonlar:
    s = float(s)
    if s < kichik:
        kichik = s
    if s > katta:
        katta = s

ortalama = (kichik + katta) / 2
print("O‘rtacha:", ortalama)