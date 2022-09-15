# f = open("text.txt", "w")
# f.write("text text")
# f.close()
import csv
f = open("people.csv", "a", newline = "")
tup1 = ("bob", 19)
writer = csv.writer(f)
writer.writerow(tup1)
f.close()
