print("Hi Im Alonso")

message = "Im a student at FIU"
print(message[0])
print(type(message))


a = 10
b = 3

print(a + b) #addition
print(a - b) #subtraction
print(a * b) #multiplication
print(a / b) #division
print(10/2)
print(a // b) #floor division
print(a ** b) #a to the power of b
print(a % b) #modulo

professors = ["greg", "kianoosh", "debra", "patricia", "richard"]
print(professors[0])
print(professors[1:3])
print(professors[-1])
professors.append("jim")
print(professors)
professors.remove("jim")
professors.extend(["heather", "kevin", "jason"])
print(professors)
professors.insert(2, "trevor")
print(professors)
professors[3] = "mark"
print(professors)
print(professors[3:5]) # accessing professors in positions 3 and 4
print(professors[5:])
print(professors[:3])
print(professors[:])
print(professors.remove("kianoosh"))
print(professors)
print(professors.index("mark"))
x = professors.pop(6)
print(professors)
print(x)
print(len(professors))
print(type(professors))
professors.sort(reverse=True)
print(professors)

for i in professors:
    print(i)
    print(i.title())
    print("FIU")
print("FIU")

water_data = {
    "temperature":[78,89,92],
    "pH":[6.5,6.7,6.3],
    "oxygen":[7.2,5.6,3.5],
}

print(water_data["oxygen"])

import pandas as pd
df = pd.DataFrame(water_data)
print(df)




