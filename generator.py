import memory_profiler as mem_profile
import random
import time

name = ['John','Corey','Adam','Steve','Rick','Thomas']
majors = ['Math','Computer','Arts','Business','Engineering','AI']

print('Memory (Before): ' + str(mem_profile.memory_usage()) + 'MB')

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                  'id' : i,
                  'name': random.choice(name),
                  'major': random.choice(majors),
                 }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
                  'id' : i,
                  'name': random.choice(name),
                  'major': random.choice(majors),
                 }
        yield person


t1 = time.clock()
#people = people_list(1000000)
people = list(people_generator(1000000))
t2 = time.clock()

print('Memory (After): ' + str(mem_profile.memory_usage()) + 'MB')
print ((t2-t1),' seconds')
