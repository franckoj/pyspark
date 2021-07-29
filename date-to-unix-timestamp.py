from_date ='2021-01-01'
to_date = '2021-04-30'
import datetime
#convert string to datetimeformat
f_date = datetime.datetime.strptime(from_date, "%Y-%m-%d")
t_date = datetime.datetime.strptime(to_date, "%Y-%m-%d")
  
#convert datetime to timestamp
  
ft_date = int(datetime.datetime.timestamp(f_date))
tt_date = int(datetime.datetime.timestamp(t_date))
