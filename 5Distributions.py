import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# Bernoulli dağılımının teorik tarafını çalışmıştım. Şimdi burada nasıl kullanılıyor bunu görelim.
p = 0.5 # bir paranın atılması ile tura gelme olasılığı başarısızlık için olsun 

# dağılımımızı tanımlayalım
distr = stats.bernoulli(p) # sadece bir değer yeterli çünkü q değeri zaten 1-p olduğu için kendisi yapacaktır. 

turaProb = distr.pmf(k=0) # bu kesikli olasılık dağılımı olduğu için probability mass function kullanıyoruz teorikten 
yazıProb = distr.pmf(k=1) 

# başarılı ve başarısız olasılıkları bu şekilde görebilir ve yazdırabiliriz. 
print(f"Yazı gelme olasılığı {yazıProb}\nTura gelme olasılığı {turaProb}")

# beklenen değeri ve varyansı da yazdırabiliriz. 
print(f"Bernoulli Dağılımının beklenen değeri {distr.expect()}\nBernoulli Dağılımının varyansı {distr.var()}")
 

# Bernoulli bu şekilde basit ilk olarak başarılı olsasılık sonrasında dağılımı oluştur ve başarılı başarısızı tanıt ve bitti 

# Şimdi de binom dağılımı için bakalım bu nokta da bernoulli ile çok benzer demiştik zaten sadece birden çok durumun varlığı ve 
# bunun hesaplama farklılıkları var. Burada ek olarak sadece parametreler için n yani deney sayısı parametresi gireceğiz

# bir madeni paranın atılması ile 3 tanesinin yazı gelme olasılığı durumu için oluşan binomial istatistiki dağılım.
n = 7 # daha önce notlardaki örneği kullanalım.
p = 0.5 # yazı gelme olasılığı 

binomialDist = stats.binom(n,p)
yazı = binomialDist.pmf(k=3) # 3 tanesinin yazı gelme olasılığını merak ettiğimiz için soruda ki gibi 3 yazdık ve pmf yani 
                             # probability mass function kesikli bir olasılık dağılımı olduğu için de olasılık kütle fonksiyonunu kullandık
print("\n######################################## BİNOM DAĞILIMI ######################################")
print("Binom dağılımına göre 7 kere atılan paranın 3 defa yazı gelme olasılığı {}".format(yazı))
print(f"Binom Dağılımının beklenen değeri {binomialDist.expect()}\nBinom Dağılımının varyansı {binomialDist.var()}")

#  örnek 2 
pbin2 = 0.01
nbin2 = 10

binomialDist2 = stats.binom(nbin2,pbin2)

# düz mantıkla toplayarak da gidebiliriz bunun için pmf fonksiyonunu kullanırız. 
ürün0 = binomialDist2.pmf(k=0)
ürün1 = binomialDist2.pmf(k=1)
ürün2 = binomialDist2.pmf(k=2)
print("Cevap: {}".format(ürün0+ürün1+ürün2))

# veya kısa ve mantıklı olan yol cdf kullanırız 

ürüncdf012 = binomialDist2.cdf(x=2)
print("Cevap cdf: {}".format(ürüncdf012))



print("\n######################################## POISSON DAĞILIMI ######################################")

# teorik olarak konuyu ele aldık şimdi scipy kütüphanesinde nasıl çalıştığına bakalım 
"""
Bir çağrı merkezine 1 dakika da ortalama 10 adet arama yapılıyorsa 1.dakika da hiç çağır yapılmama olasılığı kaçtır. 
"""

poissonP = 10 # lambda değerimiz yani ortalama

poissonDist = stats.poisson(poissonP)

p0 = poissonDist.pmf(0) # burada olasılık kütle fonksiyonu kullandık çünkü bu bir kesikli dağılım.
                        # Burada X = 0 dememizin nedeni zaten hiç çağrı gelmemeyi sorduğu için X = 0 yani Gelen çağrı = 0 demek oluyor. 

print("Çağrı gelmeme olasılığı %{}".format(p0*100)) # yüzde olarak görmek için 100 ile çarpacağım


print("\n######################################## NORMAL DAĞILIMI ######################################")

"""
Bir fabrikada üretilen ürünlerin ortalama ağırlığı 500 gr ve varyansı da 100 gramdır. Rastgele seçilen bir ürünün 518 gramdan az olma ihtimali 
nedir ? 
"""

# Buna göre P ( X < 518 ) İSTİYOR hemen oluşturalım ve burada belirli bir alanı istiyor o yüzden birikimli dağılım fonksiyonunu kullanacağım.

meanNorm = 500
varianceNorm = 100

normalDist = stats.norm(meanNorm,np.sqrt(varianceNorm)) # variance norm verdim çünkü fonksiyon std üstünden çalışıyor 
possibilityNorm = normalDist.cdf(x = 518)

print("Normal dağılımda seçilen ürünün 518 gramdan az olma ihtimali: %{}".format(possibilityNorm*100))


"""
Bir üretimde günlük gelen talep ortalam 100 adettir. varyans değerimiz ise 3000 adet. Stoğumuz da 3500 adet ürün bulunmaktadır. 
üretim durursa 1 ayda stok biter mi ? 
"""
# modelleyecek olursak X = ürün sayısı, mü = 100 sigmaKare = 3000 E(x) = 3000 ( çünkü günlük talep 100 tane ve 30 gün isteniyor n*p = 3000 oldu)
# İstenilen durum nedir Stok bitme durumunu belirlemek için, toplam 30 günlük talebin 3500'ü aşma olasılığını hesaplamalıyız.
# Bu,𝑃(𝑋>3500)'i bulmak demektir.

meanNorm2 = 3000 # E(x) i alacağız 
varianceNorm2 = 90000 # bize normal günlük varyans verilmişti o yüzden 30 gün istediği için bunu da 30 ile çarparak 90000 i bulduk bu aylık varyans

normalDist2 = stats.norm(meanNorm2,np.sqrt(varianceNorm2))
possibilityNorm2 = normalDist2.cdf(x=3500)

# Z-tabloları genellikle −∞ (eksi sonsuz) noktasından belirli bir Z-skoruna kadar olan olasılığı (𝑃(𝑍≤𝑧)verir. 
# Bu, Z-skorunun solundaki alanı temsil eder. O yüzden 1- P(X>3500)  yapmış bulunduk
print("1 ay içinde stoğun tükenme ihtimali: %{}".format(((1-possibilityNorm2)*100)))


# ek olarak sf() fonksiyonumuz var o da 1 - cdf hesaplamasını yapar yani yukarıdaki 1 den çıkartma mevzusu ile uğraşmak istemiyorsak
# direkt olarak bunu kullanabiliriz.
possibilityNorm21 = normalDist2.sf(x=3500)
print("1 ay içinde stoğun tükenme ihtimali: %{}".format((possibilityNorm21*100)))
# gördüğümüz gibi aynı çıktıyı veriyorlar hatta hasasiyeti fazla gibi :D


# kalan örnekler için uygulama yapmaya gerek yok uygulanış aynı çünkü. Fazladan aynı şeyi tekrar etmenin anlamı yok. 






