# 12. Write List to File

def list_to_file(name,lst):
    with open(name,"w") as file:
        file.writelines(lst)

list_to_file("new.txt",["Apple\n","Orange\n","Banana\n","Indian Berries\n"])
        