import pandas as pd 
import pingouin as pg 
import matplotlib.pyplot as plt 
import seaborn as sns 

data = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python ile Veri analizi\correlationMatrixExample.xlsx")

# bu şekilde korelasyon matrisini hesaplayabiliriz. 
kormat= data.corr()
print(kormat)

# daha detaylı görmek için pingouin kütüphanesindeki hesaplamayı da kullanabileriz burada pval ile 
# ilişkinin mantıklı olup olmadığını da yorumlayabiliriz.
p1 = pg.pairwise_corr(data)
print(p1)

# istersek bu şekilde ısı haritasını da çıkarabiliriz. 
sns.heatmap(kormat)

# ısı haritası üzerine değerleri de yazdırabiliriz 
sns.heatmap(kormat,annot=True)

# iki tane legend çıkmasının nedeni yukarı da da göstermiştik adım adım gittiğimiz için dursun zaten neden
# olduğunu bildiğimiz için bizim için bir bilinmez değil.
# rengini de değiştirebiliriz

sns.heatmap(kormat,annot=True,cmap=plt.cm.Blues)
plt.show()

# farklı bir gösterim olarak pingouin den 
p2 = pg.rcorr(data)
print(p2)
"""
        A      B       C  D
A       -
B   0.119      -
C   0.188  0.214       -
D  -0.135  0.126  -0.162  -

Burada alt tarafta korelasyon değerleri gözükür üst taraf boştur orayı doldurmak istersen p valueler 
ile dolar onları getirmek için 2.bir parametre olarka stars=False yaparsak yeterli olur 
"""
p3 = pg.rcorr(data,stars=False)
print(p3)

"""
        A      B       C      D
A       -  0.538   0.328  0.484
B   0.119      -   0.264  0.515
C   0.188  0.214       -    0.4
D  -0.135  0.126  -0.162      -

Bu şekilde doldu daha önce p1 = pg.pairwise_corr(data) ile hesapladığımız her şey buraya gelmiş oldu artık
"""
