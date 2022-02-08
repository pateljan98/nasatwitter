#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 17:19:53 2019

@author: donnahn87
"""

#import csv
import os
import pandas
import csv
 
userhome = os.path.expanduser('~')
RTcsvfile= userhome + r'/NASA-Data-Mining/Retweets High to Low.csv'
    
#Read Retweets High to Low csv file and filter to just NASA's tweets (no retweets)
nasa_data = pandas.read_csv(r'/Users/hungtu/NASA-Data-Mining/Retweets High to Low.csv')
nasa_filter = nasa_data.Handle=="NASA"
nasa_data['lower_tweet'] = map(lambda x: x.lower(), nasa_data['Tweet'])
print(nasa_data['lower_tweet'])

#Export to new filtered csv file
nasa_data['lower_tweet'].to_csv(r'/Users/hungtu/NASA-Data-Mining/my-NASA-data.csv')

#Read filtered csv file and filter to all lower case tweets 
nasa_data = pandas.read_csv(r'/Users/hungtu/NASA-Data-Mining/my-data.csv').apply(lambda x: x.astype(str).str.lower())
nasa_data.to_csv(r'/Users/hungtu/NASA-Data-Mining/my-NASA-data.csv')

#Read filtered lower case csv file and filter to just contain tweets about black holes 
nasa_data = pandas.read_csv(r'/Users/hungtu/NASA-Data-Mining/my-NASA-data.csv')
nasa_data_BH = nasa_data['Tweet'].str.contains('|'.join(['black hole', '#blackhole', 'blackhole', 'supernova', 'super nova']))

#Export to new csv file (filter = black holes)
nasa_data[nasa_data_BH].to_csv(r'/Users/hungtu/NASA-Data-Mining/my-data-BH.csv')

#Read and count number of tweets on black holes
nasa_data = pandas.read_csv(r'/Users/hungtu/NASA-Data-Mining/my-data-BH.csv')
numRowsBH = str(len(nasa_data))
print("Number of tweets about black holes: " + numRowsBH)


#Read filtered csv file and filter to just contain tweets about solar eclipses 
nasa_data = pandas.read_csv(r'/Users/hungtu/NASA-Data-Mining/my-NASA-data.csv')
nasa_data_SE = nasa_data['Tweet'].str.contains('|'.join(['solar eclipse', '#solareclipse', 'solareclipse', 'partial eclipse', 'total eclipse', 'total solar eclipse', 'penumbra', 'sun eclipse', 'eclipse of the sun']))

#Export to new csv file (filter = solar eclipse)
nasa_data[nasa_data_SE].to_csv(r'/Users/hungtu/NASA-Data-Mining/my-data-SE.csv')

#Read and count number of tweets on solar eclipses
nasa_data = pandas.read_csv(r'/Users/hungtu/NASA-Data-Mining/my-data-SE.csv')
numRowsSE = str(len(nasa_data))
print("Number of tweets about solar eclipses: " + numRowsSE)


#Read filtered csv file and filter to just contain tweets about aliens 
nasa_data = pandas.read_csv(r'/Users/hungtu/NASA-Data-Mining/my-NASA-data.csv')
nasa_data_ET = nasa_data['Tweet'].str.contains('|'.join(['alien', '#alien', 'extraterrestrial', 'martian', 'Area51', 'Area 51', 'space being', 'space inhabitant', 'intelligent life form', 'supernatural being', 'space invader', 'space jam', 'UFO']))

#Export to new csv file (filter = aliens)
nasa_data[nasa_data_ET].to_csv(r'/Users/hungtu/NASA-Data-Mining/my-data-ET.csv')

#Read and count number of tweets on aliens
nasa_data = pandas.read_csv(r'/Users/hungtu/NASA-Data-Mining/my-data-ET.csv')
numRowsET = str(len(nasa_data))
print("Number of tweets about aliens: " + numRowsET)


#Read filtered csv file and filter to just contain tweets about constellations 
nasa_data = pandas.read_csv(r'/Users/hungtu/NASA-Data-Mining/my-NASA-data.csv')
nasa_data_CS = nasa_data['Tweet'].str.contains('|'.join(['constellation', '#constellation', 'stars', 'orion', 'big dipper', 'little dipper', 'great bear', 'artemis', 'aries', 'taurus', 'gemini', 'cancer', 'leo', 'pisces', 'virgo', 'aquarius', 'capricorn', 'libra', 'sagittarius', 'scorpio']))

#Export to new csv file (filter = constellations)
nasa_data[nasa_data_CS].to_csv(r'/Users/hungtu/NASA-Data-Mining/my-data-CS.csv')

#Read and count number of tweets on constellations
nasa_data = pandas.read_csv(r'/Users/hungtu/NASA-Data-Mining/my-data-CS.csv')
numRowsCS = str(len(nasa_data))
print("Number of tweets about constellations: " + numRowsCS)
