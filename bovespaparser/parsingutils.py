#!/usr/bin/python


import datetime


def __no_conversion(data):
    return data


def __money_conversion(data):
    return float(data) / 100


def __rstrip_conversion(data):
    return data.rstrip()


def __date_conversion(data):
    month = ""
    if int(data[4:6]) == 1:
          month = "Jan"
    if int(data[4:6]) == 2:
          month = "Feb"
    if int(data[4:6]) == 3:
          month = "Mar"
    if int(data[4:6]) == 4:
          month = "Apr"
    if int(data[4:6]) == 5:
          month = "May"
    if int(data[4:6]) == 6:
          month = "Jun"
    if int(data[4:6]) == 7:
          month = "Jul"
    if int(data[4:6]) == 8:
          month = "Aug"
    if int(data[4:6]) == 9:
          month = "Sep"
    if int(data[4:6]) == 10:
          month = "Oct"
    if int(data[4:6]) == 11:
          month = "Nov"
    if int(data[4:6]) == 12:
          month = "Dec"
    return data[0:4]+'-'+month+'-'+data[6:8]


NO, INT, MONEY, RTRIM, DATE = ([__no_conversion,
                                int,
         
                       __money_conversion,
                                __rstrip_conversion,
                                __date_conversion])


class DataSegment:

    def __init__(self, startIndex=0, endIndex=0, postProcessing=NO):
        self.__slice = slice(startIndex, endIndex)
        self.__funct = postProcessing

    def parse(self, data):
        return self.__funct(data[self.__slice])
