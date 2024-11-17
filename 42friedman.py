import pandas as pd 
import pingouin as pg
from scikit_posthocs import posthoc_conover_friedman # friedman için olanı seçmemiz lazım.
import numpy as np 
data = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python ile Veri analizi\friedman.xlsx")

# long formata getirmek için melt fonksiyonunu kullanabiliriz 
dataCor = pd.melt(data,id_vars=["Hastalar"],value_vars=["TÖ","TS","TS2","TS3"])
dataCor.columns = ["Hastalar","Testler","Değerler"]

normalityCheck = pg.normality(data=dataCor,dv="Değerler",group="Testler")
print(normalityCheck)
"""
                W      pval  normal
Testler
TÖ       0.906973  0.466514    True
TS       0.833805  0.177942    True
TS2      0.691725  0.009263   False
TS3      0.746922  0.036132   False

Buna göre 2 grubum normal dağılım gösterirken 2 grubum göstermiyormuş bunlar TS2 TS3
Diğer varsayımları da burada deneyebiliriz ama 1 tanesi sağlamadığı için friedman ı da görmek için 
ben direkt olarak teste geçiyorum yine Pingouin kütüphanesini kullanacağım

"""

test = pg.friedman(dataCor,dv="Değerler",within="Testler",subject="Hastalar")
print(test)
"""
           Source      W  ddof1    Q     p-unc
Friedman  Testler  0.575      3  6.9  0.075154

Burada pval > 0.05 şeklinde sonuç verdi bu demek oluyor ki aşılar hastalar üzerinde bir farklılık oluşturmuyor
velev ki oluştursaydı ne olacaktı o zaman post hoc testlerine geçerdik orada da yine aynı şekilde 
Conover ve Dunn var ama genellikle akademilerde Conover kullanılır görme açısından onları da kullanalım
Burada Friedman conover diye geçer
"""
# conover çalışırken array yapıları ile çalışır yukarıdaki test değerlerini 
# hasta bazlı olarak arraylere çevirmemiz lazım 
df = np.array([data["TÖ"],data["TS"],data["TS2"],data["TS3"]])
postho = posthoc_conover_friedman(df,p_adjust="bonf")
print(postho)
"""
          0    1         2         3
0  1.000000  1.0  0.118639  0.118639
1  1.000000  1.0  1.000000  1.000000
2  0.118639  1.0  1.000000  1.000000
3  0.118639  1.0  1.000000  1.000000
0 1 2 3 -> data["TÖ"],data["TS"],data["TS2"],data["TS3"] aslında 
tabloda her hangi bir farklılık olmadığını söylemişti o yüzden bu da onu desteklemiş oldu 
eğer bir farklılık olsaydı hangi testler arasında olduğunu buradan görebilir ve buna göre de yorum 
yapabilirdik
"""






