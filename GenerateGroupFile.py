# Generate a fresh student group file from the ADUsers.csv file that gets updated daily
import csv
import os


def generateGroupFile(groupTXT,groupCSV,building,grade):
    inputfile = csv.reader(open('C:\\Users\\zechaaron\\Downloads\\ADUsers.csv', 'r'))
    outputfile = open('C:\\Users\\zechaaron\\OneDrive - Osseo Area Schools\\Documents\\AD\\'+groupTXT, 'w')

    header = next(inputfile)
    for line in inputfile:

        #  Grab All PCSH students
        if grade == 'PCSH-ALL':
            if line[7] == "PCSH":
                format = "1_" + line[2] + "," + line[7]  # line 7 is student buildings
                print(format)  # prints out all the Student IDs in the spread sheet
                outputfile.write(format + '\n')
        #  Grab Students by building/grade
        if line[7] == building and line[5] == grade:
            format = "1_" + line[2] + "," + line[7] + "," + line[5]  # line 7 is student buildings, line 5 is Grade
            print(format)  # prints out all the Student IDs in the spread sheet
            outputfile.write(format + '\n')

    # close files
    outputfile.close()

    # rename file to CSV
    try:
         os.rename('C:\\Users\\zechaaron\\OneDrive - Osseo Area Schools\\Documents\\AD\\'+groupTXT, 'C:\\Users\\zechaaron\\OneDrive - Osseo Area Schools\\Documents\\AD\\' + groupCSV)
    except WindowsError:
        os.remove('C:\\Users\\zechaaron\\OneDrive - Osseo Area Schools\\Documents\\AD\\'+groupCSV)
        os.rename('C:\\Users\\zechaaron\\OneDrive - Osseo Area Schools\\Documents\\AD\\'+groupTXT,
                  'C:\\Users\\zechaaron\\OneDrive - Osseo Area Schools\\Documents\\AD\\'+groupCSV)

    print("File Generated");
