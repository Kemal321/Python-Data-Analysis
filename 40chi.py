import pandas as pd
from scipy import stats
import numpy as np

data = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python ile Veri analizi\chi2x2.xlsx")

# eğer 2 değişken üzerinden frekans tablosu yapmam lazım ise eğer bu noktada crosstab denilen bir fonksiyonu kullanmamız lazım
# geçen sefer value_counts yapmıştık bu sefer cross_tab yapacağız 
table = pd.crosstab(index=data["Cinsiyet"],columns=data["Kol"])   
print(table)

"""
Hangi testi kullanacağımız beklenen değer üzerinden bakıldığı için beklenen frekansları bulmamız lazım
"""
test, pval, df,beklenen = stats.chi2_contingency(table)
print(beklenen) # 4 farklı değer döndürüyor ama biz ilk olarak beklenen bakacağız testi belirlemek için 
print(beklenen.min()) # bu şekilde en küçüğü direktmen alabiliriz. Buna göre 6.505050505050505 imiş buna göre Yates Chi squ kullanmamız gerekiyor

# yine de hepsini görelim 
"""Pearson Chi Squ testleri"""
test2, pval2, df2,beklenen2 = stats.chi2_contingency(table,correction=False) # aslında aynı şekilde yapacağız. correction = False yaparsak pearson
# yapacak True yaparsak Yatesin testini uygulayacaktır. 

print("Pearson Sonucu: ",test2,pval2)
# Pearson Sonucu:  0.7575775018785202 0.38408770206353904 p değerimiz 0.05 ten büyük olduğu için H0 reddedilemez
# Yani elimizdeki cinsiyet ve kol arasında bir ilişki yoktur.Normalde 25 den büyük iken kullanmak lazım tabi


test3, pval3, df3,beklenen3 = stats.chi2_contingency(table,correction=True) # yates olunca true olmuş oluyor 
print("Yates in Sonucu: ",test3,pval3)# Yates in Sonucu:  0.33783192932628353 0.5610833547072969
# bu sonuçlara göre yüzde 95 güven ile cinsiyet ile kol arasında her hangi bir ilişki yoktur.


# fisher dayı farklı 
test4 = stats.fisher_exact(table=table)
print("Fisher in Sonucu: ",test4.pvalue) # Fisher in Sonucu:  0.5644171650896102 Buna göre yine aynı şekilde H0 reddedilemez


"""""""""""""""""""""""""""""""""""""""RxC Tablosu Bağımsızlık Testkleri"""""""""""""""""""""""""""""""""""""""
data2 = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python ile Veri analizi\chirxc.xlsx")

table2 = pd.crosstab(index=data2["Cinsiyet"],columns=data2["Marka"])
print(table2)

test,pval,df,expected = stats.chi2_contingency(table2) # bu zaten testin kendisi RxC içinde yukarıdaki mantıkta yaparak uygulamış olacağız.
# ekstra olarak yapmanın anlamı yok farklı data seti bulup oradan yapın ki yapmak lazım yap işte yap yap yap
