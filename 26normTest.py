import matplotlib.pyplot as plt 
import numpy as np
from scipy import stats
import seaborn as sns

# dağılımlara göre rastgele sayılar üreteceğim ve normallik testlerinden bir kaçını deneyeceğim.
# Rastgele verilerin sabit olmasını istediğim için rng için bir seed oluşturalım.

np.random.seed(3) # her hangi bir değer verebilirsiniz okul numaramı veriyorum
datas = stats.norm.rvs(loc=38,size=500) # verilerimi normal dağılıma göre oluşturduk. 

# genelde çalışmalar yapılırken momentlerin skewness veya kurtosis gibi bunların belirli aralıklarda kalmasına bakılarak varsayım ile 
# ilerlenir bunun için yapılmış çalışmalara atıfta bulunularak kullanıldığından bahseder ve varsayımın üstünden ilerlenir. 

print(f"Veri setinin kurtosis değeri: {stats.kurtosis(datas)}\nVeri setinin Skewness değeri: {stats.skew(datas)}")
# bir makaleden örnekle mesela Tabachnick ve Fidell 2013 te bir çalışmada kurtosis ve skewness in -1.5 ve +1.5 arasında kalmasının normal dağılım
# gösterdiğini varsayarak ilerlemiş. Bizim değerlerimiz de bu şekilde -0.1450440464554381 , -0.009003052693810708

# verilerimizin dağılımının grafiğini de çizdirebiliriz. 
sns.displot(datas,kde=True) # hocanın kullandığı zamanlar 2 sene önce o yüzden doküman kontrolü yapmayı unutmamak lazım çalışmayabilir. 

stats.probplot(datas,dist="norm",plot=plt) # burada da verilerin dağılımına uyan en iyi lineer doğruyu çizdirerek verilern ona göre nasıl 
plt.show()                                 # dağıldığını görmemiz açısından kullanılıyor. Dökümanları incelemek yetmez ekstra bilmek lazım
                                           # bu şuan için yeterli bilgi.


# Gelelim normal dağılım sınamalarına 
"""
İlk olarak bunun amacı burada aslında 
H0: Normal dağılıma uygun
H1: Normal dağılıma uygun değil 
hipotezlerinin sınanmasıdır. Biz Kolmogrov-Smirnov tek örneklem sınaması ve Shapiro-Wilk sınamasına odaklanacağız.
İleride de bunları detaylı göreceğiz şuan kodlarda nasıl olduğunu ufak bir görelim istedik.
"""

ks = stats.kstest(datas,cdf="norm") # bu şekilde bırakırsak normal bir dağılıma göre nasıl bir veri olması gerektiğini gösterir. 
# ek olarak kendi mean ve std değerlerimizi vermemiz gerek
ks2 = stats.kstest(datas,cdf="norm",args=(datas.mean(),datas.std()))
print(ks2)
# bir de çıktısı biraz karmaşık olabilir o yüzden sadece p value ye odaklanarak onu düzenlemeliyiz. Bunu da format ile yapacağız.
print(f"P value düzgünce: {ks2.pvalue:5f}")


"""Shapiro dayının metodunu görelim. Shapiro dayı daha fazla kullanılır en çok kullanılanlardan birisidir. """

shapiroDayi = stats.shapiro(datas)
print(shapiroDayi)
print(f"P value düzgünce shapiro dayi: {shapiroDayi.pvalue:5f}")

# 0.72 geldi yani 0.05 den büyük olduğu için verilerin normal dağılıma uygun dağıldığını hipotezimizi desteklediğini görmüş olduk.