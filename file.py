# create file in write mode replaces the content if already exists
try:
    with open('docs/readme.txt', 'w') as f:
        f.write('Create')
except FileNotFoundError:
    print('The directory doen not exist')

# x mode gives warning if file already exists
with open('docs/readme.txt', 'x') as f:
    f.write('Create')

