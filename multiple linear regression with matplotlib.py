from __future__ import print_function #adds the backward compatibility

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing CSV file
data=pd.read_csv("datasets_50_Startups.csv")
print("The provided dataset shows the profit earned by various startups (In USA) as a function of R&D spend, Administration spend and Marketing spend\n")
print(data.tail())
print(data.shape)


#. The numpy function polyfit numpy.polyfit(x,y,deg) fits a polynomial of degree deg to points (x, y), returning the polynomial coefficients that minimize the square error.
rd_fit=np.polyfit(data["R&D Spend"],data["Profit"],1)
admin_fit=np.polyfit(data["Administration"],data["Profit"],1)
mkt_fit=np.polyfit(data["Marketing Spend"],data["Profit"],1)

#drawing the scatter plots
plt.figure(figsize=(8.7,7))
plt.scatter(x=data["R&D Spend"],y=data["Profit"],color="blue",marker="*")
plt.scatter(x=data["Administration"],y=data["Profit"],color="magenta",marker="*")
plt.scatter(x=data["Marketing Spend"],y=data["Profit"],color="orange",marker="*")

# #drawing regression lines
plt.plot(data["R&D Spend"],rd_fit[0]*data["R&D Spend"]+rd_fit[1],color='darkblue', linewidth=2)
plt.plot(data["Administration"],admin_fit[0]*data["Administration"]+admin_fit[1],color='deeppink', linewidth=2)
plt.plot(data["Marketing Spend"],mkt_fit[0]*data["Marketing Spend"]+mkt_fit[1],color='red', linewidth=2)

#Putting the legend, title and lables
plt.title("Relationship between the profit obtained w.r.t. spend on various domains",size=15)
plt.legend(['Spend on R&D','Spend on Administration','Spend on Marketing','R&D','Admin','Marketing'])
plt.xlabel("Domains")
plt.ylabel("Profit obtained")
plt.show()
