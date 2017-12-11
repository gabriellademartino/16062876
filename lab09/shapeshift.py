from datetime import datetime as dt

with open('shapeshift.csv', 'r') as file:
    reader = csv.DictReader(file)

# opens the csv file and reads the lines - please change directory to open it

orderedlist = []

for row in reader:
    time = dt.fromtimestamp(float(row['timestamp']))
    row['timestamp'] = time
    orderedlist.append(row)

#coonverts the time from the unix to the date time format and adds to a list

orderedlist.sort(key = lambda t : t['timestamp'])

# sorts the list into the right order

print 'The ordered list is:'
print orderedlist

