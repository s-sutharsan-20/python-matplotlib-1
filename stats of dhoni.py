import matplotlib.pyplot as plt
labels=[2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
usage=[414,332,287,392,358,461,371,372,284,290,455,416,200,114,232]
y_positions=range(len(labels))
plt.bar(y_positions,usage)
plt.xticks(y_positions,labels)
plt.ylabel("Runs")
plt.xlabel("Year")
plt.title("M.S.Dhoni in IPL")
plt.show()
