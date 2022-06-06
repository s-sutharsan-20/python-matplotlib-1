import matplotlib.pyplot as plt
days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
temperature=[32,37,39,38,38,37,38]
y_positions=range(len(days))
plt.bar(y_positions,temperature)
plt.xticks(y_positions,days)
plt.ylabel("Temperature in celcius")
plt.title("Temperature in madurai for past week")
plt.show()
