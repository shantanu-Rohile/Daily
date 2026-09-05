# 9. Tuple Elements and String to Int Map

def split_list(sample1):
    name=list(map(lambda x:x[0],sample1))
    date=list(map(lambda x:x[1],sample1))
    weight=list(map(lambda x:x[2],sample1))

    return name,date,weight

print(split_list([('Alberto Franco','15/05/2002','35kg'), ('Gino Mcneill','17/05/2002','37kg'), ('Ryan Parkes','16/02/1999', '39kg'), ('Eesha Hinton','25/09/1998', '35kg')]))