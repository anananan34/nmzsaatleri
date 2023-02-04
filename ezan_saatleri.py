import requests
from bs4 import BeautifulSoup as bs
from colorama import *
init(autoreset=True)


sayfa = requests.get("https://namazvakitleri.diyanet.gov.tr/tr-TR/9773/fatsa-icin-namaz-vakti")


sayfa_kaynak = bs(sayfa.content,"lxml")

#takvimler
miladi_takvim = sayfa_kaynak.find("div",attrs={"class":"ti-miladi"}).text 
#print(miladi_takvim)
hicri_takvim = sayfa_kaynak.find("div" , attrs={"class":"ti-hicri"}).text 
#print(hicri_takvim)

#namaz saatleri

imsak = sayfa_kaynak.find("div" , attrs={"data-vakit-name":"imsak"}).text 
#print(imsak)
gunes = sayfa_kaynak.find("div",attrs={"data-vakit-name":"gunes"}).text
#print(gunes)
ogle = sayfa_kaynak.find("div",attrs={"data-vakit-name":"ogle"}).text
#print(ogle)
ikindi = sayfa_kaynak.find("div",attrs={"data-vakit-name":"ikindi"}).text
#print(ikindi)
aksam = sayfa_kaynak.find("div",attrs={"data-vakit-name":"aksam"}).text
#print(aksam)
yatsi = sayfa_kaynak.find("div",attrs={"data-vakit-name":"yatsi"}).text
#print(yatsi)

banner = Back.LIGHTWHITE_EX+Fore.GREEN


uzunluk = len(" |     "+miladi_takvim+"         | ")
uzunluk = uzunluk -4
good = "-"* uzunluk

print(Back.LIGHTWHITE_EX+Fore.GREEN+" +"+good+"+ ")
print(banner+" |     "+miladi_takvim+"         | ")
print(Back.LIGHTWHITE_EX+Fore.GREEN+" +"+good+"+ ")
print(Style.RESET_ALL)

#namaz saatleri düzenlenmiş çıktı
print(banner+" +          Imsak Vakti          + ")
print(" "+imsak)

print(banner+" +          Güneş Doğuşu         + ")
print(" "+gunes)

print(banner+" +          Öğle Vakti           + ")
print(" "+ogle)

print(banner+" +          Ikindi Vakti         + ")
print(" "+ikindi)

print(banner+" +          Akşam Vakti          + ")
print(" "+aksam)

print(banner+" +          Yatsı Vakti          + ")
print(" "+yatsi)
