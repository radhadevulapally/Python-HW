#importing required libraries
import csv

#reading csv file
myfile="data.csv"
with open(myfile,"r") as csv_file:
    csv_reader=csv.reader(csv_file)
    #creating and setting variables,lists
    dates_list=[]
    profit_loss_list=[]
    prev_value=0
    change_in_profit_loss_list=[]
    initial_profit=0
    #skip header
    next(csv_reader)
    #looping throgh file and getting values
    for row in csv_reader:
         dates_list.append(row[0])
         profit_loss_list.append(int(row[1]))
         change_value=int(row[1])-prev_value
         change_in_profit_loss_list.append(change_value)
         prev_value=int(row[1])
         total_value=sum(profit_loss_list)
         monthly_change=change_value/len(dates_list)-1
         
         #final result
         
print('Financial Analysis')
print('----------------------------')

print("Total months:",len(dates_list))
print("Total:",sum(profit_loss_list) )
print('average Change $',monthly_change )
    
print("Greatest increase in profits: ",dates_list[change_in_profit_loss_list.index(max(change_in_profit_loss_list))],  max(change_in_profit_loss_list))
print("Greatest Decrease in Profits: ",dates_list[change_in_profit_loss_list.index(min(change_in_profit_loss_list))],  min(change_in_profit_loss_list))

#result to output1 text file by opening in write mode and writing the required statements
file='Output1.txt'
with open(file, 'w') as writefile1:
 writefile1.write('Financial Analysis' + '\n')
 writefile1.write('----------------------------' + '\n')


 writefile1.write("Total months:" + str(len(dates_list)) + '\n')

 writefile1.write("Total:" + str(sum(profit_loss_list)) + "\n")
 writefile1.write('average Change $' + str(monthly_change) + "\n" )
    

 writefile1.write("Greatest increase in profits: " + str(dates_list[change_in_profit_loss_list.index(max(change_in_profit_loss_list))]) + str(max(change_in_profit_loss_list)) + "\n")
 writefile1.write("Greatest Decrease in Profits: " + str(dates_list[change_in_profit_loss_list.index(min(change_in_profit_loss_list))]) + str(min(change_in_profit_loss_list)) + "\n")
         
