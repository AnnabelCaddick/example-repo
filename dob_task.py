

names = []
dates_of_birth = []
with open("DOB.txt") as file:
    for line in file:
        line =line.strip()
        
        if not line:
            continue
        
        parts = line.split()

        DOB = " ".join(parts[-3:])
        name = " ". join(parts[:-3])

        names.append(name)
        dates_of_birth.append(DOB)

print ("\n NAMES")
for n in names:
    print(n)
        
print("\n")

print ("DATES OF BIRTH")
for d in dates_of_birth:
    print(d)
