import pandas as pd
from scipy import stats

data = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python ile Veri analizi\chiDs.xlsx")


# Bu şekilde frekansları tek seferde bulabiliriz.
frequencyTable = pd.value_counts(data["Kilo"])
print(frequencyTable)

chis, pval = stats.chisquare(frequencyTable)
print(chis,pval) # 5.32 0.06994822174465536
"""
P > 0.05 olduğu için H0 hipotezini reddedemiyoruz. yani gözlemlediğimiz değer ile 
beklenen değer arasında anlamlı bir farklılık yok demektir. 

Chisquare testini yaparken aldığımız verinin frekanslarına ayrılıp ayrılmadığına göre 
çalışacağız çünkü yukarıdaki fonksiyon frekanslar üzerinden çalışıyor görüldüğü üzere
o yüzden bize gelen veri seti eğer frekanslarına ayrılarak geldiyse onu vereceğiz 
frekanslarına ayrılmadan gelmiş ise eğer o zaman frekanslarına ayıracağız.
"""