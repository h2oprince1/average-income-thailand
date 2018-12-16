""" Family is income low than 30,000 Bath """
import matplotlib.pyplot as plt
import pygal
import csv
def main():
    """ This main function """
    graph_per_region()

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


    x = ["", "South", "West", "East north", "Center", "East", "North", ""]
    ghp = pygal.Line()
    ghp.x_labels = x
    ghp.title = " จำนวนคนต่อครัวที่รายได้ต่ำกว่า 30,000 บาท แบ่งตามภาค "
    ghp.add("2558", values58)
    ghp.add("2557", values57)
    ghp.add("2556", values56)
    ghp.add("2555", values55)
    return ghp.render_to_file('graph_per_region.svg')

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

    listvaluse = [0, sum(south), sum(west), sum(east_n), sum(center), sum(east), sum(north), 0]
    return listvaluse

main()
