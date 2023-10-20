print("Enter score list")
score_list=input()
split_list=score_list.split(',')
max_score=0
for element in split_list:
    temporary_element=int(element)
    if max_score<temporary_element:
       max_score=temporary_element
print (max_score)