import json

doctor_companions = {}
doctor_companions['12th Doctor'] = 'Bill Potts'

doctor_companions['11th Doctor'] = 'The Ponds'

doctor_companions['10th Doctor'] = 'Donna Noble'

doctor_companions['9th Doctor'] = 'Rose Tyler'
print(json.dumps(doctor_companions))

with open('doctor_companions.json', 'w') as doctor_companions_file:
    doctor_companions_file.write(json.dumps(doctor_companions))

