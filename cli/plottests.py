import os
os.chdir('/home/manish/intranet')

from service.Canias import Integration
from service.Canias.sales.reports import SalesReports
from service.Canias.rawapi import rawAPI
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats.stats import pearsonr

#salesdata = rawAPI().runSQL(
#    "SELECT B.CREATEDAT, B.CURRENCY, B.CUSTOMER, B.DOCNUM, B.DOCTYPE, B.EXCHRATE, B.GRANDTOTAL, B.QUANTITY, B.MATERIAL, B.SALDEPT FROM IASSALHEAD A LEFT JOIN IASSALITEM B ON A.DOCTYPE = B.DOCTYPE AND A.DOCNUM = B.DOCNUM WHERE A.DOCTYPE IN ('RI','RC') AND A.BUSAREA = '50' AND A.VALIDFROM >= '2016-01-01' AND A.VALIDFROM <= '2016-12-31'")

#data = pd.read_json(salesdata)
#
# sns.set_style("white", {"font.family": [u'Cantarell']})
# plt.plot(data.HOUR, data.QUANTITY)
# plt.ylabel('Quantity')
# plt.xlabel('Hour')
# plt.show()

#data.to_csv('salesData.csv',sep=',')

data = pd.read_csv('salesData.csv',sep=',')

dataitem = data[data['MATERIAL'] == 'CH033010051001-00080-0050']

