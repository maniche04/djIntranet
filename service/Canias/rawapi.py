from service.Canias.Integration import Canias
from service.Canias.sales.reports import SalesReports

""" BASIC REPORTS """
""" ------------- """

class rawAPI:
    # Returns the Sales Trend
    def runSQL(self, query):
        query = str(query).replace(',','#') + ' INTO QUERYRESULTTABLE'
        return (Canias().run('JZNAPIRAWQUERYGET', query))