import pandas as pd 
import pingouin as pg
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
import statsmodels.stats as ss
import matplotlib.pyplot as plt

data = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python ile Veri analizi\employee.xlsx")


"""ANOVA, bir doğrusal model (Linear Model, OLS - Ordinary Least Squares) üzerinden çalışır.
Bu model bağımlı değişken ile bağımsız değişkenler arasındaki ilişkileri incelemek için oluşturulur.
Yani her zaman yaptığımız gibi aşağıdaki gibi parçalayarak vs. ilerlemeyeceğiz """


model = ols("Performans~C(Mevki)+C(Süre)+C(Mevki):C(Süre)",data=data).fit() # burada verdiğimiz string OLS nin model yapısıdır. 


"""
"Performans~C(Mevki)+C(Süre)+C(Mevki):C(Süre)" yazımı,
 Performans bağımlı değişkenini Mevki, Süre ve bu ikisinin etkileşimini içeren bağımsız değişkenlerle ilişkilendirir.
Bu model kendiliğinden varyansları ve etkileşimleri hesaplayarak ANOVA tablosu için uygun bir yapı kurar
"""
hatalar = model.resid # burada modelimiz kendisi bu işlemi yapacak ve bize verecek

normallik = stats.shapiro(hatalar) # sonrasında shapiro testi ile bu hatalar değişkenimiz üzerinden yapacağız ve normallik diye kaydettik
print(normallik) # bu şekilde klasik bir çıktı alabiliriz. Ama genel olarak qq plot olarak alınır çıktılar bizde qq plot alalım

"""# ilk olarak bağımsız değişkenleri kendi gruplarında tutmak adına değişkenlerde saklayalım
işçi = data[data["Mevki"] == "İşçi"]["Performans"]
UstaBaşı = data[data["Mevki"] == "UstaBaşı"]["Performans"]
Yönetici = data[data["Mevki"] == "Yönetici"]["Performans"]"""

fig = sm.qqplot(hatalar,line="s")
plt.show()
"""
qq plot isminden kolayca anlaşılıyor veriyi çeyrekliklere bölüyor anladığım kadarı ile ve aynı zamanda veriye uygun teorik
normal dağılımın çeyreklikleri ile karşılaştırıyor.  Ve biz de görsel üzerinden aykırı değerlerin çokluğu azlığı ve 
normallik testinin sonuçlarına ne kadar uygun olduğunu görsel açıdan da test etmiş oluyoruz
"""

#şimdi model ile ilgili sonuçları almak için pandas da yaptığımız describe gibi burada da summary fonksiyonu ile bir çıktı alacağız 
print( model.summary() ) # Prob (F-statistic):            0.00136 Şuan çok iyi değiliz ama bizim için şuanlık bu deperin daha önceki gibi 0.05 ten 
                         # az olması gerektiğidir. Normalde silerim de dursun anovadan devam maksat not olarak saklansın

# anova modelini oluşturabiliriz. 
anovam = sm.stats.anova_lm(model,type=2) # anova_lm yani anova linear model type 2 derken bağımsız değişken gruplarımızın 
                                         # örneklem sayıları eşit olduğu için kullanırız daha sağlıklı değil ise type=3 daha sağlıklıdır 

print(anovam)
"""
                    df      sum_sq    mean_sq         F    PR(>F)
C(Mevki)           2.0   45.875000  22.937500  5.898214  0.006086
C(Süre)            3.0    2.833333   0.944444  0.242857  0.865846
C(Mevki):C(Süre)   6.0  110.291667  18.381944  4.726786  0.001210

Buna göre Mevki anlamlı 0.05 ten küçük çünkü ama süre tek başına mantıklı bir etki yapmıyormuş aynı zamanda 
mevki ve sürenin beraber etkisi de mantıklıymış bu noktadan sonra post hoca yapacağız neden çünkü anova tek başına
bize tam sonuç vermiyordu şimdi mevki ve mevki&süre nin birleşimi ile beraber ilerleyeceğiz ve indireceğiz.
"""

