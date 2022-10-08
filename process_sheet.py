import pandas as pd
import numpy as np 

example_file = '/Users/skernytsky/Dropbox/personal_data/time_trackers/time_tracker_week_v20220918.xlsx'

import re 

a = re.sub('.xlsx','',re.sub('^.*?time_tracker_week_v','',example_file))

pd.Period(a)

import datetime
datetime.weekday('Monday')

import calendar

weekmap = {'Sunday':0,'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6}
weekmap


def calc_date(datestr,sheetname):
    return pd.Period(datestr)+weekmap[sheetname]


calc_date(a,'Saturday')
calc_date(a,'Sunday')



def process_week(excelfile):
    '''
    
    
    '''

    #Check that the string for the file is a sunday date. 

    #Loop across the days of the week and run the process_single_day script

    



def process_single_day(excelfile,weekday):

    ''' 
    This will take a sheet and process all the components

    1. Check the date given and the name of sheet 

    2. 
    *Args are the excel sheet and the name of the week. 
    if you give the sheet you can't compare the sheet name 
    bcause it's not stored anywhere 

    3. it then processes each row.

    Checks to add: 
        If any of the to-be filtered rows have data in the start end that looks like
        time data. print them out. 
        Make sure anywhere there is Total time, there is also a valid category 
    '''


    #First determine the proper date for this sheet 
    date_str = re.sub('.xlsx','',re.sub('^.*?time_tracker_week_v','',example_file))
    cln_date = pd.Period(date_str)+weekmap[weekday]

    #load data 
    df = (pd.read_excel(excelfile,skiprows=1,sheet_name=weekday)
        .loc[0:40,['Start','End','Total','Category1','Category2','Task']]
        .query("~Total.isnull()")
    )

    '''

        RETURN HERE 
        ADD checks 
        ADD in Aggs 

    '''


    #>>loc[0:13,['Start','End','Total','Category1','Category2','Task']]

#    return cln_date,df 
    return df
    #Trim data. remove comments below 

    #run checks on tasks

    #run checks on pero

    #Do aggregations

a = process_single_day(example_file,'Monday')[1]
a.assign(dropflag = lambda d: 1*d.Total.isnull())
a.assign(dropflag = lambda d: 1*d.Total.isnull().cummax())

a.query("~Total.isnull()")


b = process_single_day(example_file,'Tuesday')

c = process_single_day(example_file,'Wednesday')
c
process_single_day(example_file,'Thursday')
process_single_day(example_file,'Friday')
process_single_day(example_file,'Saturday')


#First rows that are all missing should be the flag

#If there is a row that has some of them populated immediately. 
#If there are any rows that have 
# It should warn and print that row 


import re 

a = re.sub('.xlsx','',re.sub('^.*?time_tracker_week_v','',example_file))

pd.Period(a)

import datetime
datetime.weekday('Monday')

import calendar

weekmap = {'Sunday':0,'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6}
weekmap


def calc_date(datestr,sheetname):
    return pd.Period(datestr)+weekmap[sheetname]


calc_date(a,'Saturday')
calc_date(a,'Sunday')



def process_week(excelfile):
    '''
    
    
    '''

    #Check that the string for the file is a sunday date. 

    #Loop across the days of the week and run the process_single_day script

    



def process_single_day(excelfile,weekday):

    ''' 
    This will take a sheet and process all the components

    1. Check the date given and the name of sheet 

    2. 
    *Args are the excel sheet and the name of the week. 
    if you give the sheet you can't compare the sheet name 
    bcause it's not stored anywhere 

    3. it then processes each row.

    '''


    #First determine the proper date for this sheet 
    date_str = re.sub('.xlsx','',re.sub('^.*?time_tracker_week_v','',example_file))
    cln_date = pd.Period(date_str)+weekmap[weekday]

    #load data 
    df = (pd.read_excel(excelfile,skiprows=1,sheet_name=weekday)
        .loc[0:40,['Start','End','Total','Category1','Category2','Task']]

    )




    #>>loc[0:13,['Start','End','Total','Category1','Category2','Task']]

    return cln_date,df 
    #Trim data. remove comments below 

    #run checks on tasks

    #run checks on pero

    #Do aggregations

process_single_day(,'Monday')

date_str = re.sub('.xlsx','',re.sub('^.*?time_tracker_week_v','',example_file))
for days, number in weekmap.items():

    cln_date = pd.Period(date_str)+number
    print(cln_date)
    #Do process code here. 

dict(zip(calendar.day_name,range(7)))

example_file.substr()

a =  pd.read_excel(example_file,skiprows=1,sheet_name='Monday')

b = a.loc[0:13,['Start','End','Total','Category1','Category2','Task']]
b

#Add checks for totals to make sure they are not 10000000

b.Task
b = b.assign(minutes = lambda d : d.Total.apply(lambda x: x.hour*60+x.minute+x.second/60),
    personal = lambda d: np.where(d.Category1=="personal",d.minutes,0),
    office = lambda d: np.where(d.Category1=="office",d.minutes,0),
)

taglist = ['journal','meditation','rehab','cardio','bwf','GTD']

b.Task
b.Task.iloc[6]

b.Task.iloc[6].split(',')

b.Task.replace([np.nan],'')

b.Task.apply(lambda x: x.replace([np.nan],'').split(','))
bigl = b.Task.replace([np.nan],'').apply(lambda x: x.split(',')).tolist()

observed_tags  = set([x.strip() for l in bigl for x in l])
observed_tags.discard('')
unexpected = observed_tags.difference(set(taglist))

if unexpected != {}:
    print("The following unexpected tags were found: \n" + ', '.join(unexpected))


def check_tags(series):

    bigl = series.replace([np.nan],'').apply(lambda x: x.split(',')).tolist()

    observed_tags  = set([x.strip() for l in bigl for x in l])
    observed_tags.discard('')
    unexpected = observed_tags.difference(set(taglist))

    if unexpected != {}:
        print("The following unexpected tags were found: \n" + ', '.join(unexpected))


check_tags(b.Task)


set  = set([x.strip() for l in bigl for x in l])
set([x.strip() for l in bigl for x in l])

del set

for tag in taglist:
     
    b = b.assign(**{tag: lambda d: 
        np.where(d.Task.fillna('').apply(lambda x: tag in x),d.minutes,0)}
        )

agg = (b
    .filter(['personal','office','journal','meditation','rehab','cardio','bwf','GTD'])
    .sum()
)
agg


b.Total.minute

from datetime import date , datetime 

p