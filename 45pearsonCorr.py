import pandas as pd 
import pingouin as pg
import seaborn as sns 
import matplotlib.pyplot as plt 


data = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python ile Veri analizi\dondurma.xlsx")

normalityCheck = pg.normality(data)
print(normalityCheck)
"""
Normallik kontrolünde her iki değişken için de True değeri döndü Normalde burada ikisi false gelseydi veri sayıma bakardım merkezi limit
teoremine göre yeteri kadar verim olsaydı devam ederdim. Halihazırda True yani normallik testinden döndüğümüz ve değişkenlerimiz sürekli
olduğu için varsayımlarımızın ikisini tamamladık.
"""

sns.scatterplot(x="Sıcaklık",y="Dondurma Satış",data=data)
sns.lmplot(x="Sıcaklık",y="Dondurma Satış",data=data,ci=None) # doğru çizdirmek için de bunu kullanarak verilerimiz için bir 
# lineer line plot yaptık ve verilerimizin oluşturduğu çizgimiz bu şekilde. Düşük sıcaklıklarda sapmalar daha fazla gibi 
# Muhtemelen insanlar sıcaklığı çok farketmiyor :)


# SOnrasında yukarıdaki doğrusallık testleri vs. her şeyi gördük artık korelasyon testlerine geçebiliriz.

corrTest = pg.corr(x=data["Sıcaklık"],y=data["Dondurma Satış"],method='pearson')
print(corrTest)
"""
          n         r         CI95%     p-val     BF10     power
pearson  13  0.875714  [0.63, 0.96]  0.000087  318.018  0.992615

Buna göre p-val <0.05 yani H0 hipotezini reddediyoruz burada ilişkinin var olduğuna dair r=0.875714 lük güçte bir güçlü ilişkinin olduğunu
istatistiki olarak Sıcaklık ile Dondurma satışları arasında bir korelasyon mevcuttur deriz.
"""

data2 = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python ile Veri analizi\spearman.xlsx")

normalityCheck2 = pg.normality(data2)
print(normalityCheck2)
"""
          W      pval  normal
A  0.968391  0.869842    True
B  0.792429  0.007479   False

Burada normallik testlerinde B grubu normal olarak dağılmadığı ortaya çıktı bir de doğrusallık testi yapalım
"""

sns.lmplot(x="A",y="B",data=data2)
# Doğrusallık olmadığı görülmekte ama bir nmonotic durum gözleniyor 
# Hem monotonic hem de non-linear durum olduğu için spearman a geçebiliriz.

corrTest2 = pg.corr(x=data2["A"],y=data2["B"],method='spearman')
print(corrTest2)
"""
           n         r           CI95%     p-val     power
spearman  11 -0.918182  [-0.98, -0.71]  0.000067  0.995623
Test sonuçlarına göre 0.91 güçlü bir ilişki varmış ve bu ilişki negatifmiş
p-val değeri 0.0000067<0.05 olduğu için H0 hipotezini reddetmiş olduk
"""