""" Total human per year each region """
import pygal
import csv
def main():
    """ This main function this program """
    table = callfile()
    y58, y57, y56, y55 = group_data(table)
    human58 = locations(y58, 3)
    human57 = locations(y57, 3)
    human56 = locations(y56, 3)
    human55 = locations(y55, 3)

    eachsouth = [human55[0], human56[0], human57[0], human58[0]]
    eachwest = [human55[1], human56[1], human57[1], human58[1]]
    eacheast_n = [human55[2], human56[2], human57[2], human58[2]]
    eachcenter = [human55[3], human56[3], human57[3], human58[3]]
    eacheast = [human55[4], human56[4], human57[4], human58[4]]
    eachnorth = [human55[5], human56[5], human57[5], human58[5]]

    group_values = [eachsouth, eachwest, eacheast_n, eachcenter, eacheast, eachnorth]
    create_ghp(group_values).render_to_file('Chart/graph_total_people_each_years.svg')

def callfile():
    """
    Get values from database
    """
    file = open('database/database1.csv')
    data = csv.reader(file)
    table = [row for row in data]
    return table

def group_data(table):
    """
    Group data each years
    """
    years_2558 = [each for each in table if "2558" in each]
    years_2557 = [each for each in table if "2557" in each]
    years_2556 = [each for each in table if "2556" in each]
    years_2555 = [each for each in table if "2555" in each]
    return years_2558, years_2557, years_2556, years_2555

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

def create_ghp(list_in):
    """
    Creath the graph type Pie.
    """
    line_chart = pygal.Bar()
    line_chart.title = ('จำนวนประชากรทั้งหมดแต่ละภาค [CHART B3]\nปี พ.ศ. 2555-2558')
    line_chart.x_labels = map(str, range(2555, 2559))
    line_chart.add('North', list_in[5])
    line_chart.add('West', list_in[1])
    line_chart.add('East north', list_in[2])
    line_chart.add('Central', list_in[3])
    line_chart.add('East', list_in[4])
    line_chart.add('South', list_in[0])
    return line_chart

main()
