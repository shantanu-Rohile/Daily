# 2. Add Key to Dictionary

def add_new_key(sample,key,value="no value given by user"):
    sample.update({key:value})
    return sample

student ={"name":"Klein Moretti", "University":"Khoy University", "Department":"History"}

print(add_new_key(student,"Age",22))