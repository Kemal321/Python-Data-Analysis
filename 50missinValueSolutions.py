"""""""""""""""""""""""""""""""""""""""""""""""EKSİK VERİ ÇÖZÜMLERİ GİRİŞ"""""""""""""""""""""""""""""""""""""""""""""""""""""
import pandas as pd 
import missingno as msno 
import matplotlib.pyplot as plt 

data = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python ile Veri analizi\nullDataExercise.xlsx")

data2= data.copy()
print(data2.isnull().sum()) # kaç tane eksik gözlem var 

# en çok kaçınmamız gereken yöntemi görerek başlayalım. Satır silme işlemi.
data3 = data2.dropna()
print(data3.isnull().sum())
"""
D1    5  -> D1    0  >> Diğer satılardakiler de bu şekilde silinmiş oldu.
data3 e attık çünkü aldığı inplace parametresi varsayılan olrak bu değişikliği kalıcı olmayacak şekilde
ayarlanmış bir şeydir. Karar verdiğinizde True olarak gönderirisek oluşmuş olur.
"""
# verileri sildikten sonra ona göre bir indeksleme yapmaız gerekebilir bu durumu nasıl yaparız.
print(data3) # son ->  33  29.30  29.53  28.21  29.99
data3.reset_index(drop=True,inplace=True)
print(data3) # son -> 15  29.30  29.53  28.21  29.99

# dropna çalışma mantığında en az 1 tane null değer var ise siler bunun yerine tüm satırı boş olan değerleri silmek istersek bunun için 
# how adında bir parametre alır buna how="all" yaparsak tüm sütunları boş olan satırı siler.
data4 = data2.dropna(how="all") # zaten any ve all olmak üzre 2 tane var :)
data4.reset_index(drop=True,inplace=True)
print(data4) # son -> 33  29.30  29.53  28.21  29.99  -->> Aynı anda 4 sütunu boş değer yokmuş demek ki ilk çıktı ile aynı sayıda veri döndürdü

"""
Bazen tüm sütunu silmek isteyebileceğimiz durumlar olabilir mesela bir sütunun çoğu değeri nan diyelim bu oranın yüzde 70 75 olması ile ilgili 
fikirler mevcut böyle zamanlar satırları silerek veri kaybetmek yerine o sütundan kurtulmak daha mantıklı gelebilir. Bunun için dropna() fonksiyonu
na axis parametresini 1 gönderirsek axis=1 diyerek sütun bazlı çalışma yapar. axis=0 default tur.
"""
data5 = data2.dropna(axis=1)
print(data5)
# Columns: [] -> çıktıya bakılırsa boş döndü yani sütun kalmamış bu ne demek hepsini taradım her sütunda en az 1 tane vardı bende o sütunu yok ettim
# diyor buna göre :D veri kalmadı lkjghldkşfgjhflkgdhşl 
data6 = data2.dropna(axis=1,how="all") # tamamı dolu olanları sil dedik 
print(data6) # 33  29.30  29.53  28.21  29.99 dümdüz tüm veriyi döndürdü yani silmemiş eleman demek ki tamamı nan olan yok.

# ileri metodları bilmiyoruz ama bazı basit ortalama medya vs. gibi doldurmaları görerek başlayabiliriz
data7 = data2.copy()
print(data7.fillna(value=data7.median(),inplace=False)) # burada value yerine her hangi bir şey koyabiliriz. Mesela string ifade veya 0 veya verinin medyanı ortalaması modu vs. vs. 
print(data7.fillna(value=data7.mode(),inplace=False))
print(data7.fillna(value=data7.mean(),inplace=False))
print(data7.fillna(value="Eksik gözlem",inplace=False))

# veya mesela bir sütundaki eksik değerler için daha önce kategorik bir karşılık veya ilişkili yapı var ise o kategorinin kendi örneklemleri 
# kullanılmalı demiştik. Bizim örneğimiz de  de D1 sütunundaki NaN ları o sütunun kendi ortalaması ile dolduralım mesela
print(data7["D1"].fillna(value=data7["D1"].mean(),inplace=True)) # işte bu şekilde aslında serilerin birleşimi olduğu için oralarda da aynı şekilde mantık
# yani mantıklı olduğu sürece bir sürü şey yapılabilir. O yüzden kendinizi ezbere kasıntıya vermeyin yapıların çalışma prensiplerini anlamaya çalışın

data8 = data2.copy()
# veya hesaplamaya kısmi bir bölümü dahil edecek olursak.
print(data8.fillna(value=data7.mean()["D1":"D3"],inplace=False),data8.mean()["D1":"D2"])
# buranın da mantığı belli zaten mean ile hesaplama sonucu ortaya çıkan değer yine bir seri olacak çünkü 4 sütun var 
# fakat sütunlara göre long formata dönüştürülecek çünkü 4 sütun varken 33 tane değer satırı var Bu durumda D1 D2 D3 D4 şeklinde long yani bunları 
# referans alan bir indeksleme yapılacak bu durumda "D1":"D3" dediğimiz için onları dolduracak diğer sütunu boşverecek.
# bunu yaparken her sütunu kendi ortalaması ile dolduracak tabi ki bunu da unutmamak lazım.
# buna göre tamamını kendisi için doldurmak istersek [:] -> bu yapıyı kullanacağız bu kadar 
print(data8.fillna(value=data8.mean()[:],inplace=False))

# yine aynı mantık ile mod ve medyan ile de aynı şeyleri yapabiliriz. 
# medyan ortalama hangisi ne zaman kullanılacak bunu zaten biliyoruz. çarpıklık düşük ise ortalama fazla ise std si fazla ise yani medyan kullanılabilir



