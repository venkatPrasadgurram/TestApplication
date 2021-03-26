import datetime, calendar

def test_date_validation(st_date, end_date):
	try:
		st_date = datetime.datetime.strptime(st_date, '%Y%m%d')
		end_date = datetime.datetime.strptime(end_date, '%Y%m%d')
		st_year = st_date.year
		end_year = end_date.year

		st_date_val = int(str(st_date).split(" ")[0].replace('-',''))
		end_date_val = int(str(end_date).split(" ")[0].replace('-',''))

		if st_date_val>=end_date_val:
			starting_date = input("Please Enter the Starting Date:\n from the following format(YYYYDDMM) ex:year above 1900:\n")
			ending_date = input("Please Enter the Ending Date:\n from the following format(YYYYDDMM) ex:year below 2100 :\n")
			test_date_validation(starting_date, ending_date)

		elif 1900<int(st_year) and int(end_year)<2100:
			return st_date, end_date
		else:
			starting_date = input("Please Enter the Starting Date:\n from the following format(YYYYDDMM) ex:year above 1900:\n")
			ending_date = input("Please Enter the Ending Date:\n from the following format(YYYYDDMM) ex:year below 2100 :\n")
			test_date_validation(starting_date, ending_date)

	except:
		starting_date = input("Please Enter the Starting Date:\n from the following format(YYYYDDMM) ex:20200101:\n")
		ending_date = input("Please Enter the Ending Date:\n from the following format(YYYYDDMM) ex:20210101 :\n")

		test_date_validation(starting_date, ending_date)

def get_devisible_by_5_date(sat_week,month, year):
	saturday_date = sat_week[calendar.SATURDAY]
	
	if saturday_date%5==0 and saturday_date!=0:
		saturday_date = str(saturday_date).zfill(2)
		month = str(month).zfill(2)
		saturday_date = '%s%s%s'%(str(year), month, saturday_date)
		saturday_date = int(saturday_date)
		return saturday_date
	else:
		return ''

def get_saturday_dates_between_st_end_dates(st_date, end_date):
	saturday_li = []
	st_date_val = int(str(st_date).split(" ")[0].replace('-',''))
	end_date_val = int(str(end_date).split(" ")[0].replace('-',''))

	st_year = st_date.year
	end_year = end_date.year
	for year in range(st_year, end_year+1):
		for month in range(1,13):
			cal = calendar.monthcalendar(year, month)
			
			first_week  = cal[0]
			second_week = cal[1]
			third_week  = cal[2]
			forth_week  = cal[3]
			fivth_week  = cal[4] if len(cal)==5 else ''

			if first_week[calendar.SATURDAY]:
				saturday_date = forth_week[calendar.SATURDAY]

			elif third_week:
				saturday_date = third_week[calendar.SATURDAY]
			saturday_date = str(saturday_date).zfill(2)
			if len(saturday_date) ==2:
				month = str(month).zfill(2)
				saturday_date = '%s%s%s'%(str(year), month, saturday_date)
			saturday_date = int(saturday_date)

			if saturday_date not in saturday_li and st_date_val<=saturday_date<=end_date_val:
				saturday_li.append(saturday_date)
			first_sat_date = get_devisible_by_5_date(first_week, month, year)

			if first_sat_date and first_sat_date not in saturday_li and st_date_val<=first_sat_date<=end_date_val:
				saturday_li.append(first_sat_date)

			second_sat_date = get_devisible_by_5_date(second_week, month, year)
			if second_sat_date and second_sat_date not in saturday_li and st_date_val<=second_sat_date<=end_date_val:
				saturday_li.append(second_sat_date)

			third_sat_date = get_devisible_by_5_date(third_week, month, year)
			if third_sat_date and third_sat_date not in saturday_li and st_date_val<=third_sat_date<=end_date_val:
				saturday_li.append(third_sat_date)

			forth_sat_date = get_devisible_by_5_date(forth_week, month, year)
			if forth_sat_date and forth_sat_date not in saturday_li and st_date_val<=forth_sat_date<=end_date_val:
				saturday_li.append(forth_sat_date)

			if fivth_week:
				fivth_sat_date = get_devisible_by_5_date(fivth_week, month, year)
				if fivth_sat_date and fivth_sat_date not in saturday_li and st_date_val<=fivth_sat_date<=end_date_val:
					saturday_li.append(fivth_sat_date)

	return saturday_li


if __name__ == "__main__":
	starting_date = input("Please Enter the Starting Date:\n from the following format(YYYYDDMM):\n")
	ending_date = input("Please Enter the Ending Date:\n from the following format(YYYYDDMM):\n")

	starting_date, ending_date = test_date_validation(starting_date, ending_date)
	saturday_li = get_saturday_dates_between_st_end_dates(starting_date, ending_date)
	
	saturday_li = sorted(saturday_li, key=abs)
	print(saturday_li)

