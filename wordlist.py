import itertools
import random
import string
import time

def ehtimollik_sozlar_yarat(data, min_len, max_len, max_sozlar, min_ehtimoliy=5000):
    sozlar = set()
    for r in range(2, min(len(data)+1, 6)):
        for perm in itertools.permutations(data, r):
            soz = ''.join(perm)
            if min_len <= len(soz) <= max_len and soz[0].isalpha():
                sozlar.add(soz)
            if len(sozlar) >= max_sozlar:
                return list(sozlar)
    if len(sozlar) < min_ehtimoliy:
        print(f"")
    return list(sozlar)

def random_soz_yarat(min_u, max_u, kerak_son, belgilar):
    sozlar = set()
    while len(sozlar) < kerak_son:
        uzunlik = random.randint(min_u, max_u)
        soz = random.choice(string.ascii_letters)
        soz += ''.join(random.choices(belgilar, k=uzunlik - 1))
        sozlar.add(soz)
    return list(sozlar)

print("\033[34mIsm kiriting: \033[0m", end="")
ism = input().strip().lower()
print("\033[34mFamiliya kiriting: \033[0m", end="")
familiya = input().strip().lower()
print("\033[34mTug'ilgan kun (masalan, 15): \033[0m", end="")
kun = input().strip()
print("\033[34mTug'ilgan oy (masalan, 07): \033[0m", end="")
oy = input().strip()
print("\033[34mTug'ilgan yil (masalan, 1995): \033[0m", end="")
yil = input().strip()
print("\033[34mMinimal kod uzunligi: \033[0m", end="")
min_uzunlik = int(input().strip())
print("\033[34mMaksimal kod uzunligi: \033[0m", end="")
maks_uzunlik = int(input().strip())
print("\033[34mKalit so'zlar (vergul bilan ajratib kiriting): \033[0m", end="")
kalit_sozlar = input().strip().replace(",", " ").split()
print("\033[34mMaksimal yoziladigan so'zlar soni: \033[0m", end="")
maks_sozlar = int(input().strip())


malumotlar = [ism, familiya, kun, oy, yil] + kalit_sozlar
belgilar = string.ascii_lowercase + string.digits + ''.join(kalit_sozlar)
belgilar = ''.join(sorted(set(belgilar)))

print("", end="", flush=True)
ehtimollar = ehtimollik_sozlar_yarat(malumotlar, min_uzunlik, maks_uzunlik, maks_sozlar)


qoldiq = maks_sozlar - len(ehtimollar)
if qoldiq > 0:
    print(f"")
    randomlar = random_soz_yarat(min_uzunlik, maks_uzunlik, qoldiq, belgilar)
    ehtimollar.extend(randomlar)


fayl_nomi = f"{ism}_{familiya}_wordlist.txt"
with open(fayl_nomi, "w") as f:
    for soz in ehtimollar:
        f.write(soz + "\n")

print(f"\n\033[32m✅ Tayyor! {len(ehtimollar)} ta so‘z '{fayl_nomi}' faylga yozildi.\033[0m")
