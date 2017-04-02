from service.Canias.Integration import Canias

""" BASIC REPORTS """
""" ------------- """

class SalesReports:
    # Returns the Sales Trend
    def salesTrend(self, barea, startdate, enddate):
        return (Canias().run('JZNAPISALESTREND', str(barea) + '$' + str(startdate) + '$' + str(enddate)))

    # Returns the Sales Performance Report for Salesman
    def salesPerformance(self, barea, startdate, enddate):
        return (Canias().run('JZNAPISALESPERFORMANCE', str(barea) + '$' + str(startdate) + '$' + str(enddate)))

    # Returns raw Data Set for all Sales Related Data
    def rawData(self, barea, startdate, enddate):
        return (Canias().run('JZNAPISALESRAW', str(barea) + '$' + str(startdate) + '$' + str(enddate)))