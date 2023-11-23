import math

# Balok
def luas_balok(panjang, lebar, tinggi):
    value = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    return value

def volume_balok(panjang, lebar, tinggi):
    value = panjang * lebar * tinggi
    return value
    
# Bola
def luas_bola(jari_jari):
    value = 4 * math.pi * jari_jari ** 2
    return value

def volume_bola(jari_jari):
    value = (4/3) * math.pi * jari_jari ** 3
    return value

# Kerucut
def luas_kerucut(jari_jari, tinggi):
    value = math.pi * jari_jari * (jari_jari + math.sqrt(jari_jari**2 + tinggi**2))
    return value

def volume_kerucut(jari_jari, tinggi):
    value = (1/3) * math.pi * jari_jari**2 * tinggi
    return value

# Kubus
def luas_kubus(sisi):
    value = 6 * sisi**2
    return value

def volume_kubus(sisi):
    value = sisi**3
    return value

# Limas Segiempat
def luas_limas_segiempat(panjang, lebar, tinggi_limas):
    value = panjang * lebar + 2 * (panjang * tinggi_limas / 2) + 2 * (lebar * tinggi_limas / 2)
    return value

def volume_limas_segiempat(panjang, lebar, tinggi):
    value = (1/3) * panjang * lebar * tinggi
    return value

# Limas Segitiga
def luas_limas_segitiga(panjang_alas, tinggi_segitiga, tinggi_limas):
    value = (panjang_alas * tinggi_segitiga) + (3 * (1 / 2) * panjang_alas * tinggi_limas)
    return value

def volume_limas_segitiga(panjang_alas, tinggi_segitiga, tinggi_limas):
    value = (1 / 3) * (1 / 2) * panjang_alas * tinggi_segitiga * tinggi_limas
    return value

# Prisma Segitiga
def luas_segitiga_prisma(alas_segitiga, tinggi_segitiga):
    value = 0.5 * alas_segitiga * tinggi_segitiga
    return value

def luas_permukaan_prisma_segitiga(alas_segitiga, tinggi_segitiga, tinggi_prisma):
    value = 2 * alas_segitiga * tinggi_segitiga + 3 * alas_segitiga * tinggi_prisma
    return value

def volume_prisma_segitiga(alas_segitiga, tinggi_segitiga, tinggi_prisma):
    luas_segitiga = 0.5 * alas_segitiga * tinggi_segitiga
    value = luas_segitiga * tinggi_prisma
    return value

# Tabung
def luas_tabung(jari_jari, tinggi):
    value = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    return value

def volume_tabung(jari_jari, tinggi):
    value = math.pi * jari_jari**2 * tinggi
    return value