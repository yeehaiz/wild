# coding: utf-8

import re
import datetime
import hashlib
import time
import datetime

REG_MOBILE = re.compile(r'1[34578]{1}\d{9}$')
REG_USERNAME = re.compile(r'[a-zA-Z][a-z0-9A-Z_]{2,17}$')

WEEKS = [
    '周一',
    '周二',
    '周三',
    '周四',
    '周五',
    '周六',
    '周日',
]


def parseInt(s):
    try:
        return int(s)
    except:
        return None


def md5(s):
    hash_md5 = hashlib.md5(s)
    return hash_md5.hexdigest()


def is_mobile(mobile):
    return bool(REG_MOBILE.match(mobile))


def is_username(username):
    return bool(REG_USERNAME.match(username))

def is_valid_password(password):
    return True


def checkIdcard(idcard):
    ''' @return (id_valid, gender, birthday)
    '''
    #Errors=['验证通过!','身份证号码位数不对!','身份证号码出生日期超出范围或含有非法字符!','身份证号码校验错误!','身份证地区非法!']
    area={"11":"北京","12":"天津","13":"河北","14":"山西","15":"内蒙古","21":"辽宁","22":"吉林","23":"黑龙江","31":"上海","32":"江苏","33":"浙江","34":"安徽","35":"福建","36":"江西","37":"山东","41":"河南","42":"湖北","43":"湖南","44":"广东","45":"广西","46":"海南","50":"重庆","51":"四川","52":"贵州","53":"云南","54":"西藏","61":"陕西","62":"甘肃","63":"青海","64":"宁夏","65":"新疆","71":"台湾","81":"香港","82":"澳门","91":"国外"}
    idcard=str(idcard)
    idcard=idcard.strip()
    idcard_list=list(idcard)
    #地区校验
    if(not area[(idcard)[0:2]]):
        return (False, None, None)  #print Errors[4]
    #15位身份号码检测
    if(len(idcard)==15):
        if((int(idcard[6:8])+1900) % 4 == 0 or((int(idcard[6:8])+1900) % 100 == 0 and (int(idcard[6:8])+1900) % 4 == 0 )):
            erg=re.compile('[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}$')#//测试出生日期的合法性
        else:
            ereg=re.compile('[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}$')#//测试出生日期的合法性
        if(re.match(ereg,idcard)):
            #print Errors[0]
            sex_val = 'f' if int(idcard[14]) % 2 == 0 else 'm'
            birthday = '19%s-%s-%s' % (idcard[6:8], idcard[8:10], idcard[10:12])
            return (True, sex_val, birthday)

        else:
            return (False, None, None)  #print Errors[2]
    #18位身份号码检测
    elif(len(idcard)==18):
        #出生日期的合法性检查
        #闰年月日:((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))
        #平年月日:((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))
        if(int(idcard[6:10]) % 4 == 0 or (int(idcard[6:10]) % 100 == 0 and int(idcard[6:10])%4 == 0 )):
            ereg=re.compile('[1-9][0-9]{5}19[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$')#//闰年出生日期的合法性正则表达式
        else:
            ereg=re.compile('[1-9][0-9]{5}19[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$')#//平年出生日期的合法性正则表达式
        #//测试出生日期的合法性
        if(re.match(ereg,idcard)):
            #//计算校验位
            S = (int(idcard_list[0]) + int(idcard_list[10])) * 7 + (int(idcard_list[1]) + int(idcard_list[11])) * 9 + (int(idcard_list[2]) + int(idcard_list[12])) * 10 + (int(idcard_list[3]) + int(idcard_list[13])) * 5 + (int(idcard_list[4]) + int(idcard_list[14])) * 8 + (int(idcard_list[5]) + int(idcard_list[15])) * 4 + (int(idcard_list[6]) + int(idcard_list[16])) * 2 + int(idcard_list[7]) * 1 + int(idcard_list[8]) * 6 + int(idcard_list[9]) * 3
            Y = S % 11
            M = "F"
            JYM = "10X98765432"
            M = JYM[Y]#判断校验位
            if(M == idcard_list[17]):#检测ID的校验位
                #print Errors[0]
                sex_val = 'f' if int(idcard[16]) % 2 == 0 else 'm'
                birthday = '%s-%s-%s' % (idcard[6:10], idcard[10:12], idcard[12:14])
                return (True, sex_val, birthday)

            else:
                return (False, None, None)  #print Errors[3]
        else:
            return (False, None, None)  #print Errors[2]
    else:
        return (False, None, None)  #print Errors[1]



def get_client_ip(request):
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        return request.META['HTTP_X_FORWARDED_FOR']
    else:
        return request.META['REMOTE_ADDR']



def paging_range(current, page_count, nav_count):
    if page_count <= nav_count:
        return range(1, page_count+1)

    start = current - nav_count/2
    end = start + nav_count

    if start < 1:
        return range(1, 1 + nav_count)

    if end > nav_count + 1:
        return range(page_count - nav_count + 1 , page_count + 1)

    return range(start, end)



## date functions

def df(dt):
    '''date format'''
    return dt.strftime('%Y-%m-%d')

def date_strp(s):
    '''字符串转日期'''
    t = time.strptime(s, "%Y-%m-%d")
    return datetime.date(*tuple(t)[:3])

def df_week(dt):
    return df(dt) + ' ' + WEEKS[dt.weekday()]


def date_add(dt, days):
    return (dt +  datetime.timedelta(days))

def month_begin_add(dt, months):
    m = (dt.month + months - 1) % 12 + 1
    y = dt.year + (dt.month + months -1) /12
    return datetime.date(y, m, 1)

def month_end_add(dt, months):
    m = (dt.month + months) % 12 + 1
    y = dt.year + (dt.month + months) /12
    return datetime.date(y, m, 1) - datetime.timedelta(1)
