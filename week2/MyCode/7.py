import csv
name = ['Nurs','Ars','Xer']
soname = ['Turugeldiev','Hekas','ahja']
age = [18,21,12]

for i in range(0,len(name)):
    print(name[i],soname[i],age[i])

for i in range(0,len(name)):
    if(name[i]=='Nurs' and soname[i]=='Turugeldiev'):
        indexForDelete = i
del(name[indexForDelete])
del(soname[indexForDelete])
del(age[indexForDelete])


# print(name)
# print(soname)
# print(age)

