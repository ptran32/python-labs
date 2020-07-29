import pprint
from faker import Faker

pp = pprint.PrettyPrinter()
fake = Faker()

employee = {}

for i in range(1, 11):
    employee[i] = {}
    employee[i]['uuid'] = fake.uuid4()
    employee[i]['name'] = fake.name()
    employee[i]['address'] = fake.address()
    employee[i]['email'] = fake.email()
    employee[i]['job'] = fake.job()
    employee[i]['country'] = fake.country()

# Uncomment it to see the raw dict 
# pp.pprint(employee)

# Print employee's information
# Split the uuid to get only the fist group of digit
for value in employee.values():
    print(f"""
    {value['uuid'].split('-')[0]}, {value['name']}, {value['email']}, {value['job']}, {value['country']}
    """, end='')