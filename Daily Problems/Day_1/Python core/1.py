# 1. to accept id, name and salary

def form():
    id = int(input("Enter your id : "))
    name = input("Enter your name : ")
    name = name.strip()
    salary = input("Enter your salary : ")
    salary = salary.strip()


    print("====================================================================================")

    if (not (id == "" or name == "" or salary == "")) : 
        print('ID : {} \nName : "{}" \nSalary : "{}"'.format(id,name,salary))
    else :
        print("ID, name or salary can not be empty")



form()