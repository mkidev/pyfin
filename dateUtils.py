'''
Created on 27.12.2015

@author: marcelkisilowski
'''
import datetime
from dateutil.relativedelta import relativedelta
def to_date(date):
    """Method converts string date to datetime date. You should use %Y-%m-%d format."""
    return datetime.datetime.strptime(date, '%d.%m.%Y').date()

def checkMonthsBetweenDates(startDate,endDate):
    rd = relativedelta(endDate,startDate)
    if abs(rd.years) > 0:
        months = abs(rd.years)*12 + abs(rd.months)
    else: 
        months = abs(rd.months)
    return months

def getDateList(startDate,endDate,maxMonth=6):
    """Liste mit Daten von startDate bis endDate. Gesplittet in maxMonth lange einheiten 
    bsp. getDateList(01.01.2012, 01.01.2013) -> {[01.01.2012,31.05.2012],[01.06.2012,01.01.2013]}"""