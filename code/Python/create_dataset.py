# This python code is written to access certain specific fields from the World Bank database
# for certain specified countries.
# It will create a CSV file with the data.
# Comment

import requests
import pandas as pd
import wbgapi as wb
import csv
import math
CURRENT = 2025
YRSTART = 1960

# World Bank Data
# Use Google Chrome
# data.worldbank.org
def imf_get_data():
    i = 1

def wb_get_population():
    with open('population.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=",", quoting=csv.QUOTE_MINIMAL)
        tuple = ("Date", "IND_POP", "CHN_POP",)
        writer.writerow(tuple)
        tuple = ""

        df_ind = wb.data.DataFrame('SP.POP.TOTL', 'IND')
        df_chn = wb.data.DataFrame('SP.POP.TOTL', 'CHN')
        for i in range(1960, CURRENT):
            yearstring = "YR" + str(i)
            datestr = str(i) + "-12-31"
            tuple =  (datestr, df_ind.loc['IND'][yearstring], df_chn.loc['CHN'][yearstring])
            print (df_ind.loc['IND'][yearstring])
            writer.writerow(tuple)


def wb_getdata(countrylist, key, suffix):
    with open(suffix + '.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=",", quoting=csv.QUOTE_MINIMAL)
        tuple = ("Date",)
        for country in range(len(countrylist)):
            tuple = tuple + (countrylist[country] + "_" + suffix,)

        writer.writerow(tuple)
        tuple = ""
        df = {}
        for i in countrylist:
            df[i] = wb.data.DataFrame(key, i)

        for i in range(1960, CURRENT):
            yearstring = "YR" + str(i)
            datestr = str(i) + "-12-31"
            tuple = (datestr,)
            for country in range(len(countrylist)):
                tuple = tuple + (df[countrylist[country]].loc[countrylist[country]][yearstring], )
#            print(df_ind.loc['IND'][yearstring])
            writer.writerow(tuple)

def wb_getdata_goldin(countrylist, key, key2, suffix):
    pwd = '/Users/ashbelur/Documents/ash belur/BIG PROJECTS/phd/pythondevelopment/wbdata/'
    pwd = './'
    print('In GET DATA GOLDIN')
    print('Directory is', pwd)


    with open(pwd + suffix + '.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=",", quoting=csv.QUOTE_MINIMAL)
        tuple = ("Date",)
        for country in range(len(countrylist)):
            tuple = tuple + (countrylist[country] + "_" + suffix,)
        tuple = ("COUNTRY", "FLPP", "GDPP", )
#        writer.writerow(tuple)
        tuple = ""
        df = {}
        dg = {}
        for i in countrylist:
            df[i] = wb.data.DataFrame(key, i)
            dg[i] = wb.data.DataFrame(key2, i)

        for i in range(YRSTART, CURRENT):
            yearstring = "YR" + str(i)
            datestr = str(i) + "-12-31"
            tuple = (datestr,)
            for country in range(len(countrylist)):
                tuple = (datestr, countrylist[country], \
                         df[countrylist[country]].loc[countrylist[country]][yearstring], \
                         math.log(dg[countrylist[country]].loc[countrylist[country]][yearstring]) )
                print("Value", datestr, countrylist[country], i, \
                  df[countrylist[country]].loc[countrylist[country]][yearstring], \
                  dg[countrylist[country]].loc[countrylist[country]][yearstring])
                writer.writerow(tuple)

    thisset = {"CHN", "IND", "BRA", "BGD", "RUS", "KOR", "IDN", "VNM", "SGP"}
    with open(pwd + suffix + '2.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=",", quoting=csv.QUOTE_MINIMAL)
        counter = 0
        for country in range(len(countrylist)):
            if (countrylist[country] in thisset):
                for i in range (1960, CURRENT):
                    yearstring = "YR" + str(i)
                    datestr = str(i) + "-12-31"

                    tuple = (countrylist[country], datestr, \
                         math.log(dg[countrylist[country]].loc[countrylist[country]][yearstring]),)
                    for j in range(counter):
                        tuple = tuple + ("",)
                    tuple = tuple + (df[countrylist[country]].loc[countrylist[country]][yearstring],)
                    print("Value2", datestr, countrylist[country], i, \
                        math.log(dg[countrylist[country]].loc[countrylist[country]][yearstring]), \
                        df[countrylist[country]].loc[countrylist[country]][yearstring])
                    writer.writerow(tuple)
                counter = counter + 1

if __name__ == '__main__':
    if (1 == 0):
        key = 'NY.GDP.PCAP.CD'
        print("First")
        print(wb.series.info(key))

        print("Second")
        print(wb.series.info())

        print("Third")
        print(wb.economy.info(db=6))

        print("Fourth")
        print(wb.series.info(key))

    if(1 == 1):
        print("Getting Country Codes")
        print(wb.economy.coder(['United States', 'China', 'Germany', 'India', 'Japan', \
                                'England',  'France', 'Italy', 'Canada', 'Brazil', \
                                'Russia', 'Spain', 'South Korea', 'Australia', 'Mexico', \
                                'Turkey', 'Indonesia', 'Netherlands', 'Saudi Arabia', 'Poland', \
                                'Switzerland', 'Taiwan', 'Belgium', 'Argentina', 'Sweden', 'Ireland', \
                                'Israel', 'Singapore', 'United Arab Emirates', 'Thailand', 'Austria', \
                                'Norway', 'Philippines', 'Viet nam', 'Bangladesh', 'Denmark', \
                                'Malaysia', 'Colombia',  'Hong Kong', 'South Africa', 'Romania', 'Pakistan', \
                                'Czech Republic', 'Egypt', 'Chile', 'Iran', 'Portugal', \
                                'Finland', 'Peru', 'Kazakhstan', 'Algeria', 'Greece', \
                                'Iraq', 'New Zealand', 'Hungary', 'Qatar', 'Ukraine', \
                                'Cuba', 'Nigeria', 'Morocco', 'Kuwait', 'Slovakia', \
                                'Uzbekistan', 'Kenya', 'Dominican Republic', 'Ecuador', 'Guatemala', \
                                'Ethiopia', 'Bulgaria', 'Angola', 'Venezuela', 'Oman', \
                                'Costa Rica', 'Sri Lanka', 'Croatia', 'Luxembourg', 'Ivory Coast', \
                                'Serbia', 'Panama', 'Lithuania', 'Turkmenistan', 'Ghana', \
                                'Tanzania', 'Uruguay', 'D R Congo', 'Azerbaijan', 'Slovenia', \
                                'Belarus', 'Myanmar', 'Uganda', 'Bolivia', 'Tunisia', \
                                'Jordan', 'Cameroon', 'Cambodia', 'Bahrain', 'Libya', \
                                'Nepal', 'Latvia', 'Paraguay', 'Estonia', 'Cyprus', \
                                'Nicaragua', 'Cameroon',  \
                                'Afghanistan']))

# Real GDP Per Capita (2007$) PPP - NY.GDP.PCAP.PP.KD
    wb_getdata_goldin(['USA'], 'NY.GDP.PCAP.PP.KD', 'NY.GDP.PCAP.CD', 'GOLDIN')

#   wb_get_population()
#    wb_getdata(['USA', 'CHN', 'JPN', 'DEU', 'IND', 'GBR', 'BRA', 'RUS', 'ZAF', 'KOR', 'BGD', 'SGP', 'HKG', 'IDN', 'VNM'], 'SP.POP.TOTL', 'POP')
#    wb_getdata(['USA', 'CHN', 'JPN', 'DEU', 'IND', 'GBR', 'BRA', 'RUS', 'ZAF', 'KOR', 'BGD', 'SGP', 'HKG', 'IDN', 'VNM'], 'NY.GDP.PCAP.CD', 'GDPP')
#    wb_getdata(['USA', 'CHN', 'JPN', 'DEU', 'IND', 'GBR', 'BRA', 'RUS', 'ZAF', 'KOR', 'BGD', 'SGP', 'HKG', 'IDN', 'VNM'], 'NY.GDP.MKTP.CD', 'GDP')
#    wb_getdata(['USA', 'CHN', 'JPN', 'DEU', 'IND', 'GBR', 'BRA', 'RUS', 'ZAF', 'KOR', 'BGD', 'SGP', 'HKG', 'IDN', 'VNM'], 'SI.POV.GINI', 'GINI')
#    wb_getdata(['USA', 'CHN', 'JPN', 'DEU', 'IND', 'GBR', 'BRA', 'RUS', 'ZAF', 'KOR', 'BGD', 'SGP', 'HKG', 'IDN', 'VNM'], 'GC.DOD.TOTL.GD.ZS', 'DBTP')

#   wb_getdata_goldin(['USA', 'CHN', 'DEU', 'IND', 'JPN', 'GBR', 'FRA', 'ITA', 'CAN', 'BRA', \
#  'RUS', 'ESP', 'KOR', 'AUS', 'MEX', 'TUR', 'IDN', 'NLD', 'SAU', 'POL', \
#   'CHE', 'BEL', 'ARG', 'SWE', 'IRL', 'ISR', 'SGP', 'ARE', 'THA', 'AUT', \
#   'NOR', 'PHL', 'VNM', 'BGD', 'DNK', 'MYS', 'COL', 'HKG', 'ZAF', 'ROU', 'PAK', \
#   'CZE', 'EGY', 'CHL', 'IRN', 'PRT', 'FIN', 'PER', 'KAZ', 'DZA', 'GRC', \
#   'IRQ', 'NZL', 'HUN', 'QAT', 'UKR', 'CUB', 'NGA', 'MAR', 'KWT', 'SVK', \
#   'UZB', 'KEN', 'DOM', 'ECU', 'GTM', 'ETH', 'BGR', 'AGO', 'VEN', 'OMN', \
#   'CRI', 'LKA', 'HRV', 'LUX', 'CIV', 'SRB', 'PAN', 'LTU', 'TKM', 'GHA', \
#   'TZA', 'URY', 'AZE', 'SVN', 'BLR', 'MMR', 'UGA', 'BOL', 'TUN', \
#   'JOR', 'CMR', 'KHM', 'BHR', 'LBY', 'NPL', 'LVA', 'PRY', 'EST', 'CYP', \
#   'BOL', 'UGA',  'ZAF', 'BGD'], \
#    'SL.TLF.CACT.FE.ZS', 'NY.GDP.PCAP.CD', 'GOLDIN')

#    wb_getdata_goldin(['SAU', 'QAT', 'ARE', 'MAR', 'IRN', 'IRQ', 'AFG'], 'SL.TLF.CACT.FE.ZS', 'NY.GDP.PCAP.CD', 'GOLDIN')
# ['SAU', 'QAT', 'UAE', 'MAR', 'IRN', 'IRQ', 'AFG']
#    wb_getdata(['USA', 'CHN', 'JPN', 'DEU', 'IND', 'GBR', 'BRA', 'RUS', 'ZAF', 'KOR', 'BGD', 'SGP', 'HKG', 'IDN', 'VNM'], 'NY.GDP.PCAP.CD', 'GDPP')