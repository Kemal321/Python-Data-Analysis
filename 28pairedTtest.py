from scipy import stats
import numpy as np
import pandas as pd

data = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python ile Veri analizi\okul.xlsx")
print(data)

"""
Verilerimiz elle oluşturulmuş örnek olsun diye yapıyoruz o yüzden varsayımların hepsinin geçerli olduğunu varsayıyoruz :D
ilk olarak formül üzerinden yapalım mesela.

H0:MÜ1 = MÜ2
H1:MÜ1 != MÜ2

İlk hipotezimizi kurduk 

alpha = 0.05 %95 güven ile yapmak istediğimizi belirttik

şimdi varyans hesaplayalım
"""
alpha = 0.05
var1 = np.var(data["A Okulu"],ddof=1)
var2= np.var(data["B Okulu"],ddof=1)

# ortak varyans için bir formül yok o yüzden direktmen kullanalım
# Her iki grubun örnek boyutları
n1 = len(data["A Okulu"])
n2 = len(data["B Okulu"])

# Ortak varyans hesaplama
pooled_variance = ((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2)


Thesap = (np.average(data["A Okulu"]) - np.average(data["B Okulu"]))/np.sqrt(pooled_variance*((1/n1)+1/n2))

print(f"A okulunun varyans değeri: {var1}\nB okulunun varyans değeri: {var2}")
print("Ortak Varyans: ", pooled_variance)
print(f"Hesaplanan t değeri {Thesap}")

# tablodan n1+n2-2 serbestlik derecesine sahip alpha = 0.05 değere baktık ve 2,12 çıktı 
# sonuç olarak thesap > ttablo olduğu için H0 red edilmiş oldu.

# Python ın kendi fonksiyonları ile yapalım.

tthesap, p = stats.ttest_ind(data["A Okulu"],data["B Okulu"],alternative="two-sided")
print(tthesap,p)

if p<alpha:
    print("H0 reddedildi.")
else:
    print("H0 reddedilemez")

"""
Varyansların homojenliğini test amaçlı bir örnek yapacağız. Veriler excel de random bir şekilde üretildi.
"""

data2 = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python ile Veri analizi\harcama.xlsx")
print(data2)

# erkek ve kadınları ayıralım
erkek = data2[data2["Cinsiyet"] == "Erkek"]
kadın = data2[data2["Cinsiyet"] == "Kadın"]

# kadın ve erkek için shapiro dayının testini uygulayalım mesela orada bağımlı değişkenler üzerinden yapıyorduk yani harcama üzerinden yapacaz
pe = stats.shapiro(erkek["Harcama"])
pk = stats.shapiro(kadın["Harcama"])
print(pe.pvalue,pk.pvalue) # bu shapiro dayı için tabi ki de. Varyanslar ile ilgili bir sorun olduğunu düşündüğümüz de levene veya barlett dedik

# hemen bir levene yapalım. Levene daha çok kullanıldığı için onu yapacağız tabi ki
h1 = stats.levene(erkek["Harcama"],kadın["Harcama"],center="mean") # burada center dediğimiz şey ortalama etrafında levene hesaplamasını istemek
# normalde notlarda ne dedik median etrafında bakılır dedik. Genel olan budur spss gibi programlarda her ikisini de verir 
#python default olarak bırakıldığın da mean'a göre dönüş yapar.

print(h1.pvalue) #sonuç olarak 0.20606634987237799 bunu döndü 0.05 den büyük olduğu için %95 olasılıkla H0 reddedilemez diyerek yorumladık 
# yani varyanslarımızın homojen bir şekilde dağıldığını görmüş olduk.

h2 = stats.bartlett(erkek["Harcama"],kadın["Harcama"])
print(h2.pvalue)
# 0.27416489265871996 bartlett ile p value bu çıktı bunun ile de aynı yorumu yapacağız tabi. Varyans homojenliği testleri bu şekilde
# tabi ki hepsi yok mesela f testini yapmadık bence gerek yok yeter ya 2 tane adam olana çok. 

data3 = pd.read_excel(r"C:\Users\Kemalettin\Desktop\anlasekon\Python ile Veri analizi\sigara.xlsx")

içen = data3[data3["Sigara"]=="Evet"]
içmeyen = data3[data3["Sigara"]=="Hayır"]

normicen = stats.shapiro(içen["Zaman"])
normicmeen = stats.shapiro(içmeyen["Zaman"])

homojen = stats.bartlett(içen["Zaman"],içmeyen["Zaman"])
test = stats.ttest_ind(içen["Zaman"],içmeyen["Zaman"],alternative="two-sided")

print(normicen.pvalue,normicmeen.pvalue,homojen.pvalue)
print(test.pvalue)

# daha önce belirttiğimiz welch t test i parametre olarak ttest fonksiyonuna equal_var = False yaparsak kendisi hesap eder.
# bağımlı t testi ise stats.ttest_rel(veriÖnceki, veriSonraki,alternative=kuyrukYapısı) relation yani ilişki olacak. 


