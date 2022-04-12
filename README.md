# gnss_downloads
1.Usage: 
Step1:Download gnss_download.py and Time_Convert_Tools.py 
Step2:Create a directory named Data in the same directory
Step3:Scripts could be execute in terminal
command:python3 gnss_download.py year1 month1 day1 year2 month2 day2 data_type [option]
year1:			start_year 
month1:			start_month
day1:			start_day
year2:			end_year
month2:			end_month
day2:			end_day
data_type:		obs sp3 clk dcb nav
option[obs]:		MGEX GNSS station name(https://igs.org/network/#station-map-list)
option[sp3]:		Analysis Center Name(COD,GRG,GFZ,WUM,SHA,JAX)
option[clk]:		Analysis Center Name(COD,GRG,GFZ,WUM,SHA,JAX)
option[dcb]:		Analysis Center Name(GFZ,WUM)
option[nav]:
example:
	python3 gnss_download.py 2022 02 02 2022 02 22 obs HKWS JFNG
	python3 gnss_download.py 2022 02 02 2022 02 22 sp3 GFZ SHA
	python3 gnss_download.py 2022 02 02 2022 02 22 clk GFZ WUM		      
	python3 gnss_download.py 2022 02 02 2022 02 22 dcb WUM GFZ
	python3 gnss_download.py 2022 02 02 2022 02 22 nav
2. The broadcast ephemeris is IGS mix ephemeris
