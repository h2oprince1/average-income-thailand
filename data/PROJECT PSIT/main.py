""" Family is income low than 30,000 Bath """
import matplotlib.pyplot as plt
import csv
def main():
    """ This main function """
    graph_per_region()
    graph_per_year()

def callflie():
    """
    Get values from database
    """
    file = open('data/database1.csv')
    data = csv.reader(file)
    table = [row for row in data]
    return table

def graph_per_region():
    """
    group data each years
    """
    table = callflie()
    years_2558 = [each for each in table if "2558" in each]
    years_2557 = [each for each in table if "2557" in each]
    years_2556 = [each for each in table if "2556" in each]
    years_2555 = [each for each in table if "2555" in each]
    
    values58 = locations(years_2558)
    values57 = locations(years_2557)
    values56 = locations(years_2556)
    values55 = locations(years_2555)


    x = ["South", "West", "East north", "Center", "East", "North"]
    ghp = plt.gca()
    ghp.set_title(u'จำนวนคนต่อครัวที่รายได้ต่ำกว่า 30,000 บาท แบ่งตามภาค',fontname='JasmineUPC',fontsize=20)
    ghp.set_xlabel(u'Region',fontname='JasmineUPC',fontsize=20)
    ghp.set_ylabel(u'Amount people',fontname='JasmineUPC',fontsize=20)
    ghp.plot(x,values58,'-om')
    ghp.plot(x,values57,'-oc')
    ghp.plot(x,values56,'-oy')
    ghp.plot(x,values55,'-or')
    ghp.legend([u'2558',u'2557',u'2556',u'2555'],loc=1,fancybox=1,shadow=1)
    plt.show()

def locations(year):
    """
    Share location each year.
    """
    south = [int(location[4].replace(",", "")) for location in year if "South" in location]
    west = [int(location[4].replace(",", "")) for location in year if "West" in location]
    east_n = [int(location[4].replace(",", "")) for location in year if "East north" in location]
    center = [int(location[4].replace(",", "")) for location in year if "Center" in location]
    east = [int(location[4].replace(",", "")) for location in year if "East" in location]
    north = [int(location[4].replace(",", "")) for location in year if "North" in location]

    listvaluse = [sum(south), sum(west), sum(east_n), sum(center), sum(east), sum(north)]
    return listvaluse
def graph_per_year():
    """
    Output Graph income per year.
    """
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
    ghp = plt.gca()
    ghp.plot(data_x,data_y,'--gs')
    ghp.axis([0, 4, 0, 140000])
    ghp.set_title(u'จำนวนคนต่อครัวที่รายได้ต่ำกว่า 30,000 บาทต่อปี',fontname='JasmineUPC',fontsize=20)
    ghp.set_xlabel('Years',fontname='JasmineUPC',fontsize=20)
    ghp.set_ylabel('Amount of familys below 30000 bath',fontname='JasmineUPC',fontsize=20)
    plt.show()

main()
