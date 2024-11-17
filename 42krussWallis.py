from scikit_posthocs import posthoc_conover 
import pandas as pd 
import pingouin as pg
data = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python ile Veri analizi\kruss.xlsx")

# İlk olarak datamızın dağılımını ve formatını görmek açısından bir yazdıralım
print(data)
"""
   A Yöntemi  B Yöntemi  C Yöntemi
0         81         48         18
1         32         31         49
2         42         25         49
3         62         22         33
4         37         30         24
Bu şekilde bir dağılım gösteren 11 satırdan oluşan bir data
fakat tabular formatta olması nedeniyle bunu long formata getirirsek bizim için daha iyi olacaktır.
"""

# long formata çevirme işlemi için 
dataCor = pd.melt(data,value_vars=["A Yöntemi","B Yöntemi","C Yöntemi"])
dataCor.columns=["Yöntem","Değer"]
print(dataCor)

"""
       Yöntem  Değer
0   A Yöntemi     81
1   A Yöntemi     32
2   A Yöntemi     42
3   A Yöntemi     62
4   A Yöntemi     37
5   A Yöntemi     44
6   A Yöntemi     38
7   A Yöntemi     47
Görüldüğü üzere long formata getirdik ve bağımsız değişkenlerimizi Yöntem sütununda bağımlı değişkenlerimizi
Değer sütunu altında toplamış olduk.
"""

# normallik testi yapabiliriz
normalityCheck = pg.normality(dataCor,dv="Değer",group="Yöntem")
print(normalityCheck)
"""
                  W      pval  normal
Yöntem
A Yöntemi  0.839268  0.043242   False
B Yöntemi  0.839410  0.043412   False
C Yöntemi  0.836683  0.040263   False
Normallik dağılımından geçemedi ve veri adedimiz çok küçük burada tek yönlü anova uygulayamayız 
o yüzden krussWillis e geçeceğiz.
"""
test = pg.kruskal(data=dataCor,dv="Değer",between="Yöntem")
print(test)
"""
        Source  ddof1         H     p-unc
Kruskal  Yöntem      2  6.433021  0.040095
Buna göre kruskal değeri p = 0.04 < 0.05 olduğu için H0 hipotezimiz reddedildi 
Yani verilerimizin medyan dağılımları eşit değil o halde posthoc testi yaparak bu farklılığın 
nerede olduğunu bulmaya çalışalım
"""

posthoc = posthoc_conover(dataCor,val_col="Değer",group_col="Yöntem",p_adjust="bonf")
print(posthoc)
"""
           A Yöntemi  B Yöntemi  C Yöntemi
A Yöntemi   1.000000   0.083968   0.059622
B Yöntemi   0.083968   1.000000   1.000000
C Yöntemi   0.059622   1.000000   1.000000
Sonuçlarımız bu şekilde baktığımız zaman 0.05 ten küçük olan bir değerimiz olmasa da ona çok yakın olan
A ve C yöntemleri arasında 0.0596 gelmiş bir değerimiz var farklılığın bundan kaynaklandığı yorumu yapılabilir.
"""