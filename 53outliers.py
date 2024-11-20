import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.neighbors import LocalOutlierFactor
data = sns.load_dataset("titanic")

data2 = data.copy()

# age üzerinde çalışacağız burada öncelikle notlarda belirtildiği gibi eksik değer var mı bunun kontrolü 
# var ise çözümü sonrasında ise aykırı değerler hususuna ilerleyeceğiz.
print(data2.isnull().sum())
"""
survived         0
pclass           0
sex              0
age            177
sibsp            0
parch            0
fare             0
embarked         2
class            0
who              0
adult_male       0
deck           688
embark_town      2
alive            0
alone            0
"""

data2["age"].fillna(data2.groupby("sex")["age"].transform("mean"),inplace=True)
print(data2.isnull().sum())
print(data2["age"].isnull().sum())

"""
survived         0
pclass           0
sex              0
age              0
sibsp            0
parch            0
fare             0
embarked         2
class            0
who              0
adult_male       0
deck           688
embark_town      2
alive            0
alone            0

veya 2.satırdaki direkt olarak 0 değerini döndürür.
Yani burada herhangi eksik veri yani missing data problemimiz kalmamış oldu 
"""

# box plot ile aykırı değerlerimizin olup olmadığını bulabiliriz sonuçta bu bir tek değişkenli aykırı değer 
#sns.boxplot(data=data2["age"])
#plt.show()

# sonuçta grafiğimizin uçlarında aykırı değer olduğunu gösteren işaretleri gördük ve artık aykırı değerlerin
# varlığına karşın emin durumdayız. Şimdi bunları çözmemiz gerekiyor.

# çözüm için Q1-1.5*IQR ve Q3+1.5*IQR yapısını oluşturmamız gerekiyor. 
Q1  = data2["age"].quantile(0.25)
Q3  = data2["age"].quantile(0.75)
IQR = Q3 - Q1

altSınır = Q1 - 1.5 * IQR
ustSınır = Q3 + 1.5 * IQR

# şimdi aykırı değerlerimizi toplayabiliriz.
askucuk = data2[data2["age"]<altSınır]["age"]
usbuyuk = data2[data2["age"]>ustSınır]["age"]
# burada dedik ki data2 ye git orada data2["age"]>ustSınır koşulunu sağlayan indeksleri bul sonra 
# bunlar arasında ["age"] sütunundakileri al ve bir yere topla 
print(askucuk,"*****************************",usbuyuk,sep="\n")

"""
827    1.00
831    0.83
Name: age, dtype: float64
*****************************
11     58.0
15     55.0
33     66.0

Böylece bunak ve bebişleri topladık :D
"""
#  Çözümüne girmedik ama tespiti bu şekilde oluyor bir de çok değişkenli tespite bakalım :D

data3= sns.load_dataset("taxis")
data4 = data3.copy()

print(data4.isnull().sum())# bu nokta da fare ve tip e bakacaktık bunlarda bir eksik değer yok
# peki outlier var mı

# veriyi aldık ve yedekledik şimdi bunlar arasından scatter plot ile bir bakalım var mı yok mu 
sns.scatterplot(data=data4,x="fare",y="tip") # ücret (fare) ile bahşiş (tip) arasında aykırı ( bonkör ) eleman var mı bakaciz
plt.show() 
# sonuçlar sıkıntılı outlier var :) ücretin yüzde 40 ı kadar tip veren var taksici mi olsak. Aga yapma kafam karıştı 

# aykırı değerleri bulduğum sütunları çalışmak için öncelikle farklı bir DataFrame olarak saklamak istiyorum 

aykırıDf = pd.DataFrame(data=data4,columns=["fare","tip"])

# sonrasında sklearn daha önce kullandık ilgili metodu import edelim ( LOF )
LOF = LocalOutlierFactor(n_neighbors=20,contamination=0.1)
tahmin = LOF.fit_predict(aykırıDf)
print(tahmin)
"""
[1 1 1 ... 1 1 1]
Bu şekilde bir çıktı döndü şimdi öncelikle içerideki parametreleri bileceğiz ama şuan da değil şuan sadece
çalıştıralım mesela metric = "minkowski" demiş bu mahalanobis gibi bir mesafe ölçme tekniğidir. 
Şuan sadece kullanımına örnek olarak uygulama yapıyorum
Ek olarak bu tahmin değerlerinin döndüğü 1 değerleri aykırı değerler değil iken -1 dönenler aykırı değerdir
Buna göre bizim aykırıDf değişkenindeki verileri filtreleyebiliriz 
"""

print(aykırıDf[tahmin==-1])
"""
       fare   tip
8     15.00  1.00
6426   4.50  0.50

[644 rows x 2 columns]
644 aykırı gözlem değeri varmış. Toplumda bu 644 eleman taksicilerin en sevdiği elemanlardır diyebiliriz :D
"""

