import random

GroupCode = str(random.randint(0,10000))

string1 = '''document.querySelectorAll("[href*='''
string2 = "'/Settings"+"/EntityGroup/EditGroupFormAsync?entityCode="+GroupCode+"'"
string3 = ''']")[0].click()'''
string4 = string1+string2+string3
print(string4)