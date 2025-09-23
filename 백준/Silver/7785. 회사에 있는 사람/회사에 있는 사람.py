n = int(input().strip())

company = set()

for i in range(0,n):
    name, status = input().split()
	
    if status == 'enter':
        company.add(name)
    else:
        if name in company:
            company.remove(name)
    

result = sorted(list(company), reverse=True)

for person in result:
    print(person)