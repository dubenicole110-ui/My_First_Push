students = {}
while True:
    name = input("enter student name (or 'done' to quit):")
    if name.lower() == "done":
        break
    
    score = float(input("Enter score :"))
    students[name] = score

print("student info")

total = 0
for name ,score in students.items():
        print(name,":" ,score)
        total += score
average = total/len(students)

print("Class Aveage", average)

