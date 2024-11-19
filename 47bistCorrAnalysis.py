import pandas as pd 
import yfinance as yf 
import matplotlib.pyplot as plt 
import seaborn as sns 
import pingouin as pg 


dataShare = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python ile Veri analizi\bistshares.xlsx")

# Yfinance kütüphanesini kullanırken hisselerin isminin yanında ıs eki olmalı yani OZRDN.IS -> bunun gibi o yüzden verilerimi güncellemem lazım

dataShare2 = dataShare + ".IS"

# Burada yfinance de kullanabilmem için dataframe yapısından liste yapısına gitmem lazım 
# bunları almak için dataShare2 dataframesinin Kod sütunundaki değerleri listeye çevir -> aynısını yapacağım gramatik düşünün
sharesList = dataShare2["Kod"].values.tolist()
           # Kod sütunundaki  değerleri  listeye çevir   aynen bu şekilde dümdüz ingilizce yazı yazmak gibi. 
# ı will turn the values of dataframe inTO list

# yfinance den verileri alalım
veri = yf.download(tickers=sharesList,start="2020-01-01",end="2022-05-24")
"""[*********************100%***********************]  30 of 30 completed
Price                      Adj Close                                               ...     Volume
Ticker                      AKBNK.IS   ALARK.IS   ASELS.IS   ASTOR.IS    BIMAS.IS  ...   TOASO.IS    TTKOM.IS    TUPRS.IS    ULKER.IS     YKBNK.IS
Date                                                                               ...
2022-01-03 00:00:00+00:00   6.170553  12.177504  10.826067        NaN   60.502232  ...  7368487.0  21174279.0  39196843.0   1861033.0  274077473.0
2022-01-04 00:00:00+00:00   6.120044  12.187138  11.173693        NaN   63.553165  ...  8375544.0  25375454.0  50476923.0   3677434.0  319225871.0
2022-01-05 00:00:00+00:00   6.178972  12.158235  11.431930        NaN   65.055161  ...  5324848.0  37446851.0  43477014.0   2388677.0  181430411.0
2022-01-06 00:00:00+00:00   6.162135  11.782504  11.551115        NaN   64.726593  ...  6508441.0  29931524.0  47209372.0   2267245.0  336966331.0

Bu şekilde verileri indirdi ve onları veri adlı değişkene atamış olduk
"""
# ama burada volume gibi hacimle alakalı veriler şuan da benim ilgimi çekmiyor sadece adj close tarafındaki verileri alalım
priceS = veri["Adj Close"].reset_index()
print(priceS.isna().sum()) # bazı hisselerde çok fazla veri eksik belki onların o zaman daha arz edilmeyip şuan bu listede olmalarından doalyı
# olabilir.

getiri = veri["Adj Close"].pct_change() # getirileri bu fonksiyon ile hesap eder aslında binrönceki gün fiyat / bugün kapanış fiyat -1  
print(getiri) # ilk satırın NaN ile dolmasının nednei ondan önceki günün verileri yok yani referans alacağı bir maliyet fiyat yok.

# oynaklığı yani volatiliteyi hesap etmek istersek yani standart sapma 
sd = getiri.std()
print(sd.sort_values(ascending=False))

korelasyon = getiri.corr()

plt.title("BIST 30 Korelasyon Matrisi",color = "Blue",fontsize=15)
sns.heatmap(korelasyon,annot=True,cmap="Blues",xticklabels=True,yticklabels=True,vmax=1,vmin=-1)
plt.show()

# anlamlılıklarını anlamak için de pingouin kütüphanesinden korelasyon analizini gerçekleştirelim

anlam = pg.pairwise_corr(data=getiri)
pd.set_option("display.max_rows",None)
print(anlam)
print(anlam[anlam["p-unc"]<0.05])
# bu kadar bu şekilde :D