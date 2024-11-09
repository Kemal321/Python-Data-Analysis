import numpy as np
from scipy import stats
import scipy.integrate # integral almak için kullanıyoruz
## Fabrika sorusunu bir de python a çözdürelim. 
xmean = 1040
sd = 25
n = 100
interval = 0.95
estimatedInterval = stats.norm.interval(confidence=interval,loc = xmean, scale = sd/np.sqrt(n))
print(estimatedInterval[0],estimatedInterval[1])
# Bu şekilde 12.sayfanın notlarının uygulanmış çözümü bu şekilde yani.

# farklı bir soru içindi bu bunu geçebiliriz.
xmean2 = 67
sd2 = 14
interval = 0.95

estimatedInterval2 = stats.norm.interval(confidence=interval,loc= xmean2, scale= sd2/np.sqrt(85))
print(estimatedInterval2[0],estimatedInterval2[1])

# ana mantık bu şekilde yani python ı scientific hesaplamalar için de bu şekilde kullanabiliriz ve kullanarak öğrenmeliyizde.
# T dağılımı için nasıl yapacağımıza bakalım.



# Mantık aynı hiç bir şey değişmeyecek sadece diğerinde stats.norm dedik yani normal dist idi bu ise t dist olduğu için
# stats.t.interval yaptık başka değişen bir şey yok bir de tablo için serbestlik derecesi verdik ekstradan kalan her şey aynı
n = 30 
xmean3 =  140
sd3 = 25
interval = 0.95
df = n-1

estimatedInterval3 = stats.t.interval(confidence=interval,loc=xmean3, scale = sd3/np.sqrt(n),df=df)
print(estimatedInterval3[0],estimatedInterval3[1])


########################## EXPECTED VALUE ###########################

# bir paranın 3 kere atılması ve en az 1 defa yazı gelme olasılığını hesap etmiştik 

"""

X 0   -> TTT          -> 1/8  
x 1   -> TTY TYT YTT  -> 3/8
X 2   -> YYT YTY TYY  -> 3/8
X 3   -> YYY          -> 1/8

"""
x = [0,1,2,3]
p = [1/8,3/8,3/8,1/8]

expectedValue = stats.rv_discrete(values=([x],[p])).expect() # rv yani random variable discrete yani ayrık. Bu fonksiyon ayrık random var. için kullanılıyor
print("Ayrık rassal değişkenlerin beklenen değeri: ",expectedValue)


# bir de sürekli değişkenler için görelim
"""
f(x) = 3/7*x**2  -> 1 < x < 2
        0        -> D.D   
"""
# İlk olarak bir fonksiyonu tanımlayalım

def f(x):
    return (3/7)*x**3 # return yaptık çünkü başka bir yerde çağırmak istiyorsak eğer return etmek durumundayız. Aslında burada yaptığımız 
                      # çağrılabilir bir nesneye dönüştürmek olarak da düşünülebilir. 

expectedValueCont =  scipy.integrate.quad(f,1,2,)
print(expectedValueCont) # iki değer döner bunlardan birincisi integralin sonucu ikincisi bu integral alınırken oluşan mutlak hata









