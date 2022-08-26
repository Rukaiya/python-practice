companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]

def sort_key(company):
    return company[2]

# companies.sort(key=sort_key, reverse=True)

# using lambda expression
companies.sort(key= lambda company: company[2])
print(companies)


