import pandas as pd 
import statsmodels.api as sm
import statsmodels.stats.diagnostic as smd 

data = pd.read_csv(r"C:\Users\Kemalettin\Desktop\anlasekon\Python ile Veri analizi\Veri Önişleme Proje\Simple Linear Regression\Advertising.csv")

data2 = data.copy()
y = data2["Sales"]
x = data2[["TV","Radio"]] # newspaper zaten kötüydü onu çıkardık. 

const = sm.add_constant(x)
model=sm.OLS(y,const).fit()
print(model.summary())

# white test i kullanacağız varyans sabitliğini test etmek için 
whitetest = smd.het_white(model.resid, model.model.exog)
print(whitetest)
# son değer pvalue değerimizdir işte buna bakacaz ve e-15ler gelmiş o yüzden çok küçük

BPtest = smd.het_breuschpagan(model.resid,model.model.exog)
print(BPtest) # bu da farklı bir testimiz aynı amaçlı. Sonuçlarında zaten son değerimiz yine p value verir buradan bakarız.
# ikisi arasındaki fark white testi daha çok t testi gibidir yani normallik testinden geçemedi hatalarımız ama merkezi limit teoremine 
# atfen devam etmek istiyoruz. İşte o zaman onu kullanacağız ama biz daha çok zaten onu kullanacağız :d 