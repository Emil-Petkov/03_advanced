peoples = {'Peter': 21, 'George': 18, 'John': 45, }

print(sorted(peoples.items(), key=lambda kvp: kvp[0]))
''' 
peoples.items() -> create list of tuples with kvp pairs  
 
[0] sorted by name -> [('George', 18), ('John', 45), ('Peter', 21)]
[1] sorted by age -> [('George', 18), ('Peter', 21), ('John', 45)]
'''
