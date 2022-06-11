import matplotlib.pyplot as pyplot
labels=("Twitter","Instagram","FaceBook","Spotify","Chess.com","Sololearn")
sizes=[5,25,20,10,10,30]
pyplot.pie(sizes,labels=labels,autopct='%1.f%%',counterclock=False,startangle=105)
pyplot.title("Screen Time")
pyplot.show()
