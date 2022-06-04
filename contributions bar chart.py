import matplotlib.pyplot as plt
labels=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
usage=[4,4,8,6,5,5,6]
y_positions=range(len(labels))
plt.bar(y_positions,usage)
plt.xticks(y_positions,labels)
plt.ylabel("Contributions")
plt.title("GITHUB CONTRIBUTIONS  in past week")
plt.show()
          
