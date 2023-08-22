import matplotlib.pyplot as p
import csv
def top_ten_batsmen():
    x = []
    y = []
    counter = 0
    with open('t20.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')  # separates by comma
        csvfile.readline()  # ignores the titles/names for each column
        # essentially ignores first line of the file to avoid errors in
        # calculations
        for row in plots:
            if counter < 10:  # only gets the top 10 out of a total of 2007
                # batsmen
                if row[6] != '-':  # only proceeds if the player actually has
                    # scored runs
                    x.append(row[1])  # adds name of player
                    y.append(int(row[6]))  # adds the player's respective runs
                    counter += 1  # increments to account for the addition of a
                    # name to the list of 10
    #  for visualization:
    p.xticks(
        rotation='vertical')  # makes all x-axis labels vertical; saves space
    p.bar(x, y, color='b', width=0.72, label="Runs")  # colour, width, and
    # representation of the bars (representation means what do the bars
    # symbolize)
    p.xlabel('Names')  # x-axis title
    p.ylabel('Runs')  # y-axis title
    p.title('Top 10 Batsmen in T20 Format in Terms of Runs (From Years 1877 -'
            ' 2020)')  # title of the graph
    p.legend()
    p.show()

def top_ten_matches():
    dct = {}
    with open('t20.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')  # separates by comma
        csvfile.readline()  # ignores the titles/names for each column
        # essentially ignores first line of the file to avoid errors in
        # calculations
        for row in plots:
            dct[row[1]] = row[3]  # gets the name and respective matches played
            # for further analysis later on
    # gathering matches for IND, NZ, PAK, AUS, ENG, AFG, SA, IRE and others
    matches = {'India': 0, 'New Zealand': 0, 'Pakistan': 0, 'Australia': 0,
               'England': 0, 'Afghanistan': 0, 'South Africa': 0, 'Ireland': 0,
               'Others': 0}
    for element in dct:
        if element.__contains__('IND'):
            matches['India'] += int(dct[element])
        elif element.__contains__('NZ'):
            matches['New Zealand'] += int(dct[element])
        elif element.__contains__('PAK'):
            matches['Pakistan'] += int(dct[element])
        elif element.__contains__('AUS'):
            matches['Australia'] += int(dct[element])
        elif element.__contains__('ENG'):
            matches['England'] += int(dct[element])
        elif element.__contains__('AFG'):
            matches['Afghanistan'] += int(dct[element])
        elif element.__contains__('(SA') or element.__contains__('SA)'):
            matches['South Africa'] += int(dct[element])
        elif element.__contains__('(IRE') or element.__contains__('IRE)'):
            matches['Ireland'] += int(dct[element])
        else:
            matches['Others'] += int(dct[element])
    teams = []
    matches2 = []
    for i in matches:
        if i != 'Others':  # not including other teams in the pie chart
            teams.append(i)
            matches2.append(matches[i])
    #  for visualization:
    p.pie(matches2, labels=teams, autopct='%.2f%%')  # forming the pie chart
    p.title('Matches Played by Players from Teams That Appear on The \'Top 10 '
            'Batsmen\' List', fontsize=20)  # setting the title and font size
    p.show()

def all_matches():
    dct = {}
    with open('t20.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')  # separates by comma
        csvfile.readline()  # ignores the titles/names for each column
        # essentially ignores first line of the file to avoid errors in
        # calculations
        for row in plots:
            dct[row[1]] = row[3]  # gets the name and respective matches played
            # for further analysis later on
    # gathering matches for IND, NZ, PAK, AUS, ENG, AFG, SA, IRE and others
    matches = {'India': 0, 'New Zealand': 0, 'Pakistan': 0, 'Australia': 0,
               'England': 0, 'Afghanistan': 0, 'South Africa': 0, 'Ireland': 0,
               'Others': 0}
    for element in dct:
        if element.__contains__('IND'):
            matches['India'] += int(dct[element])
        elif element.__contains__('NZ'):
            matches['New Zealand'] += int(dct[element])
        elif element.__contains__('PAK'):
            matches['Pakistan'] += int(dct[element])
        elif element.__contains__('AUS'):
            matches['Australia'] += int(dct[element])
        elif element.__contains__('ENG'):
            matches['England'] += int(dct[element])
        elif element.__contains__('AFG'):
            matches['Afghanistan'] += int(dct[element])
        elif element.__contains__('(SA') or element.__contains__('SA)'):
            matches['South Africa'] += int(dct[element])
        elif element.__contains__('(IRE') or element.__contains__('IRE)'):
            matches['Ireland'] += int(dct[element])
        else:
            matches['Others'] += int(dct[element])
    teams = []
    matches2 = []
    for i in matches:  # no if condition means it includes all teams
        teams.append(i)
        matches2.append(matches[i])
    #  for visualization:
    p.pie(matches2, labels=teams, autopct='%.2f%%')  # forming the pie chart
    # setting the title and font size
    p.title('Matches Played by Players from Teams That Appear on The \'Top 10 '
            'Batsmen\' List,\n as Compared to All Other Teams', fontsize=20)
    p.show()

switch = True  # while this remains true the program will keep asking user for
# input
while switch:  # only exits when user enters a number instead of a string
    try:
        method_to_run = int(input("Which graph/chart would you like to see "
                                  "being displayed (Please enter either 1, 2, "
                                  "or 3):\n "
                                  "\n"
                                  "1. Top 10 Batsmen in T20 Format in Terms "
                                  "of Runs "
                                  "(From Years 1877 - 2020) \n"
                                  "\n"
                                  "2. Matches Played by Players from Teams "
                                  "That Appear "
                                  "on The \'Top 10 Batsmen\' List \n"
                                  "\n"
                                  "3. Matches Played by Players from Teams "
                                  "That Appear "
                                  "on The \'Top 10 Batsmen\' List, "
                                  "as Compared to All "
                                  "Other Teams \n\nYour input: "))
        switch = False
    except ValueError:
        print("\nInput must be either the number 1, 2, or 3. Try again.")
        switch = True
        # If program executes this part above, it means invalid input
        continue  # Avoids infinite loop error
    if method_to_run == 1:
        top_ten_batsmen()
    elif method_to_run == 2:
        top_ten_matches()
    elif method_to_run == 3:
        all_matches()
    else:  # in case that user enters a number, but it is not associated with
        # any graph/chart
        print("Invalid input. Please restart the program and enter valid "
              "input.")