# posthoc yapalım 
etkimevki = ss.multicomp.pairwise_tukeyhsd(endog=data["Performans"],groups=data["Mevki"])
print(etkimevki)
"""
  Multiple Comparison of Means - Tukey HSD, FWER=0.05
========================================================
 group1   group2  meandiff p-adj   lower   upper  reject
--------------------------------------------------------
Ustabaşı Yönetici     0.25 0.9522 -1.7823  2.2823  False
Ustabaşı     İşçi  -1.9375 0.0645 -3.9698  0.0948  False
Yönetici     İşçi  -2.1875 0.0323 -4.2198 -0.1552   True

Bizim için anlamlı olan değerler Reject kısmında True olarak dönen değerler bu nokta da Ustabaşı yönetici ve Ustabaşı işçi arasında bir fark yoktur
demek ki biz true olana yani yönetici-işçi ikilisine bakacağız 

"""
# şimdi bu farklı ortalamaları tespit edelim
grup1 = data.groupby("Mevki")["Performans"].mean()
print(grup1)
"""
Ustabaşı    6.3125
Yönetici    6.5625
İşçi        4.3750

Görüldüğü gibi ustabaşı ve yöneticiler çalışıyor işçiler çok da performanslı değil. İyi firma iyi işçiler bulursa ya da aynı performans da
ucuz işçi bulursa firmanın iyileşeceği görülmekte :D
"""

# şimdi mevki ve sürenin beraber olan etkisini inceleyelim çünkü o da F score adına biizm için mantıklı taraftaydı
etkimevkisüre = ss.multicomp.pairwise_tukeyhsd(endog=data["Performans"],groups=data["Mevki"]+data["Süre"])
print(etkimevkisüre)
# yine aynı şekilde true olanlara bakacağız


grup2 = data.groupby(["Mevki", "Süre"])["Performans"].mean()
print(grup2)
"""
       YöneticiBir yıl               İşçiBir ay     -5.5 0.0158 -10.367 -0.633   True
       YöneticiBir yıl               İşçiBir yıl    -5.5 0.0158 -10.367 -0.633   True
       İşçi3 yıl ve üzeri            İşçiBir ay     -5.5 0.0158 -10.367 -0.633   True
       İşçi3 yıl ve üzeri            İşçiBir yıl    -5.5 0.0158 -10.367 -0.633   True

Mevki     Süre
Ustabaşı  3 yıl ve üzeri    6.00
          Beş ay            6.25
          Bir ay            6.50
          Bir yıl           6.50
Yönetici  3 yıl ve üzeri    4.25
          Beş ay            6.75
          Bir ay            7.25
          Bir yıl           8.00
İşçi      3 yıl ve üzeri    8.00
          Beş ay            4.50
          Bir ay            2.50
          Bir yıl           2.50

Evet baktık aslında buna göre yorum yapacağız yeni gelen işçiler paket sonrasında performans yıl geçtikçe performans artarak devam etmiş 
yöneticilerde ise bu durum yine bu şekilde iken yıllanmış yöneticiler işin tricklerini anlamış ve çalışmak yerine gelen tehlikeleri atlatarak 
statülerini korumaya odaklanmış işçilerde ise bir yıl olduğunda işçiler ciddi performans kaybı yaşamış ve ayrılan ayrılmış ayrılmayanlarda 
işi öğrendikleri ve yatkınlıkları sistemin işleyişine olan adaptasyonları iyileşme yaşadıktan sornasında ise mermi gibi performans sağlamışlar 
helal olsun 3 yıl ve üzeri olanlara prim vermek lazım 1 maaş ikramiye bas reislere serisinden :D
"""


"""
Ek olarak Pandas’ın melt fonksiyonu, veri setlerini geniş (wide) formattan uzun (long) formata dönüştürmek için kullanılır.
Bu, özellikle verilerin görselleştirme veya analiz için daha uygun bir formatta olması gerektiğinde yararlıdır.
 Melt İşleyişi ve Kullanım Alanı
melt fonksiyonu, geniş formatta yan yana bulunan sütunları, uzun formatta satır başına bir gözlem olacak şekilde yeniden düzenler. Bu işlev:

Analiz kolaylığı sağlar: Örneğin, belirli kategoriler veya değişkenler arasındaki farkları kolayca incelememize olanak tanır.
Veri görselleştirme araçlarıyla uyumluluk sağlar: Çoğu grafik aracı uzun veri formatını tercih eder.
"""
data2 = pd.DataFrame({
    'id': [1, 2, 3],
    'Math': [90, 80, 85],
    'Science': [92, 82, 88]
})
melted_data = pd.melt(data2, id_vars=['id'], var_name='Subject', value_name='Score')
print(melted_data)
# bunu da öğrendik burada bitirdik