import matplotlib.pyplot as plt
days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
temperature=[32,37,39,38,38,37,38]
plt.plot(days,temperature)

plt.title("Temperature in Madurai for past week")
plt.ylabel("Temperature in celcius")
plt.show()
