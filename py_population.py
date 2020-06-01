import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# LINE GRAPH 1 - 0 - 2020 WORLD POPULATION
plt.figure(figsize=(8,5))
data01 = pd.read_csv('data02sheet.csv')
plt.title('Population Over Time (0-2020) in millions', fontdict={'fontweight':'bold', 'fontsize': 18})
plt.plot(data01.Year, data01.World)
plt.xlabel('Year')
plt.ylabel('Population (millions)')
plt.grid(True)
plt.ylim(0, 6500)
plt.xlim(0, 2020)
plt.yscale('linear')
plt.xscale('linear')
plt.savefig('populationtrends_img01.png')
plt.show()


# LINE GRAPH 2 1900 - 2000 WORLD POPULATION
plt.figure(figsize=(8,5))
data01 = pd.read_csv('data01sheet.csv')
plt.title('Population Over Time (1900-2020) in billions', fontdict={'fontweight':'bold', 'fontsize': 18})
plt.plot(data01.Year, data01.AvgTotPop)
plt.xlabel('Year')
plt.ylabel('Population (billions)')
plt.grid(True)
plt.ylim(0, 8)
plt.xlim(1900, 2020)
plt.yscale('linear')
plt.xscale('linear')
plt.savefig('populationtrends_img02.png')
plt.show()

# LINE GRAPH 3 0 -2000 REGION POPULATION
plt.figure(figsize=(8,5))
data02 = pd.read_csv('data02sheet.csv')
plt.title('Population Over Time in Different Regions (0-2000)', fontdict={'fontweight':'bold', 'fontsize': 18})
plt.plot(data02.Year, data02['Asia Total'], label='Asia')
plt.plot(data02.Year, data02.Europe, label='Europe')
plt.plot(data02.Year, data02.Africa, label='Africa')
plt.plot(data02.Year, data02['South/Central America'], label='South&Central America')
plt.plot(data02.Year, data02['North America'], label='North America')
plt.plot(data02.Year, data02.Oceania, label='Oceania')
plt.xlabel('Year')
plt.ylabel('Population (millions)')
plt.grid(True)
plt.ylim(0, 3750)
plt.xlim(0, 2000)
plt.yscale('linear')
plt.xscale('linear')
plt.legend()
plt.savefig('populationtrends_img03.png')
plt.show()

# LINE GRAPH 4 - 1500 - 2000 REGION POPULATION
plt.figure(figsize=(8,5))
data02 = pd.read_csv('data02sheet.csv')
plt.title('Population Over Time in Different Regions (1500-2000)', fontdict={'fontweight':'bold', 'fontsize': 18})
plt.plot(data02.Year, data02['Asia Total'], label='Asia')
plt.plot(data02.Year, data02.Europe, label='Europe')
plt.plot(data02.Year, data02.Africa, label='Africa')
plt.plot(data02.Year, data02['South/Central America'], label='South&Central America')
plt.plot(data02.Year, data02['North America'], label='North America')
plt.plot(data02.Year, data02.Oceania, label='Oceania')
plt.xlabel('Year')
plt.ylabel('Population (millions)')
plt.grid(True)
plt.ylim(0, 3750)
plt.xlim(1800, 2000)
plt.yscale('linear')
plt.xscale('linear')
plt.legend()
plt.savefig('populationtrends_img04.png')
plt.show()


# LINE GRAPH 5 - ASIA POPULATION
plt.figure(figsize=(8,5))
data02 = pd.read_csv('data02sheet.csv')
plt.title('Population Over Time in Different Parts of Asia', fontdict={'fontweight':'bold', 'fontsize': 18})
plt.plot(data02.Year, data02['Asia Total'], label='Asia Total')
plt.plot(data02.Year, data02['East Asia'], label='East Asia')
plt.plot(data02.Year, data02['South Asia'], label='South Asia')
plt.plot(data02.Year, data02['West Asia'], label='West Asia')
plt.xlabel('Year')
plt.ylabel('Population (millions)')
plt.grid(True)
plt.ylim(0, 3750)
plt.xlim(1800, 2000)
plt.yscale('linear')
plt.xscale('linear')
plt.legend()
plt.savefig('populationtrends_img05.png')
plt.show()

# BAR GRAPH 5.5 - TOP MOST POPULOUS COUNTRIES
plt.figure(figsize=(8,5))
data02 = pd.read_csv('data02Csheet.csv')
plt.title('10 Most Populous Countries', fontdict={'fontweight':'bold', 'fontsize': 18})
plt.bar(data02.Country, data02.Population, zorder=3)
plt.ylabel('Population (millions)')
plt.grid(zorder=0)
plt.xticks(rotation=25)
plt.yscale('linear')
plt.savefig('populationtrends_img05_1.png')
plt.show()


# LINE GRAPH 6 - POPULATION PROJECTION WORLD TOTAL
plt.figure(figsize=(8,5))
data02 = pd.read_csv('data02Bsheet.csv')
plt.title('Total World Population Projection', fontdict={'fontweight':'bold', 'fontsize': 18})
plt.plot(data02.Year, data02['World'])
plt.xlabel('Year')
plt.ylabel('Population (millions)')
plt.grid(True)
plt.ylim(0, 15000)
plt.xlim(2000, 2100)
plt.yscale('linear')
plt.xscale('linear')
plt.savefig('populationtrends_img06.png')
plt.show()

# LINE GRAPH 7 - POPULATION PROJECTION BY REGION 
plt.figure(figsize=(8,5))
data02 = pd.read_csv('data02Bsheet.csv')
plt.title('Population Projection by Region', fontdict={'fontweight':'bold', 'fontsize': 18})
plt.plot(data02.Year, data02['Asia'], label='Asia')
plt.plot(data02.Year, data02.Africa, label='Africa')
plt.plot(data02.Year, data02.Europe, label='Europe')
plt.plot(data02.Year, data02['South/Central America'], label='South&Central America')
plt.plot(data02.Year, data02['North America'], label='North America')
plt.plot(data02.Year, data02.Oceania, label='Oceania')
plt.xlpabel('Year')
plt.ylabel('Population (millions)')
plt.grid(True)
plt.ylim(0, 6000)
plt.xlim(2000, 2100)
plt.yscale('linear')
plt.xscale('linear')
plt.legend()
plt.savefig('populationtrends_img07.png')
plt.show()
