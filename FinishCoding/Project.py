import pygal
import csv
def graph_per_year():
    """
    Output Graph income per year.
    """
    data_x = []
    data_y = []
    y = 0

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
    ghp = pygal.Bar()
    ghp.title = " จำนวนคนต่อครัวที่รายได้ต่ำกว่า 30,000 บาท ทั้งประเทศ ปี 2555-2558 "
    ghp.x_labels = data_x
    ghp.add("Amount people", data_y)
    return ghp.render_to_file('graph_per_year.svg')

graph_per_year()
