#1.line plot
import matplotlib.pyplot as plt
marks = [88,57,59,78,90,55,14,88]
div = [1,2,3,4,5,6,7,8]
plt.plot(div,marks)
plt.show()


#2.scatter plot
import matplotlib.pyplot as plt
marks = [88,57,59,78,90,55,14,88]
div = [1,2,3,4,5,6,7,8]
plt.scatter(div,marks)
plt.show()

#3.Histogram 
import matplotlib.pyplot as plt
runs = [66,86,45,21,77,1,5,99,105,81,105,200]
plt.hist(runs,bins=4)
plt.show()

#Customization
import matplotlib.pyplot as plt
marks = [88,57,59,78,90,55,14,88]
div = [1,2,3,4,5,6,7,8]
plt.plot(div,marks)
plt.xlabel('divisin')
plt.ylabel('marks')
plt.title('Marks obtained')
plt.yticks([0,2,4,6,8])
plt.show()



