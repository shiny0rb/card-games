# check if an integer to sort error
def is_int(val):
    if type(val) == int:
        return True
    else:
      return False


import random

# initial arrays (lists)
suits = ['hearts','diamonds','clubs','spades']
suit = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
suitsA = ['H','D','C','S']
deck = []
decks= [*range(1,52)]


# build the pack up from individual suits and cards
for i in suitsA:
  for j in suit:
    if is_int(j):
      j=str(j)
    deck.append(j+i)  

print(deck)

random.shuffle(decks)
print(decks)

print(deck[0:5])

j=0

'''
for i in decks:
  j+=1
  if j<=5:
    print(deck[i], end =" , ")
    j=0
    print('\n')

'''

print(decks)

for i in decks:
  print(deck[i])

for i in deck:
  print(i)

l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


print (len(l))
for i in range(int(len(l)/5+1)):
  print(",".join(l[i*5:(i+1)*5]) + "\n")


my_file = open("defaultdeck.txt", "r")
content = my_file.read()
print(content)
content_list = content.split("\n")
my_file.close()
print(content_list)

cleandeck = []

for e in content_list:
  print(e)
  e = e.strip('\n')
  e = e.strip('\t')
  cleandeck.append(e)

print(cleandeck,"\n")

print(cleandeck[0])
print (len(cleandeck))
cleandeck.pop(0)
cleandeck.pop(0)
cleandeck.pop(-1)
cleandeck.pop(-1)
print(cleandeck[0])
print (len(cleandeck))

orig_cleandeck = cleandeck.copy()

print (orig_cleandeck)

random.shuffle(cleandeck)z
for i in range(int(len(cleandeck)/5+1)):
  print(",".join(cleandeck[i*5:(i+1)*5]) + "\n")
random.shuffle(cleandeck)
