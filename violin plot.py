import seaborn as sns
import matplotlib.pyplot as plt
data=sns.load_dataset("tips")
plt.figure(figsize=(6,4))
sns.violinplot(x="day",y="total_bill",data=data)
plt.show()
