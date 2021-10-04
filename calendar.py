
class Calendar(object):
    def __init__(self, date_params):
        self.__month = date_params[0]
        self.__day = date_params[1]
        self.__year = date_params[2]
        self.__day_of_week = date_params[3]

    def match_day_quant(self):
        m = self.__month
        y = self.__year
        if m in ['September', 'April', 'June', 'November']:
            self.__number_of_days = 30
        elif m == 'Februrary':
            self.__number_of_days = 29 if not y % 4 and not y % 100 else 28
        else:
            self.__number_of_days = 31
    def number_of_days(self):
        return self.__number_of_days

