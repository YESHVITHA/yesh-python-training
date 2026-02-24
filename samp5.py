N = int(input("Enter number of students: "))
total_marks = 0
pass_students = 0
fail_students = 0
for i in range(N):
    mark = int(input(f"Enter mark of student {i+1}: "))
    if 0 <= mark <= 100:
        total_marks += mark
        if mark >= 40:
            pass_students += 1
        else:
            fail_students += 1
    else:
        print("Please enter between 0 and 100")
        break

average_marks = total_marks / N
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Passed Students:", pass_students)
print("Failed Students:", fail_students)
