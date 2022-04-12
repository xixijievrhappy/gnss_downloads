# gnss_downloads
1.Usage:<br>
	Step1:Download gnss_download.py and Time_Convert_Tools.py<br>
	Step2:Create a directory named Data in the same directory<br>
	Step3:Scripts could be execute in terminal<br>
	
	command:python3 gnss_download.py year1 month1 day1 year2 month2 day2 data_type [option]<br>
	
	year1:       		start_year<br>
	month1:    		start_month<br>
	day1:        		start_day<br>
	year2:			end_year<br>
	month2:			end_month<br>
	day2:			end_day<br>
	data_type: 		data type option: obs sp3 clk dcb nav<br>
	option[obs]:		MGEX GNSS station name(https://igs.org/network/#station-map-list)<br>
	option[sp3]:		Analysis Center Name(COD,GRG,GFZ,WUM,SHA,JAX)<br>
	option[clk]:		Analysis Center Name(COD,GRG,GFZ,WUM,SHA,JAX)<br>
	option[dcb]:		Analysis Center Name(GFZ,WUM)<br>

	example: python3 gnss_download.py 2022 02 02 2022 02 22 obs HKWS JFNG<br>
		 python3 gnss_download.py 2022 02 02 2022 02 22 sp3 GFZ SHA<br>
		 python3 gnss_download.py 2022 02 02 2022 02 22 clk   GFZ WUM<br>		       
		 python3 gnss_download.py 2022 02 02 2022 02 22 dcb WUM GFZ<br>		       
		 python3 gnss_download.py 2022 02 02 2022 02 22 nav<br> 
2. The broadcast ephemeris is IGS mix ephemeris
