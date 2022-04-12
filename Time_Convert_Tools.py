import math
class time_convert_tools:
    # leap year or not

    def if_leap_year(self, year):
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        elif year % 4 == 0:
            return True
        else:
            return False

    def month_day_list(self, year):
        if self.if_leap_year(year):
            day_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return day_list

    def Julian2MJD(self, year, month, day, hours, minute, sec):
        if (month > 2):
            Y = year
            M = month
        else:
            Y = year - 1
            M = month + 12
        D = day + hours / 24 + minute / 1440 + sec / 86400
        A = int(Y / 100)
        B = 2 - A + int(A / 4)
        JD = int(365.25 * (Y + 4716)) + int(30.6001 * (M + 1)) + D + B - 1524.5
        MJD = JD - 2400000.5
        return MJD

    def MJD2Julian(self, MJD):
        JD = MJD + 2400000.5
        JD = JD + 0.5
        Z = math.floor(JD)
        F = JD - Z
        if Z < 2299161:
            A = Z
        else:
            a = math.floor((Z - 2305507.25) / 36524.25)
            A = Z + 10 + a - math.floor(a / 4)
        k = 0
        while True:
            B = A + 1524
            C = math.floor((B - 122.1) / 365.25)
            D = math.floor(365.25 * C)
            E = math.floor((B - D) / 30.6)
            day = B - D - math.floor(30.6 * E) + F
            if day >= 1: break
            A -= 1
            k += 1
        month = E - 1 if E < 14 else E - 13
        year = C - 4716 if month > 2 else C - 4715
        day += k
        if int(day) == 0: day += 1

        hours = math.floor((day - math.floor(day))*24)
        minute = math.floor((day - math.floor(day))*24 - hours)*60
        second = (day - math.floor(day))*86400 - hours*3600 - minute*60

        day = math.floor(day)

        date = [year,month,day,hours,minute,second]
        return date

    def Julian2GPS_week_day(self, year, month, day):
        MJD0 = self.Julian2MJD(1980, 1, 6, 0, 0, 0)
        MJD = self.Julian2MJD(year, month, day, 0, 0, 0)
        d_day = MJD - MJD0
        GPS_week = int(d_day / 7)
        GPS_day = int(d_day % 7)
        GPS_week_day = [GPS_week, GPS_day]
        return GPS_week_day

    def Julian2GPS_week_sow(self, year, month, day, hours, minute, sec):
        MJD0 = self.Julian2MJD(1980, 1, 6, 0, 0, 0)
        MJD_day = self.Julian2MJD(year, month, day, 0, 0, 0)
        d_day = MJD_day - MJD0
        GPS_week = int(d_day / 7)
        GPS_day = int(d_day % 7)
        GPS_sow = GPS_day * 86400 + hours * 3600 + minute * 60 + sec
        GPS_week_sow = [GPS_week, GPS_sow]
        return GPS_week_sow

    def Julian2DOY(self, year, month, day):
        month_day_list = self.month_day_list(year)
        DOY = 0
        for m in range(1, month):
            DOY = DOY + month_day_list[m - 1]
        DOY = DOY + day
        return DOY

    def DOY2Julian(self, year, DOY):
        month_day_list = self.month_day_list(year)
        sum_month_day_list = []
        for month in range(0,12):
            sum_month_day_list.append(sum(month_day_list[0:month+1]))
        month = 1
        while(DOY>sum_month_day_list[month-1]):
            month = month + 1
        day = DOY - sum_month_day_list[month-2]
        date = [year,month,day]
        return date