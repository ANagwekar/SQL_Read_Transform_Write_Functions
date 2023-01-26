#types of modes for openning a file
# r for reading – The file pointer is placed at the beginning of the file. This is the default mode.
# r+ Opens a file for both reading and writing. The file pointer will be at the beginning of the file.
# w Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
# w+ Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, it creates a new file for reading and writing.
# rb Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file.
# rb+ Opens a file for both reading and writing in binary format.
# wb+ Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, it creates a new file for reading and writing.
# a Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
# ab Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
# a+ Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
# ab+ Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
# x open for exclusive creation, failing if the file already exists (Python 3)



import csv

def open_csv_file(file_name):
    with open(file_name) as csvfile:
        csvreader = csv.reader(csvfile)

        #open empty list and append to it so can access the info as the 'with open' will close the file at the end of
        #the function
        list = []
        for row in csvreader:
            list.append(row)
        return list

print(open_csv_file('user_details.csv'))

def transform(file_name):
    opened = open_csv_file(file_name)

    # open empty list and append to it so can access the info as the with open will close the file at the end of the
    # function
    list2 = []
    list3 = []
    for row in opened:
        list2.append(row[1] + " " + row[2] + " " + str.partition(row[4], '@')[0])
    return list2

print(transform('user_details.csv'))

def write(file_name):
    transformed = transform(file_name)
    transformed_split = [] # Have to split for individual variables to be in separate so creates a list of lists
    for line in transformed:
        transformed_split.append(line.split(" "))

    with open('Transformed.csv','w', newline='') as user_select:
        details_writer = csv.writer(user_select)
        details_writer.writerows(transformed_split)

write('user_details.csv')