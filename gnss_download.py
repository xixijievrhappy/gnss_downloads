import sys
from ftplib import FTP
from Time_Convert_Tools import time_convert_tools

class gnss_downloads:

    def __init__(self,date,data_type,CODE):
        self.date = date
        self.data_type = data_type
        self.CODE = CODE  # Station or Analysis Center
        self.time_conv = time_convert_tools() # GNSS time convert tools

    def obs_downloads(self):
        local_path = './Data'
        bufsize = 1024
        year = date[0]
        DOY = self.time_conv.Julian2DOY(date[0],date[1],date[2])
        ftp = FTP('igs.ign.fr')
        ftp.login()
        ftp.cwd('/pub/igs/data')
        ftp.cwd(str(year))

        if DOY < 10:
            DOY_ = '00' + str(DOY)
        elif DOY < 100:
            DOY_ = '0' + str(DOY)
        else:
            DOY_ = str(DOY)

        ftp.cwd(DOY_)
        # get file information of DOY directory
        obs_list = []
        ftp.retrlines("LIST", obs_list.append)
        # find station crx file name
        for stat in self.CODE:
            for obs_name in obs_list:
                indx = obs_name.find(stat)
                if (indx != -1):
                    if ('crx' in obs_name):
                        file_name = obs_name[indx:]
                        print(file_name + '      download...')
            file = local_path + '/' + file_name
            fp = open(file, 'wb')
            ftp.retrbinary('RETR ' + file_name, fp.write, bufsize)
            fp.close()
        ftp.close()

    def sp3_downloads(self):
        local_path = './Data'
        bufsize = 1024
        GPS_week_day = self.time_conv.Julian2GPS_week_day(self.date[0],self.date[1],self.date[2])
        DOY = self.time_conv.Julian2DOY(self.date[0],self.date[1],self.date[2])
        ftp = FTP('igs.ign.fr')
        ftp.login()
        ftp.cwd('/pub/igs/products/mgex')
        ftp.cwd(str(GPS_week_day[0]))
        file_list = []
        ftp.retrlines("LIST",file_list.append)
        sp3_list = []
        for file_ in file_list:
            if('.SP3' in file_):
                sp3_list.append(file_)
        sp3_file_name = []
        # extract sp3 file
        for sp3 in sp3_list:
            for AC_ in self.CODE:
                indx = sp3.find(AC_)
                if(indx != -1):
                    if(str(DOY) in sp3[indx:]):
                        sp3_file_name.append(sp3[indx:])

        for sp3_name in sp3_file_name:
            print(sp3_name)
            print('Download...')
            file = local_path + '/' + sp3_name
            fp = open(file,'wb')
            ftp.retrbinary('RETR '+sp3_name,fp.write,bufsize)
            fp.close()
        ftp.close()

    def clk_downloads(self):

        local_path = './Data'
        bufsize = 1024
        GPS_week_day = self.time_conv.Julian2GPS_week_day(self.date[0], self.date[1], self.date[2])
        DOY = self.time_conv.Julian2DOY(self.date[0], self.date[1], self.date[2])
        ftp = FTP('igs.ign.fr')
        ftp.login()
        ftp.cwd('/pub/igs/products/mgex')
        ftp.cwd(str(GPS_week_day[0]))
        file_list = []
        ftp.retrlines("LIST", file_list.append)
        clk_list = []
        for file_ in file_list:
            if ('.CLK' in file_):
                clk_list.append(file_)
        clk_file_name = []
        # extract clk file
        for clk in clk_list:
            for AC_ in self.CODE:
                indx = clk.find(AC_)
                if (indx != -1):
                    if (str(DOY) in clk[indx:]):
                        clk_file_name.append(clk[indx:])

        for clk_name in clk_file_name:
            print(clk_name)
            print('Download...')
            file = local_path + '/' + clk_name
            fp = open(file, 'wb')
            ftp.retrbinary('RETR ' + clk_name, fp.write, bufsize)
            fp.close()
        ftp.close()

    def dcb_downloads(self):

        local_path = './Data'
        bufsize = 1024
        year = date[0]
        DOY = self.time_conv.Julian2DOY(date[0],date[1],date[2])
        ftp = FTP('igs.ign.fr')
        ftp.login()
        ftp.cwd('/pub/igs/products/mgex/dcb/'+str(year))

        if DOY < 10:
            DOY_ = '00' + str(DOY)
        elif DOY < 100:
            DOY_ = '0' + str(DOY)
        else:
            DOY_ = str(DOY)

        # get file information of DOY directory
        dcb_list = []
        ftp.retrlines("LIST", dcb_list.append)
        str_date = str(year) + DOY_
        for dcb in dcb_list:
            indx = dcb.find(str_date)
            indx1 = dcb.find('CAS')
            if(indx!=-1):
                file_name = dcb[indx1:]
                break
        if(indx==-1):
            print(str(year)+' '+DOY_+' dcb file not on the server...')
            print('please use .BIA file...')
            return False

        file = local_path + '/' + file_name
        fp = open(file, 'wb')
        ftp.retrbinary('RETR ' + file_name, fp.write, bufsize)
        fp.close()
        ftp.close()

    def nav_downloads(self):

        local_path = './Data'
        bufsize = 1024
        year = date[0]
        DOY = self.time_conv.Julian2DOY(date[0],date[1],date[2])
        ftp = FTP('igs.ign.fr')
        ftp.login()
        ftp.cwd('/pub/igs/data')
        ftp.cwd(str(year))

        if DOY < 10:
            DOY_ = '00' + str(DOY)
        elif DOY < 100:
            DOY_ = '0' + str(DOY)
        else:
            DOY_ = str(DOY)

        ftp.cwd(DOY_)
        # get file information of DOY directory
        nav_list = []
        ftp.retrlines("LIST", nav_list.append)
        for nav in nav_list:
            indx1 = nav.find('BRDC')
            indx2 = nav.find('IGS')
            if((indx1!=-1)and(indx2!=-1)):
                file_name = nav[indx1:]
                break

        if(indx2==-1):
            print('BRDC IGS navigation ephemeris not on the server...')
            return False

        file = local_path + '/' + file_name
        fp = open(file, 'wb')
        ftp.retrbinary('RETR ' + file_name, fp.write, bufsize)
        fp.close()
        ftp.close()


