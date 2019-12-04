import os
from os import path
import calendar
import re
import datetime as dt

#make dictionary of months, first three letters and number
months_dict=dict((v.lower(),str(k).zfill(2)) for k,v in enumerate(calendar.month_abbr))
months_dict.pop('')

#make a dict of week days, first three letters and full word
keys = [day.lower() for day in list(calendar.day_abbr)]
values = list(calendar.day_name)
weekdays_dict = dict(zip(keys, values))

#make a dict of weekdays, numbering according to datetime object and first three letters
keys= list(range(0,8))
values = [day.lower() for day in list(calendar.day_abbr)]
weekdaysnumbered_dict = dict(zip(keys, values))

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

def fixdirectory(dir):
    for oldname in next(os.walk(dir))[1]:
        new_dir_name = ''
        #print (type(directories))
        directory = re.sub(",", " ",oldname)
        match = re.search(r'(\d+-\d+-\d+)',directory)
        if match:
            new_dir_name=addweekday(oldname,directory)
        else:
            print(directory)
            new_dir_name=fixfolder(oldname,directory)
        os.rename(dir+os.sep+oldname,dir+os.sep+new_dir_name)
        #print ("file renamed")
        
def fixfolder(oldname,directory):
    directory = directory.split()
    year,month,day,weekday=[""]*4
    for part in directory:
        #print (part)
        piece=part.lower()
        if piece in years:
            year=piece
        if piece[:3] in months_dict.keys():
            month=(months_dict[piece[:3]])
            #print(int(month))
        if piece.zfill(2) in days:
            day=piece.zfill(2)
            #print(int(day))
        #weekday=weekdaysnumbered_dict[dt.datetime(year,int(month),int(day)).weekday()].capitalize()
    if year == "" or month == "" or day == "":
        new_dir_name = manualrename(oldname,directory)
    else:
        try:
            weekday = dt.datetime.strptime(month+ " " + day + " " + year,"%m %d %Y").strftime("%A")[:3]
            new_dir_name=year+'-'+month+'-'+day+'-'+ weekday
        except ValueError:
            new_dir_name = manualrename(oldname,directory)
    print ("old name:",oldname,"new name:",new_dir_name)
    return new_dir_name

def manualrename(oldname,directory):
    new_dir_name = input("Please manually enter the new name for %s"%oldname)
    if new_dir_name =="": 
        new_dir_name = oldname
    else:
        new_dir_name=addweekday(new_dir_name,directory)
    return new_dir_name

def addweekday(oldname,directory):
    year,month,day=oldname.split('-',3)
    #print (year,month,day)
    try:
        weekday=weekdaysnumbered_dict[dt.datetime(int(year),int(month),int(day)).weekday()].capitalize()
        new_dir_name=year+'-'+month+'-'+day+'-'+ weekday
        #print ("old name:",oldname,"new name:",new_dir_name)
        return new_dir_name
    except ValueError:
        print ('day is out of range for month')
        new_dir_name = manualrename(oldname)
        
if __name__ == "__main__":
    dir=input("what directory would you like to process?")
    fixdirectory(dir)