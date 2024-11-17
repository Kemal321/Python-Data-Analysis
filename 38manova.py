import pandas as pd
import pingouin as pg
from statsmodels.multivariate.manova import MANOVA # manovayı bu şekilde import edeceğiz

data = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python ile Veri analizi\manovadataset.xlsx")

# Şimdi manova da 1++ bağımsız değişken olduğunu söyledik burada amacımız bağımsız değişkenlerin bağımlı değişkenler üzerindeki
# etkisini test etmek. 

# Ek olarak normallik testine gerek yok çünkü n>20 zaten MLT ye göre normal dağılım olarak görüp varsayalım


# homojelik testi yapacağız ama burada pd.melt yapmadık çünkü verilerimiz zaten long formatına uygun şekilde oluşmuş yani 
# long olan bir şeyi tekrar long yapamayız gerek de yok zaten.
homojenlik  = pg.homoscedasticity(data = data, dv = "ErkekTutum",group="Ürün",center="mean") 
print(homojenlik) 

"""               W      pval  equal_var
levene  0.495013  0.612159       True
PVAL değerimiz 0.05 den büyük geldi yani varyans homojenliğimiz sıkıntılı ama ben ilerleyeceğim 
"""

varcovar = pg.box_m(data,dvs=["ErkekTutum","KadınTutum"],group="Ürün")
print(varcovar)

# Burada da aynı şekilde pval değeri veriyor zaten yorumlaması belli bunu yaparken de Chi Squ tablosundan yararlanıyor
# Varyans-Covaryans matrisi eşitliği manova için çok önemli varsayımlardan biridir o yüzden burası iyi gelmeli bu örnekte 
# bu örnekte 0.005439  bulduk 0.05 ten küçük o yüzden bizim için yeterli manovaya ilerleyebiliriz.

# daha önce anova da olduğu gibi burada da model üzerinden çalışacağız.


model = MANOVA.from_formula("ErkekTutum+KadınTutum~Ürün",data=data)

print(model.mv_test())
"""
Burada bakmamız gereken şey Pr > F değeri 0.0000 çıktı buna göre kişilerin cinsiyetlerinin ürün üzerindeki tutumlarının farklılığı var.
Yani anlamlılık var 0.05 ten çok küçük
"""
 
# post hoc a ilerleyebiliriz.
posthoc1 = pg.pairwise_tukey(data=data,dv="ErkekTutum",between="Ürün")
posthoc2 = pg.pairwise_tukey(data=data,dv="KadınTutum",between="Ürün")
print(posthoc1)
print(posthoc2)
"""
Burada da p-tukey değerlerine baktığımız da Tukey testinden çıkan p value ler 0.05 ten küçük çıkmalı erkeklerde 
1.ürün ve 2.ürün arasında p değeri 0.808 imiş Bu da, bu iki grup arasında anlamlı bir fark olmadığını gösterir.
aynı şekilde 2.ürün ile 3.ürün arasında da böyle bir durum mevcut:
"""