if __name__ == "__main__":

    time_conv_ = time_convert_tools()

    # input parameters from command line
    date_s = [int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])]  # start date: year,month,day
    date_e = [int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6])]  # end date: year,month,day
    data_type = sys.argv[7] # file typr: 'obs','sp3','clk','dcb','nav','snx','eop'
    if data_type.strip() == 'obs':

        station = sys.argv[8:]  # station name

        MJD_S = time_conv_.Julian2MJD(date_s[0],date_s[1],date_s[2],0,0,0)
        MJD_E = time_conv_.Julian2MJD(date_e[0],date_e[1],date_e[2],0,0,0)

        MJD = MJD_S
        while(MJD<=MJD_E):
            date = time_conv_.MJD2Julian(MJD)[0:3]
            dl = gnss_downloads(date, data_type, station)
            dl.obs_downloads()
            MJD += 1

    elif data_type.strip() == 'sp3':

        AC = sys.argv[8:]

        MJD_S = time_conv_.Julian2MJD(date_s[0], date_s[1], date_s[2], 0, 0, 0) # Cal Start Day MJD
        MJD_E = time_conv_.Julian2MJD(date_e[0], date_e[1], date_e[2], 0, 0, 0) # Cal End Day MJD

        MJD = MJD_S
        while (MJD <= MJD_E):
            date = time_conv_.MJD2Julian(MJD)[0:3]
            dl = gnss_downloads(date, data_type, AC)
            dl.sp3_downloads()
            MJD += 1
    elif data_type.strip() == 'clk':

        AC = sys.argv[8:]

        MJD_S = time_conv_.Julian2MJD(date_s[0], date_s[1], date_s[2], 0, 0, 0) # Cal Start Day MJD
        MJD_E = time_conv_.Julian2MJD(date_e[0], date_e[1], date_e[2], 0, 0, 0) # Cal End Day MJD

        MJD = MJD_S
        while (MJD <= MJD_E):
            date = time_conv_.MJD2Julian(MJD)[0:3]
            dl = gnss_downloads(date, data_type, AC)
            dl.clk_downloads()
            MJD += 1
    elif data_type.strip() == 'dcb':

        AC = ['CAS']

        MJD_S = time_conv_.Julian2MJD(date_s[0], date_s[1], date_s[2], 0, 0, 0) # Cal Start Day MJD
        MJD_E = time_conv_.Julian2MJD(date_e[0], date_e[1], date_e[2], 0, 0, 0) # Cal End Day MJD

        MJD = MJD_S
        while (MJD <= MJD_E):
            date = time_conv_.MJD2Julian(MJD)[0:3]
            dl = gnss_downloads(date, data_type, AC)
            flag = dl.dcb_downloads()
            MJD += 1

    elif data_type.strip() == 'nav':

        AC = ['IGS']

        MJD_S = time_conv_.Julian2MJD(date_s[0], date_s[1], date_s[2], 0, 0, 0)  # Cal Start Day MJD
        MJD_E = time_conv_.Julian2MJD(date_e[0], date_e[1], date_e[2], 0, 0, 0)  # Cal End Day MJD

        MJD = MJD_S

        while (MJD <= MJD_E):
            date = time_conv_.MJD2Julian(MJD)[0:3]
            dl = gnss_downloads(date, data_type, AC)
            flag = dl.nav_downloads()
            MJD += 1




