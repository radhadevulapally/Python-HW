#importing required libraries
import csv

#Declaring variables and lists to place new values
total_votes = 0
persons = {}
candidates_percent_dict = {}
winner = "NONE"
count = 0
candidate_votes_dict= {}
#Reading the given CSV file
myfile='data.csv'
with open (myfile,'r') as csv_file:
  csv_reader=csv.reader(csv_file,delimiter=',')
#Skip header
  next(csv_reader) 
    #Loop through the file and grab the fields to set new values to the dictionaries
  for row in csv_reader:      
    total_votes = total_votes + 1
    candidate = row[2]
    if candidate in persons.keys():
           persons[candidate] = persons[candidate]+1
    else:
            persons[candidate] = 1
for key,value in persons.items():
    candidates_percent_dict[key] = round((value/total_votes)*100,2)
for key in persons.keys():
    if persons[key] > count:
        winner = key
        count = persons[key]
        
#Print results,Use str because other data types cant be concatenated with string

print("Election Results")
print("-------------------")
print("Total Votes: " + str(total_votes))
print("-------------------")
for key, value in persons.items():
    print(key + ": " + str(candidates_percent_dict[key]) + "% (" + str(value) + ")")
print("--------------------")
print("Winner: " + winner)


#Write to output text file

outputfile=open("results.txt","w")
outputfile.write("Election Results \n")
outputfile.write('--------\n')
outputfile.write("Total Votes: " + str(total_votes) + "\n")
outputfile.write('--------\n')
for key, value in persons.items():
  outputfile.write(key + ": " + str(candidates_percent_dict[key]) + "% (" + str(value) + ") \n")

outputfile.write("---------------\n")
outputfile.write("Winner: " + winner)



