# Create a dictionary
a = {
  'one': 1,
  'two': 2,
  'three': 3
}
b = dict({
  'one': 1 ,
  'two': 2,
  'three': 3
})
print("print dicitionay b --", b)

# Using zip() to create a dictionary from two lists
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print("print dictionary c is --", c)

# Creating a dictionary from tuples
d = dict([('one', 1), ('two', 2), ('three', 3)])
print("print dictionary creates using another way", d)
print("print dictionary ", a)

# Add an new item to a dictionary
a['four'] = 4
print("print updated dictionary", a)

# Add multiple items
a.update({'five': 5, 'six': 6})
print("print updated dictionary", a) 

# Dictionary Membership
print("test membership:", 'five' in a) # membership test (only in keys)
print("test membership:", 5 in a) # membership do not check in values
print("test membership:",  'seven' in a)

print("Dictionary", zip('packt', range(5)))
print("Dictionary is", dict(zip('packt', range(5))))

a = dict(zip('packt', range(5)))
print("length of dictionary a is", len(a)) # length of dictionary a
print("Check the value of a key c is", a['c']) # to check the value of a key

print(a.pop('a')  )
print("print updated dictionary",a)

b = a.copy()
print("print copy of a dictionary:", b)

print("Print keys of dictionary ",a.keys())

print("print values of a dictionary", a.values())


print("print items of dictionary",a.items())

a.update({'a':1})   # add an item in the dictionary
print("updated dictionary", a)

a.update(a=22)  # update the value of key 'a'
print("updated dictionary after changing the value of a-- ", a)
{'p': 0, 'c': 2, 'k': 3, 't': 4, 'a': 22}



