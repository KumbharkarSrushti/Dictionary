Sample_string='w3resource'
my_dict={}
for letter in Sample_string:
    my_dict[letter]=my_dict.get(letter,0)+1
print(my_dict)