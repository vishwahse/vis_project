#19330
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/user/Documents/code/boardgame.csv")
print(df['Year'].corr(df['Average']))
print(df['Year'].corr(df['Bayes average']))
count = 0
avg = []
bayavg = []
while count < 19330:
    #print(df.iloc[0:1000, :]['Year'].corr(df.iloc[0:1000, :]['Average']))
    avg.append(df.iloc[count:count+1000, :]['Year'].corr(df.iloc[count:count+1000, :]['Average']))
    bayavg.append(df.iloc[count:count+1000, :]['Year'].corr(df.iloc[count:count+1000, :]['Bayes average']))
    count += 1000
plt.plot(avg,'r', bayavg, 'g')
plt.show()
usavg = []
usbayavg = []
labels = ['0 - 1000', '1000 - 2000', '2000 - 3000', '3000 - 4000', '4000 - 5000', '5000 - 6000', '6000 - 7000', '7000 - 8000', '8000 - 9000', '9000 - 10000', '10000 - 11000', '11000 - 12000', '12000 - 13000', '13000 - 14000', '14000 - 15000', '15000 - 16000', '16000 - 17000', '17000 - 18000', '18000 - 19000', '19000 - 20000']
count = 0
while count < 19330:
    #print(df.iloc[0:1000, :]['Year'].corr(df.iloc[0:1000, :]['Average']))
    usavg.append(df.iloc[count:count+1000, :]['Users rated'].corr(df.iloc[count:count+1000, :]['Average']))
    usbayavg.append(df.iloc[count:count+1000, :]['Users rated'].corr(df.iloc[count:count+1000, :]['Bayes average']))
    count += 1000
plt.pie(usavg, labels = labels, radius = 5)
plt.pie(usbayavg, labels = labels, radius = 5)