from scipy import stats
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd # post-hoca için bu modülü kullanacağız
import pingouin as pg
import scikit_posthocs as sp
data = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python ile Veri analizi\anovaExample.xlsx")
print(data)

sepData1 = data[data["Eğitim Durumu"] == "OrtaOkul"]
sepData2 = data[data["Eğitim Durumu"] == "Lise"]
sepData3 = data[data["Eğitim Durumu"] == "Üniversite"]
sepData4 = data[data["Eğitim Durumu"] == "YüksekLisans"]

# örnek olarak hazırlanmış daha doğrusu üretilmiş bir veri setidir sadece pratik amaçlı ürettik. 
# Şimdi anova testinin python da nasıl yapılacağını deneyeceğim

shap1 = stats.shapiro(sepData1["TvİzlemeSüresi"])
shap2 = stats.shapiro(sepData2["TvİzlemeSüresi"])
shap3 = stats.shapiro(sepData3["TvİzlemeSüresi"])
shap4 = stats.shapiro(sepData4["TvİzlemeSüresi"])
print(f"Grupların sahip olduğu veriler normal dağılıp dağılmadığını kontrol amaçlı shapiro testi sonuçları: \n{shap1.pvalue}\n{shap2.pvalue}\n{shap3.pvalue}\n{shap4.pvalue}")

# varyans homojenliğinin test edilmesi için bartlett testi yapalım 
bartDAY = stats.bartlett(sepData1["TvİzlemeSüresi"],sepData2["TvİzlemeSüresi"],sepData3["TvİzlemeSüresi"],sepData4["TvİzlemeSüresi"])
print(f"Varyans homojenliği testi sonucu: {bartDAY.pvalue}")

# yani varyansların homojen olduğunu öğrendik ve grupların verileri de normal dağılım sağladıkları için varsayımlarımızın hepsi düzgünce 
# sağlanmış oldu artık anova testini gerçekleştirerek hipotezlerimizi test edebiliriz.

testAnova = stats.f_oneway(sepData1["TvİzlemeSüresi"],sepData2["TvİzlemeSüresi"],sepData3["TvİzlemeSüresi"],sepData4["TvİzlemeSüresi"])
print(f"Anova testi sonucu: {testAnova.statistic:9.4f} -- {testAnova.pvalue:9.17f}")

# Anova testi sonucu: 2570.6487 -- 0.00000000000000000 görüldüğü üzere F testinden alınan olasılık değeri çok inanılmaz seviyelerde 
# p < alpha olduğu için H0 hipotezimiz reddedilmiştir. H1 hipotezimiz kabul edilmiştir şimdi ise H1 de bahsedilen farklılığın hangi 
# gruplar arasında olduğunu hesap etmek için Post-Hoc testleri yapacağız.

posthoc = pairwise_tukeyhsd(data["TvİzlemeSüresi"],data["Eğitim Durumu"],alpha=0.05)
print(posthoc)
"""
   group1       group2    meandiff p-adj   lower    upper   reject
------------------------------------------------------------------
        Lise     OrtaOkul   0.5961  0.775  -1.1858    2.378  False
        Lise YüksekLisans -38.1635    0.0 -39.9454 -36.3816   True
        Lise   Üniversite -38.5845    0.0 -40.3664 -36.8026   True
    OrtaOkul YüksekLisans -38.7596    0.0 -40.5415 -36.9777   True
    OrtaOkul   Üniversite -39.1806    0.0 -40.9625 -37.3986   True
YüksekLisans   Üniversite   -0.421 0.9047  -2.2029   1.3609  False

Bu şekilde bir tablo döndü değerlere bakarak anlayabiliriz zaten True olanlarda istatistiki olarak ciddi fark olsa da False olanlarda ciddi fark
yokmuş. 
"""


# Welch anova testini uygulayalım varyanslar eşit değilse uyguluyorduk
welchAnova = pg.welch_anova(data=data,dv="TvİzlemeSüresi",between="Eğitim Durumu") # burada veriyi veriyoruz sonra sütun adı ve grup adlarını veriyoruz.
print(welchAnova)
"""
Gördüğümüz gibi F i döndürdü p değerini döndürdü çok küçük olduğu görülüyor sonrasında post hoc a geçiyoruz zaten.
          Source  ddof1     ddof2            F         p-unc      np2
0  Eğitim Durumu      3  8.410716  2846.586516  5.680851e-13  0.99793
"""



# Scikit üzerinden çoğu teste ulaşabiliriz tablodaki tamhane's a bakalım.
tamhane = sp.posthoc_tamhane(data,val_col="TvİzlemeSüresi",group_col="Eğitim Durumu") # aynı mantık dökümandan görülüyor zaten
print(tamhane)