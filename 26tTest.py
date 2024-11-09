from scipy import stats
import pandas as pd
data = pd.read_excel(r"C:\Users\Kemalettin\Desktop\sinav.xlsx")
print(data)

alpha = 0.05
thetaCalc, pVal = stats.ttest_1samp(data,popmean=28,alternative="two-sided")
print(thetaCalc,pVal)

if pVal<alpha:
    print("H0 Reddedildi")
else:
    print("H0 Reddedilemez")
