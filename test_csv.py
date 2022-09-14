import csv
with open('resources/SampleCSVFile_11kb.csv') as csvfile:
    table = csv.reader(csvfile)
    # row_count = sum(1 for row in table)
    for line_no, line in enumerate(table, 1):
        if line_no == 2:
            print(line[1])
