import pandas as pd
#import numpy as np
    
def peta_to_giga(row):
    row['Energy Supply'] *= 1000000
    return row
    
    def fileref():
        energy = pd.read_excel('Energy Indicators.xls', header = None, skipfooter = 2)
        energy = (energy.drop([0,1], axis = 1))
        energy.dropna()
        energy.drop(9)
        energy.rename(columns = {2: 'Country',3: 'Enegry',4: 'Energy Supply per Capita',5: '% Renewable'})
        energy.replace(regex = True, to_replace = [r'\d', r'\(([^)]+)\)'], value = r'')
        energy.replace(to_replace = ["...", "Republic of Korea", "United States of America",
                                    "United Kingdom of Great Britain and Northern Ireland",
                                    "China, Hong Kong Special Administrative Region"],
                      value = [None, "South Korea", "United States", "United Kingdom", "Hong Kong"])
        energy.apply(peta_to_giga, axis = 1)
        
        GDP = pd.read_csv('world_bank.cv', header = None, skiprows = 4)
        
        GDP = (GDP.rename(columns = GDP.iloc[0])
                  .drop(0)
                  .replace(to_replace=["Korea, Rep.", "Iran, Islamic Rep.", "Hong Kong SAR, China"],
                      value = ["South Korea", "Iran" "Hong Kong" ])
                  .rename(columns = {2006: '2006', 2007: '2007', 2008: '2008', 2009: '2009', 2010: '2010', 2011: '2011',
                                    2012: '2012', 2013: '2013', 2014: '2014', 2015: '2015'}))
        
        ScimEn = pd.read_excel('scimagojr-3.xlsx')
        return energy, GDP, ScimEn
    def answer_one():
        energy, GDP, ScimEn = fileref()
        energy = energy.dropna()
        GDP_columns = ['Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2014', '2015']
        GDP = GDP[GDP_columns]
        ScimEn_columns = ['Rank', 'Country', 'Documents', 'Citable Documents', 'Citations', 'Self-citations', 
                          'Citations per document', 'H index']
        ScimEn_columns = ScimEn[ScimEn_columns]
        ScimEn = ScimEn[:15]
        
        new = pd.merge(energy, GDP, how = 'inner', left_on = 'Country', right_on = 'Country Name')
        new = new.drop(['Country Name'], axis = 1)
        new = pd.merge(new, ScimEn, how = 'inner', left_on = 'Country', right_on = 'Country')
        new = new.set_index('Country')
        columns = ['Rank', 'Country', 'Documents', 'Citable Documents', 'Citations', 'Self-citations', 
                   'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per capita', '% Renewable',
                   '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2014', '2015']
        new = new[columns]
        
        return new
        
    
    answer_one()
        