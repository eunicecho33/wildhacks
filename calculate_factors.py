import pandas as pd
from zips import zips

cps = pd.read_csv('cps_sy1819.csv')

factors = pd.DataFrame(columns = ['zip', 'safety', 'grad', 'college', 'sat'])
print(factors)

# i = 0
# for zip in zips:
#     count = len(cps[cps.Zip == zip])
#     pop = cps.loc[cps['Zip'] == zip, 'Population'].sum()
#     cps.at[i, 'zip'] = zip
# print(cps.loc[cps['Zip'] == 60610])
# lst = [x + y for x, y in zip(cps.loc[cps['Zip'] == 60610]['Graduation_School_Pct'], cps.loc[cps['Zip'] == 60610]['Population'])]

for zip in zips:
    temp = cps[cps['Zip'] == zip]
    lst = [x/y for (x, y) in (temp['School_Survey_Safety'], temp['Population'])]
    print(lst)