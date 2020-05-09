
import csv
link=input("input file name:")
file = open(link,encoding="utf8")
stringList = file.readlines()
i=1

with open('coutletter_'+link+'.csv', 'w', newline='\n',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["line", "Number character"])
    print("Waiting to count...")
    for line in stringList:
        n=len(line)-1 
        writer.writerow([i,n])
        i=i+1
print("Completed")

# Coded by Canh Lam #
