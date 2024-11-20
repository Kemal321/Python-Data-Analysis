import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import statsmodels.api as sm 

data = sns.load_dataset("tips")

data2 = data.copy()

# verimizde bulunan toplam fatura ile bahşiş arasında bir ilişki beklentisi içerisindeyiz 
# bunu anlamak için öncelikle bir grafikten kontrol ederiz 
sns.regplot(x=data2["total_bill"],y=data2["tip"],ci=None)
plt.show()

# daha önceki veri ön işleme adımlarından ari olarak sadece lineer regresyonun anlamak ve onun üzerinde çalışmak için 
# yapıyorum yani normalde o adımlar yapıldıktan sonra bunlar yapılmalı çünkü aralarında aykırı değerler olabilir bu da hatayı gereksiz
# daha doğrusu anlamsız arttırabilir.

sabit = sm.add_constant(data2["total_bill"])
bağımlıdeğişkenDV = data2["tip"]

model = sm.OLS(bağımlıdeğişkenDV, sabit).fit()
print(model.summary()) # bu şekilde modelimiz hakkında özet bilgileri açtık burada ilk bakmamız gereken sabit 
"""
                            OLS Regression Results
==============================================================================
Dep. Variable:                    tip   R-squared:                       0.457
Model:                            OLS   Adj. R-squared:                  0.454
Method:                 Least Squares   F-statistic:                     203.4
Date:                Thu, 21 Nov 2024   Prob (F-statistic):           6.69e-34
Time:                        00:37:11   Log-Likelihood:                -350.54
No. Observations:                 244   AIC:                             705.1
Df Residuals:                     242   BIC:                             712.1
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
ilk bakılan ->   coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
ilk bakılan B0-> const          0.9203      0.160      5.761      0.000       0.606       1.235
Burası da B1 -> total_bill     0.1050      0.007     14.260      0.000       0.091       0.120
==============================================================================
Omnibus:                       20.185   Durbin-Watson:                   2.151
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               37.750
Skew:                           0.443   Prob(JB):                     6.35e-09
Kurtosis:                       4.711   Cond. No.                         53.0
==============================================================================

Yani model Yi = 0.9203+0.1050 * Xi(total_bill)
Yani bu nasıl yorumlanır satış olmasa bile ortalama gibi 0.9203 $ tip varmış 
aynı şekilde total_bill yani B1 değeri ise bize 1 birimlik total_bill artışına karşılık 0.1050 $ tip ( bahşiş ) artışı ( b1 kadar) 
artış olduğunu söyler aslında 

- yani bunun sorusu 1 birim total bill artışına karşılı tip teki değişme nedir ? demek sorusunun cevabıdır. 
"""