import os
from os import path
import calendar
import re
import datetime as dt

months_dict=dict((v.lower(),str(k).zfill(2)) for k,v in enumerate(calendar.month_abbr))
keys = [day.lower() for day in list(calendar.day_abbr)]
values = list(calendar.day_name)
weekdays_dict = dict(zip(keys, values))
years = ['2014','2015','2016','2017','2018','2019']
days = [str(r).zfill(2) for r in range(1,32)]
months = ['april',
 'august',
 'december',
 'february',
 'january',
 'july',
 'june',
 'march',
 'may',
 'november',
 'october',
 'september'] 

for directories in next(os.walk('.'))[1]:
    new_dir_name = ''
    #print (type(directories))
    directory = re.sub(",", " ",directories)
    directory = directory.split()
    #print (directory)
    year,month,day,weekday=[""]*4
    for part in directory:
        piece=part.lower()
        if piece in years:
            year=piece
        if piece[:3] in months_dict.keys():
            month=(months_dict[piece[:3]])
        if piece.zfill(2) in days:
            day=piece.zfill(2)
        if piece[:3] in weekdays_dict.keys():
            weekday=(weekdays_dict[piece[:3]])
    if year == "" or month == "" or day == "":
        print (directory)
        new_dir_name = input("Please manually enter the new name for %s"%directories)
        if new_dir_name =="": new_dir_name = directories
    elif weekday == "":
        weekday = dt.datetime.strptime(month+ " " + day + " " + year,"%m %d %Y").strftime("%A")
        new_dir_name=year+'-'+month+'-'+day+'-'+ weekday[:3]
    else:    
        new_dir_name=year+'-'+month+'-'+day+'-'+ weekday[:3]
    print ("old name:",directories,"new name:",new_dir_name)
    os.rename(directories,new_dir_name)
    input('continue?')