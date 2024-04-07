import pandas as pd
from zips import zips

cps = pd.read_csv('cps_sy1819.csv')

for zip in zips:
    count = len(cps[cps.Zip == zip])
    