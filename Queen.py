###########################################################################      
# Description:  Toronto Parking Tickets Capstone data preparation
# Owner:        Edward Johnson   ( email edward.johnson@ikinique.com)
# Created:      Spring 2019
# Language:     Python 3.7
# Status:       Developed during BrainStation Data Science course 
# Package:      none 
# Usage:        Convert Toronto Ward information into per address feed
#               Sample for Queen St and will be enhanced with long/lat
##########################################################################
import csv
with open ('QueenStC.csv','r') as csv_file:
    reader =csv.reader(csv_file)
    next(reader) # skip first row
    for row in reader:
        print(row)
        print(row[1])
        Streetname = row[0]
        Od1 = row[1]
        Od2 = row[2]
        Ev1 = row[3]
        Ev2 = row[4]
        Ward = row[5]
        Subward = row[6]
        #
        # Process odds
        #
        if Od1.strip():
            print ("Odd not blank")
            Odd1 = int(Od1)
            Odd2 = int(Od2)
            for makeline in range(Odd1, Odd2+2,2):
                if makeline % 2 == 1:
                    print ( "Process writing Odd", makeline, Streetname)
                    rowout = [ makeline, Streetname, Ward, Subward ]
                    with open('QueenStOut.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow(rowout)
                        csvFile.close()
        #
        # Process evens
        #
        if Ev1.strip():
            print ("Even not blank")
            Even1 = int(Ev1)
            Even2 = int(Ev2)
            for makeline in range(Even1, Even2+2,2):
                if makeline % 2 == 0:
                    print ( "Process writing Even", makeline, Streetname)
                    rowout = [ makeline, Streetname, Ward, Subward ]
                    with open('QueenStOut.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow(rowout)
                        csvFile.close()


 
