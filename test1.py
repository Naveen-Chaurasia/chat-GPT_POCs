import json

emoloyees_string = '''
{
    "employees" : [
       {
           "first_name": "Michael", 
           "last_name": "Rodgers", 
           "department": "Marketing"
        },
       {
           "first_name": "Michelle", 
           "last_name": "Williams", 
           "department": "Engineering"
        }
    ]
}
'''
print(type(emoloyees_string))

data = json.loads(emoloyees_string)

print(type(data))
#output
#<class 'dict'>