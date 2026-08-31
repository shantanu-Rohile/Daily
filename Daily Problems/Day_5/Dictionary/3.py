# 3. Concatenate Dictionaries
def concatenate_dictionary(sample1,sample2):
    sample1.update(sample2)
    return sample1

student = {
    "name": "Rahul",
    "age": 21,
    "course": "Computer Science"
}
prices = {
    "apple": 1.50,
    "banana": 0.75,
    "orange": 1.20
}


print(concatenate_dictionary(student,prices))