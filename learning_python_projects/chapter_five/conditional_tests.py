car = ['bmw']
print(car == ['bmw'])
#When this was just 'bmw' it would evaluate to false. 
#This is because a string cannot evaluate to a list.
print(car == ['subaru'])
car.append('subaru')

for cars in car:    
    if cars == 'bmw':
        print(f'{cars.upper()}')
    else: print(cars.title())
print('The next section is regarding age')
age = 31
print(age > 32)
print(age >= 32)
print(age == 31)
print(age < 32)
print(age <= 32)
age_2 = 25
print(age > age_2)
print(age > 45 or age_2 > 21)
print(age > 45 and age_2 > 21)

voter_ages = list(range(1,26))
print(voter_ages)
for voter_age in voter_ages:
    if voter_age <= 17:
        print(f"{voter_age}, Ineligible to Vote")
    else:  print(f"{voter_age}, Eligible to Vote")