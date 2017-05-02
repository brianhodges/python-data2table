x = 0
y = 0
tab = ' ' * 4
countries = [
    {
        'name':'USA',
        'population':'350 million'
    },
    {
        'name':'China',
        'population':'1.4 billion'
    },
    {
        'name':'Russia',
        'population':'145 million'
    }
]

print '\nDUMP:'
print(countries)
print '\nSANITIZED:'

print '['
while x < len(countries):
    print tab + str(countries[x])
    x += 1
print ']'

print '\nTABLE:'
        
# loop countries array of objects
print 'Countries | Population'
print '-' * len('Countries | Population')
while y < len(countries):
    z = len('Countries ') - len(countries[y]['name'])
    print countries[y]['name'] + (' ' * z) + '|' + countries[y]['population']
    y += 1

print '\n'
