for items in range(5):
    problem = {"Name": input("Name"), "ExpYears": int(input("Years")), "Salary": int(input("Salary")), }
    if(problem["ExpYears"] > 5):
        problem["Salary"] = 1.5 * problem["Salary"]
