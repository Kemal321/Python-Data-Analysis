"""""""""""""""""""""""""""""""""EKSİK GÖZLEM NASIL TESPİT EDİLİR ? """""""""""""""""""""""""""""""""""""""""

import pandas as pd 
import missingno as msno 
import matplotlib.pyplot as plt 
import seaborn as sns 

data = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python ile Veri analizi\nullDataExercise.xlsx")

# ilk olarak veri kümesi üzerinden describe fonksiyonunu kullanmıştık burada null değerler için 
# yine veri kümesi hakkında bilgi veren farklı bir fonksiyon olan info() ve isnull() ı kullanacağız.
print(data.info()) 
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 34 entries, 0 to 33
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   D1      29 non-null     float64
 1   D2      29 non-null     float64
 2   D3      28 non-null     float64
 3   D4      26 non-null     float64
dtypes: float64(4)
memory usage: 1.2 KB
None
Bu şekilde bir çıktı aldık Non-Null yani eksik olmayan sayımlarda farklı veri adetlerinin olduğu belli 
Buradan veri kümemizin eksik veri içerdiğini anladık şimdi isnull() fonksiyonunu kullanarak bunlar hakkında kısa bilgi alalım
"""

print(data.isnull())
"""       D1     D2     D3     D4
0   False  False  False  False
1   False  False  False  False
2   False  False  False  False
3   False  False  False  False
Bu şekilde bir döngü dönüyor ve True olanlar null dur. ben uzun olduğu için satırları sildim maksat görmek yeterli
"""
# sayısı için 2 fonksiyonu kombine edelim
print(data.isnull().sum()) 
"""
D1    5
D2    5
D3    6
D4    8  Bu şekilde her bir sütunda kaç eksik veri olduğunu bize dönmüş oluyor.
"""

# hangi satırda veya sütunda eksik veri olduğunu bulmak ve görmek için farklı fonksiyonları mantığa göre kombine ederiz mesela
print(data[data.isnull().any(axis=1,)])
"""
df.isnull().any()
a     True
b    False
c     True
d    False
dtype: bool 

Normalde bu şekilde bir dönüte sahip iken kurduğumuz yapı ile aslında bunu sağlamış olduk benzer olarak 
df[df.columns[df.isnull().any()]] -> bu şekilde de yapabiliriz. Burada aslında daha önce verileri parçalar iken yaptığımız şeyi yapıyoruz.

Buna göre çıktımız da 
       D1     D2     D3     D4 -> Bu şekilde satıra ve sütuna göre taranarak bize NaN değerin nerede olduğunu gösteriyor.  
9   30.05  30.90    NaN  31.97 -> Bu şekilde satıra ve sütuna göre taranarak bize NaN değerin nerede olduğunu gösteriyor.
12    NaN    NaN  29.22  29.50 -> Bu şekilde satıra ve sütuna göre taranarak bize NaN değerin nerede olduğunu gösteriyor.
14  29.88  30.77    NaN  29.27 -> Bu şekilde satıra ve sütuna göre taranarak bize NaN değerin nerede olduğunu gösteriyor.
15    NaN  27.92  31.72    NaN -> Bu şekilde satıra ve sütuna göre taranarak bize NaN değerin nerede olduğunu gösteriyor.
16  27.22  29.78    NaN  30.35 -> Bu şekilde satıra ve sütuna göre taranarak bize NaN değerin nerede olduğunu gösteriyor.
17    NaN  30.17  31.58    NaN -> Bu şekilde satıra ve sütuna göre taranarak bize NaN değerin nerede olduğunu gösteriyor.
18  27.87    NaN    NaN  31.31 -> Bu şekilde satıra ve sütuna göre taranarak bize NaN değerin nerede olduğunu gösteriyor.
19    NaN  30.27  27.40    NaN -> Bu şekilde satıra ve sütuna göre taranarak bize NaN değerin nerede olduğunu gösteriyor.
"""

# bunları görselleştirerek de bakabiliriz aslında bunun için kullanabileceğimiz missingno adlı bir kütüphaneyi kullanacağız.
msno.bar(data)   # Bunları yorumlamak kolay zaten bunlar için dökümantasyona bakmak daha mantıklı yazarsak çok yer kaplar.
msno.matrix(data)# Bunları yorumlamak kolay zaten bunlar için dökümantasyona bakmak daha mantıklı yazarsak çok yer kaplar.
plt.show()

# daha büyük bir veri seti kullanalım mesela seaborn da var demiştik onlar üzerinde çalışalım
data2 = sns.load_dataset("titanic")
msno.matrix(data2)
plt.show()