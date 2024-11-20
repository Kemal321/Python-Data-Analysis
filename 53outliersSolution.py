"""
Outliers yani aykırı değerleri çözmenin genel olarak 3 yöntemi vardır biz yine giriş 
olacak şekilde öğrenelim ilerleyen zamanlarda doğrusal modeller vs. öğrendikten sonrasında bu 
konulara tekrar gelerek derin suların da tadına varacağız. 
1- Silme yöntemi
ilk olarak göreceğimiz şey aykırı değerlerin olduğu satırların silinmesi. Her ne kadar 
veri kaybını istemesek de bazen yapabileceğimiz bir şey kalmaz ve bu noktalarda el mecbur bunları sileriz
daha önce bu durumları eksik veriler hususunda ele aldık 
mantalite aynı şekilde olacak. 
2- Ortalama yöntemi 
Bu da aynı eksik veri kısmındaki gibi aykırı değerleri ortalama değerler ile doldurarak 
verinin dağılıma vereceği hasarı azaltmak veya yumuşatarak hatayı minimize ederek ilerlemek
adına kullanılabilir bir yöntem olarak çıkmaktadır. 
3- Baskılama yöntemi 
Aykırı değerlerin bulundukları yere göre en yakın sınırlara indirgeme ile ilgili bir 
konu demek istediğimiz anlaşılmıştır o yüzden devam edebiliriz.

"""

# 1 Silme yöntemi
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

data = sns.load_dataset("taxis")

data2 = data.copy()

print(data2.isnull().sum())

# tip                 0 üzerinden çalışalım

sns.boxplot(data2["tip"])
plt.show()
# bir çok aykırı değere sahip olduğumuz belli ilk olarak 
# silme metodunu görelim 

# çeyrekliklerimizi belirleyelim
Q1 = data2["tip"].quantile(0.25)
Q3 = data2["tip"].quantile(0.75)

IQR = Q3 - Q1 

altSınır = Q1 - 1.5 * IQR
ustSınır = Q3 + 1.5 * IQR

aykırıDF1 = data2[data2["tip"]<altSınır]["tip"]
aykırıDF2 = data2[data2["tip"]>ustSınır]["tip"]

# şimdi bunları birleştirmek için concat() fonksiyonumuzu kullanarak yapalım
aykırıDF = pd.concat([aykırıDF1,aykırıDF2],axis=0).index # satırbazlı olarak bunları birleştirdik ve sadece indexlerini tuttuk
print(aykırıDF)

# indexden dönen obje bir int64 index objesi bunu direkt olarak kullanamıyoruz 
# bunları bir listeye aktarmamız lazım 

aykırıIndex = [i for i in aykırıDF]
print(aykırıIndex) # bu şekilde list comprehension ile tek satırda hepsini atamış olduk 
# artık bunları tip sütunundan sileceğiz
data3 = data2.drop(data2.index[aykırıIndex])
print(data3) # aykırılar silindi 

fig, ax = plt.subplots(1,2)
ax[0].boxplot(data2["tip"])
ax[0].set_title("İlk")
ax[1].boxplot(data3["tip"])
ax[1].set_title("Son")
plt.show()
# bu sonuçlara bakacak olursak hala aykırı değerimiz 
# var gibi görünür ama aykırı gibi görünen değerlerimiz her zaman var olacak zaten
# sonuçta quartillerden hesaplıyoruz ve onlar sabit değil. 
# o yüzden sürekli silemeyiz biz en aykırıları sildik aslında :D
# bunları bu şekilde sürekli silersek veri kalmaz.

# 2- Ortalama yöntemi 
"""
Yine aynı şekilde sildiğimiz değerleri silmek yerine onlara ortalama değerlerini atayacağız. Burada indeksler
yeniden kullanılacağı içni yukarıdaki gibi tekrar yazmak yerine onları kullanacağım 
"""

mean = data["tip"].mean()
# Aykırı değerlerimizi bu ortalama (mean) değerleri ile dolduracağız.

data2.loc[aykırıIndex,"tip"] = mean  # daha önce gördüğümüz loc fonksiyonunu kullanarak bu indeklerin LOCation larına gitcez 
# ve mean değerleri ile orjinal değerleri değiştireceğiz
print(data2["tip"][aykırıIndex]) # şimdi bir de bu indeksleri çağıralım bakalım değişmiş mi 
"""
22      1.97922
42      1.97922
111     1.9792

değiştirmiş hepsini """

fig, ax = plt.subplots(1,2)
ax[0].boxplot(data["tip"])
ax[0].set_title("İlk")
ax[1].boxplot(data2["tip"])
ax[1].set_title("Son")
plt.show()

# yine benzer şekilde bir düşüş oldu bu metod da bu kadar basit ve kullanılan bir metoddur.


# 3- Baskılama yöntemi 

#basitçe loc fonksiyonu ile hızlıca yapabiliriz. Sonuçta ortalama atamak yerine bu sefer sadece alt sınır ve üst sınır değerlerini atayacağız 

data4= data.copy()
Q1 = data["tip"].quantile(0.25)
Q3 = data["tip"].quantile(0.75)

IQR = Q3 - Q1 

altSınır = Q1 - 1.5 * IQR
ustSınır = Q3 + 1.5 * IQR

data4.loc[data["tip"]<altSınır,"tip"] = altSınır
data4.loc[data["tip"]>ustSınır,"tip"] = ustSınır
sns.boxplot(data4["tip"])
plt.show()
# bu şekilde tamamını baskılamış olduk aslında. Bir nevi çantanın dışına taşan giysileri üstüne basarak fermuarı çektik 
# akademi de çok kullanılmaz ama bilmek lazım kategorik olarak da baskılanabilir .
# daha bir çok farklı metod var zamanla uğraştıkça öğreneceğiz vs. vs. devammmmmm
