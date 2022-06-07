import matplotlib.pyplot as plt
contributions=[4,4,8,6,5,5,6]
date=['29/05/2022','30/05/2022','31/05/2022','01/06/2022','02/06/2022','03/06/2022','04/06/2022']
y_positions=range(len(date))
plt.bar(y_positions,contributions)
plt.xticks(y_positions,date)
plt.title("GITHUB Contributions")
plt.ylabel("Contributions")
plt.xlabel("Date")
plt.show()
