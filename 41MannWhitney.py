import pandas as pd 
import pingouin as pg 

data = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python ile Veri analizi\gender_duration_data.xlsx")

print(data)

nomalityCheck = pg.normality(data=data,dv="Süre",group="Cinsiyet")
print(nomalityCheck)

# ikiside pvalue olarak 0.05 ten büyük olduğu için H0 hipotezimiz doğru imiş yani bunlar normal dağılıma uyuyor normalde 
# bağımsız iki örneklem t testi kullanmak gerek ama ben mann whitney görmek için bu şekilde ilerliyorum.

# ilk olarak bağımsız değişkenlerimi iki farklı değişkende tutmak istiyorum 
erkek = data[data["Cinsiyet"] == "Erkek"]["Süre"]
kadın = data[data["Cinsiyet"] == "Kadın"]["Süre"]

# hipotezlerimin durumuna göre gözlem gruplarımı erkek ve kadın olarak ayırarak verdim ve sonrasında alternative olarak two sided yani muErkek != muKadın 
# olduğunu hipotize ederek verdim
test = pg.mwu(erkek,kadın,alternative="two-sided")
print(test)

"""
     U-val alternative     p-val   RBC   CLES
MWU   31.5   two-sided  0.170042 -0.37  0.315
Test sonuçlarımız geldi p değeri olarak 0.17 yani 0.05 ten büyük bir değer geldi bu da demektir ki H0 hipotezimizi red edemiyorum
Yani buradan çıkarılacak sonuç şudur ki Örnek vermek gerekirse bu bir telefon konuşması olsaydı kadınların ve erkeklerin 
müşteri hizmetlerini aradığında ortalama olarak geçirdikleri süre aynıdır yorumunu yaparız aynı demekten ziyade istatistiki bir farklılık 
yüzde 95 güvenle görülmemektedir diyebiliriz.
"""

################## WİLCOXON T TESTİ #########################
data2 = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python ile Veri analizi\wcx.xlsx")

#veri adedinin azlığından dolayı burada bağımlı örneklem t testini uygulamak yerine Wilcoxon t testini seçiyorum 

# buna göre gözlem çiftleri arasındaki farkı hesap etmem gerekiyor. 
fark = data2["Önceki Puan"] - data2["Sonraki Puan"]
# yazdırarak fark değişkenini görelim nasıl bir veri elimize gelmiş
print(fark)

# Normal dağılım gösterip göstermediğini kontrol edelim
normalityCheck2 = pg.normality(fark)
print(normalityCheck2)
"""
          W     pval  normal
0  0.684029  0.00647   False
Burada normal dağılım göstermediği pval<0.05 ten ayrıca False dönen normal sütunundan anlaşılıyor. Bu da Wilcoxon t testini seçimimizin doğru
olduğunu gösteriyor.
"""

test2 = pg.wilcoxon(x = data2["Önceki Puan"],y = data2["Sonraki Puan"],alternative="two-sided")
print(test2)
"""
          W-val alternative   p-val  RBC  CLES
Wilcoxon    0.0   two-sided  0.0625 -1.0  0.34
Buna göre çıkan sonuçta pval > 0.05 ten olduğu için öğrencilerin küçükte olsa bir farklılık olduğu görünüyor. 
Örnek vermek gerekirse mesela seçilen 6 öğrenci üzerinden rehberlik hocalarının uyguladığı psikolojik destek etüdünün 
etkisinin ortalama da oluşan küçük farklılık olduğunu görerek az da olsa işe yaradığını söyleyebiliriz. Burada farklı denemeler ve işlemler 
yapılarak eğitim sürecinin optimizasyonunu bulmamız olasıdır.
"""