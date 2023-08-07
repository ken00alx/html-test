name = 'Eric'
profession =  'commedian'
affiliation = 'Monty python'

message = (
    f"Hi {name}. "
    f"You are a {profession}. "
    f"You were in {affiliation}. "
)

print(message)

import timeit
timeit.timeit ("""name = "Eric"
               age = 74
               '%s is %s.' % (name, age)""", number = 10000)
print(timeit)