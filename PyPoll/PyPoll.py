import csv

d = {}
no_of_votes=0
with open('Resources/election_data.csv') as csv_file:
    reader = csv.reader(csv_file,delimiter = ",")
    header = next(reader)

    for i in reader:
        no_of_votes = no_of_votes+1
        if i[2] in d:
            d[i[2]] += 1
        else:
            d[i[2]] = 1

#khan_percentage = (d['Khan']/total_votes)*100
khan_percentage_votes = (d['Khan']/no_of_votes)*100
correy_percentage_votes = (d['Correy']/no_of_votes)*100
li_percentage_votes = (d['Li']/no_of_votes)*100
otooley_percentage_votes = (d["O'Tooley"]/no_of_votes)*100

otooley_votes = d["O'Tooley"]
winner_candidate = max(d.keys(),key=(lambda k:d[k]))


print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {no_of_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percentage_votes:.3f}% ({d['Khan']})")
print(f"Correy: {correy_percentage_votes:.3f}% ({d['Correy']})")
print(f"Li: {li_percentage_votes:.3f}% ({d['Li']})")
print(f"O'Tooley: {li_percentage_votes:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {winner_candidate}")
print(f"----------------------------")

file = open("PyPoll.txt",'w')
file.write(f"Election Results")
file.write("\n")
file.write(f"----------------------------")
file.write("\n")
file.write(f"Total Votes: {no_of_votes}")
file.write("\n")
file.write(f"----------------------------")
file.write("\n")
file.write(f"Khan: {khan_percentage_votes:.3f}% ({d['Khan']})")
file.write("\n")
file.write(f"Correy: {correy_percentage_votes:.3f}% ({d['Correy']})")
file.write("\n")
file.write(f"Li: {li_percentage_votes:.3f}% ({d['Li']})")
file.write("\n")
file.write(f"O'Tooley: {li_percentage_votes:.3f}% ({otooley_votes})")
file.write("\n")
file.write(f"----------------------------")
file.write("\n")
file.write(f"Winner: {winner_candidate}")
file.write("\n")
file.write(f"----------------------------")
