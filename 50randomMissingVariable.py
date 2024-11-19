import pandas as pd 
import missingno as msno 
import matplotlib.pyplot as plt 

data = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python ile Veri analizi\nullDataExercise.xlsx")

# eğer ham datalarımızın zarar görme tehlikesini yok etmek istiyorsak ki neden istemeyelim bu noktada ana veriyi kopyalayarak kopya üzerinden 
# ilerlemek her zaman mantıklı ve kullanılan bir yöntemdir.
data2 = data.copy()

msno.matrix(data2) # matriks yapısından eksik verilerimizin varlığı ve nasıl olduğuna dair bir ön bilgi alalım
plt.show()

"""
Korelasyon sorgulamasını yapmak için tahmin edebileceğimiz gibi bir çok yöntem olacaktır çünkü yaptığımız şey belli ve basit 
eksik olan değerlere 0 atamak ve tam verilere 1 değeri atayarak bunlar arasında pearson korelasyon testi uygulamak.
"""

# ilk olarak isnull() ile yapılan yönteme bakalım
data2[~data2.isnull()] = 1
data2[data2.isnull()] = 0  
print(data2)
"""
     D1   D2   D3   D4-> Bu şekilde bir çıktı elde etmiş olduk.
0   1.0  1.0  1.0  1.0-> Bu şekilde bir çıktı elde etmiş olduk.
1   1.0  1.0  1.0  1.0-> Bu şekilde bir çıktı elde etmiş olduk.
2   1.0  1.0  1.0  1.0-> Bu şekilde bir çıktı elde etmiş olduk.
3   1.0  1.0  1.0  1.0-> Bu şekilde bir çıktı elde etmiş olduk. 
"""
# farklı bir metoda bakalım.
data3 = data.copy()
data4 = data3.notnull().astype("int")
print(data4)
"""
    D1  D2  D3  D4-> Bu şekilde bir çıktı elde etmiş olduk.
0    1   1   1   1-> Bu şekilde bir çıktı elde etmiş olduk.
1    1   1   1   1-> Bu şekilde bir çıktı elde etmiş olduk.
2    1   1   1   1-> Bu şekilde bir çıktı elde etmiş olduk.
3    1   1   1   1-> Bu şekilde bir çıktı elde etmiş olduk.
4    1   1   1   1-> Bu şekilde bir çıktı elde etmiş olduk.
"""

# artık bunu yaptıktan sonra dediğimiz gibi basitçe korelasyona bakabiliriz.
print(data3.corr())
"""
          D1        D2        D3        D4-> Çıkan sonuçlarda kayda değer yüksek değer var ise işte o zaman H0 reddedilmez ve sıkıntı çıkar.
D1  1.000000  0.075709 -0.345358 -0.119400-> Çıkan sonuçlarda kayda değer yüksek değer var ise işte o zaman H0 reddedilmez ve sıkıntı çıkar.
D2  0.075709  1.000000 -0.121263  0.207372-> Çıkan sonuçlarda kayda değer yüksek değer var ise işte o zaman H0 reddedilmez ve sıkıntı çıkar.
D3 -0.345358 -0.121263  1.000000  0.385670-> Çıkan sonuçlarda kayda değer yüksek değer var ise işte o zaman H0 reddedilmez ve sıkıntı çıkar.
D4 -0.119400  0.207372  0.385670  1.000000-> Çıkan sonuçlarda kayda değer yüksek değer var ise işte o zaman H0 reddedilmez ve sıkıntı çıkar.
"""