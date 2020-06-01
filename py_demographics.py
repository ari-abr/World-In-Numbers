import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# BAR GRAPH 1 MEDIAN AGE
plt.figure(figsize=(9,7))
data = pd.read_csv('data03sheet.csv')
plt.title('Average (Median) Age in Different Regions', fontdict={'fontweight':'bold', 'fontsize': 18})
#sorting the data into ascending order
myReg = data['Region']
myAge = data['Median age']
df = pd.DataFrame({"Region":myReg, "Median age":myAge})
df_sorted = df.sort_values(by='Median age', ascending=True)
plt.bar(df_sorted['Region'], df_sorted['Median age'], zorder=3)
plt.grid(zorder=0)
plt.ylabel('Median Age')
plt.yscale('linear')
plt.xticks(rotation=25)
plt.savefig('demographics_img01.png')
plt.show()


# PIE CHART 2 RELIGION
plt.figure(figsize=(8,5))
plt.title('Population by Religion (%)', fontdict={'fontweight':'bold', 'fontsize': 18})
myPercent = [31.2, 24.1, 16, 15.1, 6.9, 5.7, 1]
myReligions = 'Christianity', 'Islam', 'Non-religious', 'Hinduism', 'Buddhism', 'Folk', 'Other'
plt.pie(myPercent, labels=myReligions, autopct='%1.1f%%')
plt.axis('equal')
plt.savefig('demographics_img02.png')
plt.show()

# BAR GRAPH 3 - Religion
plt.figure(figsize=(8,6.5))
data = pd.read_csv('data03Bsheet.csv')
plt.title('Population by Religion (billions)', fontdict={'fontweight':'bold', 'fontsize': 18})
plt.bar(data.Religion, data.Number/1000, zorder=3)
plt.grid(zorder=0)
plt.ylabel('Population (billions)')
plt.xticks(rotation=25)
plt.xlim(-0.5, 6.5)
plt.savefig('demographics_img03.png')
plt.show()

# PIE CHART 4 POPULATION BY RACE AND ETHNICITY
plt.figure(figsize=(8,5))
plt.title('Population by Race/Ethnicity', fontdict={'fontweight':'bold', 'fontsize': 18})
myRaceRatio = [23.48, 21.23, 16, 13.93, 9.26, 8.62, 4.45, 3.03]
myRace = 'South Asian', 'East Asian', 'European', 'African', 'Southeast Asian', 'Middle Eastern','Latina', 'Other'
plt.pie(myRaceRatio, labels=myRace, autopct='%1.1f%%')
plt.axis('equal')
plt.savefig('demographics_img04.png')
plt.show()

# BAR GRAPH 5 Literacy Rate
plt.figure(figsize=(8,6.5))
data = pd.read_csv('data04Csheet.csv')
plt.title('Literacy Rate by Region', fontdict={'fontweight':'bold', 'fontsize': 18})
plt.bar(data.Region, data['Literacy Rate'], zorder=3)
plt.ylabel('Literacy Rate')
plt.grid(zorder=0)
plt.yscale('linear')
plt.xticks(rotation=25)
plt.ylim(50, 100)
plt.xlim(left=0.5)
plt.savefig('demographics_img05.png')
plt.show()

# LINE GRAPH 6 - Access
plt.figure(figsize=(8,5))
data = pd.read_csv('data04Bsheet.csv')
plt.title('Global Access (%) to Electricity and Clean Water', fontdict={'fontweight':'bold', 'fontsize': 18})
plt.plot(data.Year, data['Electricty Access'], label='Electricity')
plt.plot(data.Year, data['Clean Water Access'], label='Clean Water')
plt.xlabel('Year')
plt.ylabel('(%) Population With Access')
plt.grid(True)
plt.yscale('linear')
plt.xscale('linear')
plt.legend()
plt.xlim(1995, 2015)
plt.ylim(50, 100)
plt.savefig('demographics_img06.png')
plt.show()