import pandas as pd 
import pingouin as pg 

data = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python ile Veri analizi\partialCorr.xlsx")

corr = pg.pairwise_corr(data)
print(corr)
"""
      X     Y   method alternative   n         r           CI95%         p-unc       BF10  power
0  Kilo  Öğün  pearson   two-sided  28  0.956793    [0.91, 0.98]  1.820860e-15  2.058e+12    1.0
1  Kilo   Yaş  pearson   two-sided  28 -0.979502  [-0.99, -0.96]  1.276551e-19   1.39e+16    1.0
2  Öğün   Yaş  pearson   two-sided  28 -0.944941  [-0.97, -0.88]  3.977192e-14  1.202e+11    1.0

Buna göre kilo ile öğün arasında pozitif güçlü bir ilişki korelasyon var iken 
kilo-yaş ve öğün-yaş arasında negatif güçlü bir ilişki korelasyon var imiş 
ve p değerlerine baktığımız da bunların hepsi çok küçük sayılar 0.05 de çok küçük yani h0 reddedilir 
Hipotezler:
Null Hipotezi (𝐻0): İki değişken arasında kısmi bir ilişki yoktur (korelasyon katsayısı = 0), diğer değişkenler kontrol edildiğinde.
Alternatif Hipotez (𝐻1): İki değişken arasında kısmi bir ilişki vardır (korelasyon katsayısı ≠ 0), diğer değişkenler kontrol edildiğinde.
Verilen Çıktıyı Yorumlama:
p-unc Değeri:
p-unc değeri, null hipotezinin doğruluğunu sınar. Eğer p-unc değeri bir önceden belirlenmiş anlamlılık düzeyinden (genelde 𝛼=0.05α=0.05) küçükse,
 null hipotezi reddedilir.Bu, iki değişken arasında kontrol edilen değişken(ler)den bağımsız bir ilişki olduğunu gösterir.

 
Asıl bakmamız gereken yer neresi yani neyi inceliyoruz. Burada bağımlı ve bağımsız değişkenleri iyi seçmek gerekiyor. Yani kilo arttıkça
mı öğün artar yoksa öğün arttıkça mı kilo artar buna karar vermemiz gerekiyor.  
Mantıklıca düşününce kiloyu elimizle ayarlammıyoruz hiç bir şekilde ayarlayamıyorum ama öğünü istediğimiz gibi ayarlayabiliriz o yüzden 
öğün bağımsız bir değişkendir ve yediğimiz öğün sayısına göre kilomuz da ortaya çıkan sonuç gibi olur yani bağımlı değişken olur.
Kilo = y, Öğün = x => Y=x gibi bir denklem ortaya çıkmış olur.
"""
partialCorr = pg.partial_corr(data=data,x="Öğün",y="Kilo",covar="Yaş") 

"""
Aynen yukarıda koyduğumuz denklem gibi verdik. x bizim bağımsız değişkenimiz dedik ve x e onu verdik y ye de bağımlı değişkeni verdik. 
Covar = Yaş diyerek yaş'ın etkisini elimine etmeye çalışıyoruz.
"""
print(partialCorr)

"""
          n         r         CI95%     p-val
pearson  28  0.473648  [0.11, 0.72]  0.012574
İşte yüzde 90 ı geçkin bir ilişki var iken şimdi 0.47 lik bir ilişki var. Yaşın etkisi ortadan kalkınca gerçek korelasyon diyebileceğimiz 
etki ortaya çıkmış oldu
"""
