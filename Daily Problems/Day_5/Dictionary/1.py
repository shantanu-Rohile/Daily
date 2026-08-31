# 1. Sort a dictionary using value

# Trivia : You might be wondering what type of name 47 is, actually it is name of protagnist from famaous video game series named 'Hitman'

def sort_dict_by_values(sample):

    res=dict(sorted(sample.items(),key=lambda item:item[1]))

    print(res) 

sample = {"name":47, "age" :22, "id": 23, "phone number" : 9011223344}
sort_dict_by_values(sample)



    