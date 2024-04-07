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
    temp = cps.loc[(cps['Zip'] == zip) & (cps['Graduation_School_Pct'].notnull() == True) & (cps['Population'].notnull() == True)]
    if len(temp) != 0:
        temp_pop = temp['Population'].sum()
        temp['num'] = temp.apply(lambda row: row.Graduation_School_Pct * (row.Population / temp_pop), axis=1)
        print(temp['num'])
    else:
        # print(float('NaN'))
        print('none')
        pass
    # create col num: grad / temp_pop
    # sum of num