""" Calculation per low income than 30000 """
import pygal
import csv
import numpy as np
def main():
    """
    This main function
    """
    table = callfile()
    years_2558 = [each for each in table if "2558" in each]
    years_2557 = [each for each in table if "2557" in each]
    years_2556 = [each for each in table if "2556" in each]
    years_2555 = [each for each in table if "2555" in each]

    lowincome58 = locations(years_2558, 4)
    lowincome57 = locations(years_2557, 4)
    lowincome56 = locations(years_2556, 4)
    lowincome55 = locations(years_2555, 4)

    avg58 = (np.array(lowincome58) / sum(lowincome58)) * 100
    avg57 = (np.array(lowincome57) / sum(lowincome57)) * 100
    avg56 = (np.array(lowincome56) / sum(lowincome56)) * 100
    avg55 = (np.array(lowincome55) / sum(lowincome55)) * 100

    list58 = list(avg58)
    list57 = list(avg57)
    list56 = list(avg56)
    list55 = list(avg55)

    createpie_ghp(list58, "2558").render_to_file('Chart/graph_percen58.svg')
    createpie_ghp(list57, "2557").render_to_file('Chart/graph_percen57.svg')
    createpie_ghp(list56, "2556").render_to_file('Chart/graph_percen56.svg')
    createpie_ghp(list55, "2555").render_to_file('Chart/graph_percen55.svg')


def callfile():
    """
    Get values from database
    """
    file = open('database/database1.csv')
    data = csv.reader(file)
    table = [row for row in data]
    return table

def locations(year, loca):
    """
    Share location each year.
    """
    south = [int(location[loca].replace(",", "")) for location in year if "South" in location]
    west = [int(location[loca].replace(",", "")) for location in year if "West" in location]
    east_n = [int(location[loca].replace(",", "")) for location in year if "East north" in location]
    center = [int(location[loca].replace(",", "")) for location in year if "Center" in location]
    east = [int(location[loca].replace(",", "")) for location in year if "East" in location]
    north = [int(location[loca].replace(",", "")) for location in year if "North" in location]

    listvaluse = [sum(south), sum(west), sum(east_n), sum(center), sum(east), sum(north)]
    return listvaluse

def createpie_ghp(list_in, year):
    """
    Creath the graph type Pie.
    """
    pie_chart = pygal.Pie()
    pie_chart.title = ('ร้อยละประชากรต่อครัวเรือนที่มีรายได้ต่ำกว่า 30,000 บาท ปี พ.ศ. %s (%%)' %year)
    pie_chart.add('North', float2(list_in[5]))
    pie_chart.add('West', float2(list_in[1]))
    pie_chart.add('East north', float2(list_in[2]))
    pie_chart.add('Central', float2(list_in[3]))
    pie_chart.add('East', float2(list_in[4]))
    pie_chart.add('South', float2(list_in[0]))
    return pie_chart

def float2(var_in):
    """
    Transfer float values to .2
    """
    var = "%.2f"% var_in
    return float(var)
main()
