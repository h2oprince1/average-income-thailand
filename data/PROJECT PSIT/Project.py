import csv
data_x = []
data_y = []
y = 0
data_y.append(0)
data_x.append("0")
for i in range(4):
    data_x.append(str(2555+i))

file = open('data/database1.csv')
data = csv.reader(file)
table = [row for row in data]

for each in table[228:304]:
    y += int(each[4].replace(",", ""))
data_y.append(y)
y = 0
for each in table[152:228]:
    y += int(each[4].replace(",", ""))
data_y.append(y)
y = 0
for each in table[76:152]:
    y += int(each[4].replace(",", ""))
data_y.append(y)
y = 0
for each in table[:76]:
    y += int(each[4].replace(",", ""))
data_y.append(y)
y = 0
#% matplotlib inline
import matplotlib.pyplot as plt
ghp = plt.gca()
ghp.plot(data_x,data_y,'--gs')
ghp.axis([0, 4, 0, 140000])
ghp.set_title(u'จำนวนคนต่อครัวที่รายได้ต่ำกว่า 30,000 บาทต่อปี',fontname='JasmineUPC',fontsize=20)
ghp.set_xlabel('Years',fontname='JasmineUPC',fontsize=20)
ghp.set_ylabel('Amount of familys below 30000 bath',fontname='JasmineUPC',fontsize=20)
plt.show()
