import matplotlib.pyplot as plt

week_number=(-1,0,1,2,3,4,5)
average_points=(6.714286,8.2858,12.42857,13.28571,10.42856,7.7142,14.2857)
average=sum(average_points)/len(average_points)

plt.plot(week_number,average_points, 'bo')
plt.title("Weekly Average Points")
plt.ylabel("Average Points")
plt.xlabel("Week Numbers")
plt.xlim(-2,6)
plt.ylim(0,20)


plt.show()
