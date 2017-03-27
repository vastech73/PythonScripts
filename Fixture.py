#!/usr/bin/python

"""
List of Liverpool Fixtures in 2016
"""

Fixture = {'MD22': 'LIVERPOOLERPOOL vs MUN', 'MD23': 'NOR vs LIVERPOOL', 'MD24': 'LEI vs LIVERPOOL', 'MD25': 'LIVERPOOL vs SUN', 'MD26': 'AVL vs LIVERPOOL', 'MD27': 'LIVERPOOL vs EVE', 'MD28': 'LIVERPOOL vs MCI', 'MD29': 'CRY vs LIVERPOOL', 'MD30': 'LIVERPOOL vs CHE', 'MD31': 'SOU vs LIVERPOOL', 'MD32':'LIVERPOOL vs TOT','MD33': 'LIVERPOOL vs STO', 'MD34': 'BOU vs LIVERPOOL', 'MD35': 'LIVERPOOL vs NUFC', 'MD36': 'SWA vs LIVERPOOL', 'MD37': 'LIVERPOOL vs WAT', 'MD38': 'WBA vs LIVERPOOL'}

Matchday = raw_input("Enter the Match day number:")


for key, value in Fixture.iteritems():
    if key == Matchday:
        print value  


