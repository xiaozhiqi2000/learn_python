# coding:utf8

import time
import datetime
import calendar
import json
import requests

#————————————————————————————————————————————————————————————————————————————————————————————————————————————
#把列表分段
def get_list_page(itemlist, chunksize=2000):
    """
    分页列表
    :param itemlist:
    :param chunksize:
    :return:
    """
    while chunksize < len(itemlist):
        yield itemlist[0:chunksize]
        itemlist = itemlist[chunksize:]
    yield itemlist
#————————————————————————————————————————————————————————————————————————————————————————————————————————————
def get_sql_in_where_by_list(key, items):
    """
    列表转成sql  where {key} in ({items})
    :param key: string
    :param items: list
    :return: string
    """
    if len(items) > 0:
        sql_items = ','.join(map(lambda x: "'" + str(x) + "'", items))
        where = " {key} in ({sql_items}) ".format(sql_items=sql_items, key=key)
    else:
        where = " 1 "
    return where

#————————————————————————————————————————————————————————————————————————————————————————————————————————————
def get_time_list(str_start_time,str_end_time):
    """
    获得一个时间列表
    :param str_start_time: string
    :param str_end_time: string
    :return: list<String>
    """
    date_list=[]
    begin_date = datetime.datetime.strptime(str(str_start_time), "%Y%m%d")
    end_date = datetime.datetime.strptime(str(str_end_time), "%Y%m%d")
    if begin_date <= end_date:
        while begin_date <= end_date:
            date_str = begin_date.strftime("%Y%m%d")
            date_list.append(date_str)
            begin_date += datetime.timedelta(days=1)
    else:
        while begin_date >= end_date:
            date_str = begin_date.strftime("%Y%m%d")
            date_list.append(date_str)
            begin_date -= datetime.timedelta(days=1)
    return date_list
#————————————————————————————————————————————————————————————————————————————————————————————————————————————
def get_number_dayth(str_day,number,toward='backward'):

    """
    获得几天后的时间 向后推number用正数，向前推用负数
    :param str_day: string （无间隔的时间字符串；例如‘20180601’）
    :param number:int
    :return: String
    """
    begin_Date = datetime.datetime.strptime(str(str_day)[0:8], "%Y%m%d")

    if toward == 'forward':
        dayth_Date1 = begin_Date-datetime.timedelta(days=number)
    else:
        dayth_Date1 = begin_Date+datetime.timedelta(days=number)
    dayth_Date = dayth_Date1.strftime("%Y%m%d")
    return dayth_Date

#————————————————————————————————————————————————————————————————————————————————————————————————————————————
def strTime_timeStamp(strTime):
    """
    字符串转换为时间戳
    :param strTime: String (时间类型的字符串)
    :return: Int
    """
    timeStamp = int(time.mktime(time.strptime(strTime, "%Y%m%d")))
    return timeStamp

#————————————————————————————————————————————————————————————————————————————————————————————————————————————
def timStamp_strTime(timeStamp):
    """
    时间戳转换为时间数组
    :param timeStamp: Int (时间类型的字符串)
    :return: String
    """
    strTime=time.strftime("%Y%m%d",time.localtime(int(timeStamp)))
    return strTime

#————————————————————————————————————————————————————————————————————————————————————————————————————————————
def getMonthFirstDayAndLastDay(year=None, month=None,num=None):
    """
    :param year: 年份，默认是本年，可传int或str类型
    :param month: 月份，默认是本月，可传int或str类型
    :return: firstDay: 当月的第一天，datetime.date类型
              lastDay: 当月的最后一天，datetime.date类型
    """
    if year:
        year = int(year)
    else:
        year = datetime.date.today().year
    if month:
        month = int(month)
    else:
        month = datetime.date.today().month
    # 获取当月第一天的星期和当月的总天数
    firstDayWeekDay, monthRange = calendar.monthrange(year, month)
    # 获取当月的第一天
    firstDay =time.strftime("%Y%m%d", time.strptime(str(datetime.date(year=year, month=month, day=1)), "%Y-%m-%d"))
    lastDay = time.strftime("%Y%m%d", time.strptime(str(datetime.date(year=year, month=month, day=monthRange)), "%Y-%m-%d"))
    if num=='begin':
        return firstDay
    elif num=='last':
        return lastDay
    else:
        return firstDay,lastDay
#————————————————————————————————————————————————————————————————————————————————————————————————————————————
def get_curl_request(bbtype, bbbirthday):
    url = "http://10.1.3.107/service/bang"

    params = {"bbtype": bbtype, "bbbirthday": bbbirthday}
    payload = {'FRPC_MODULE':'user', 'FRPC_ACTION':'formatBabyAge', 'FRPC_ARG_BODY':json.dumps(params)}
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
        'Postman-Token': "00f9039b-6db1-4e43-a8d9-b0a912ced767"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    str_json = response.json()
    data=str_json.get('data','')
    return data
#————————————————————————————————————————————————————————————————————————————————————————————————————————————
'''获取两个日期的时间差，单位天'''
def diffdays(date1, date2):
    strdata1=str(date1)
    strdata2=str(date2)
    date1=time.mktime(time.strptime(strdata1,'%Y%m%d'))
    date2=time.mktime(time.strptime(strdata2,'%Y%m%d'))
    return int((date1-date2)/(24*60*60))

