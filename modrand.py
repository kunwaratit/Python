

#import random
# def range():
#    num1 = int(input('enter 1strange:'))
#   num2 = int(input('enter lastrange:'))
#    num = [1, 2, 3, 4, 5, 6, 7]
#    print(num[num1-1:num2])
for items in range(5):
    problem = {
        "Name": input("Name"),
        "ExpYears": int(input("Years")),
        "Salary": int(input("Salary")),
    }
    if(problem["ExpYears"] > 5):
        problem["Salary"] = 1.5 * problem["Salary"]
        print(f'{problem["Salary"]}')
    else:
        print(problem["Salary"])
