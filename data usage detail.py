import matplotlib.pyplot as plt
labels=["01/01","02/01","03/01","04/01","05/01","06/01","07/01","08/01","09/01","10/01"]
usage=[1.48,1.26,1.01,1.17,1.00,1.10,1.01,1.51,1.26,1.01]
y_positions=range(len(labels))
plt.bar(y_positions,usage)
plt.xticks(y_positions,labels)
plt.ylabel("Data usage (in GB)")
plt.xlabel("Date")
plt.title("DATA USAGE DETAILS")
plt.show()
