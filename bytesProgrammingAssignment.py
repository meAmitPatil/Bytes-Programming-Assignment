import glob
print("Enter Date Range:")
startDate = input("Start Date(dd/mm/yyyy):")    #Enter the start Date
startDay = int(startDate.split("/")[0])        #Extract the start day
endDate = input("End Date(dd/mm/yyyy):")    #Enter the end Date
endDay = int(endDate.split("/")[0])     #Extract the End day
print("Report for the period:",startDate,"to",endDate)

a = []
b = []
temp = []
freq = {}
date = []
path = "logs/*.*"       #Path to the logs
for file in glob.glob(path):        #Iterate through all the files in the logs folder
    for line in open(file, 'r'):        #Iterate through all the lines in the file
        if(line != '\n' and line.split(" ")[-3] == 'disconnected'):     #Check if the line is a disconnection
            date = line.split(" ")[-8]
            date = date.split("/")[0]
            date = int(date.split("(")[1])
            if(date >= startDay and date <= endDay):        #Check if the date is in the range
                a = line.split(" ")[1]  
                temp.append(a.split(":")[1]) #
    for items in temp:      #Iterate through all the items in the temp list
        freq[items] = temp.count(items)
    for key, value in freq.items():     #Display all the items in the freq dictionary
        print ("% s : % d"%(key, value))        #Display the Computer Name and their Number of Disconnections
       


