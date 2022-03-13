saniye = int(input('saniyeha: '))
saat = saniye // 3600
daghigheh =(saniye % saat)// 60
saniye = saniye - saat*3600 - daghigheh*60
print(int(saat) ,":",int(daghigheh),":",int(saniye))