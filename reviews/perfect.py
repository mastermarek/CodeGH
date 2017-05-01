import math
import random

# Eerste opdracht (Rock, Paper, Scissors)
def get_RPS():
    RPS=raw_input('Rock, Paper or Scissors?:')
    while (RPS) != 'Rock' and (RPS) != 'Paper' and (RPS) != 'Scissors':
        print 'That is not Rock, Paper or Scissors!\n'
        RPS=raw_input('Rock, Paper or Scissors?:')
    return RPS
    
def compare(x,y):
    if x == 'Rock' and y == 'Rock': print 'Tie'
    if x == 'Rock' and y == 'Scissors': print 'Player 1 wins!'
    if x == 'Rock' and y == 'Paper': print 'Player 2 wins!'
    if x == 'Paper' and y == 'Rock': print 'Player 1 wins!'
    if x == 'Paper' and y == 'Scissors': print 'Player 2 wins!'
    if x == 'Paper' and y == 'Paper': print 'Tie'
    if x == 'Scissors' and y == 'Rock': print 'Player 2 wins!'
    if x == 'Scissors' and y == 'Scissors': print 'Tie'
    if x == 'Scissors' and y == 'Paper': print 'Player 1 wins!'
    
# Opdracht Methods
def is_divisible(m,n):
    divisible = False
    if n==0:
        divisible=False
    elif m%n ==0:
        divisible = True
    return divisible

# De != operator zonder != te gebruiken
def not_equal(x,y):
    equal = True
    if x==y:
        equal= False
    return equal
    
def multadd(x,y,z):
    return x*y+z
    
def yikes(x):
    return x*math.exp(-x)+math.sqrt(1-math.exp(-x))
    
def absolute_value(x):
    if x>=0:
        return x
    if x < 0:
        return math.sqrt(x*x)
    
def rand_divis_3():
    number = random.randint(0,100)
    print number
    if number % 3 != 0:
        number_by_3 = False
    if number % 3 == 0:
        number_by_3 = True
    return number_by_3

def roll_dice(y,x):
    outcome = random.randint(x*1,x*y)
    return outcome
    
def roll_dice2(x,y):
    list_dice=[]
    while len(list_dice) < x:
        height_dice = random.randint(1,y)
        list_dice.append(height_dice)
    print list_dice[0]
    print list_dice[1]
    print list_dice[2]
    return 'That\'s all!'
    
def sum_list(x): # x must be a list with numbers!
    sum_sum_list = 0
    for num in x:
        sum_sum_list += num
    return sum_sum_list

def find_element(x,y): #x must be a list, y must be the element to find)
    for i in range (0,len(x)):
        if x[i]==y:
            return i
    
def find_maximum(x): # x must be a list)
    grootste = 0
    for i in x:
        if i > grootste:
            grootste=i
    return grootste
        


# --------------------------------Main----------------------------------


"""
compare('Rock','Paper')
compare('Rock','Scissors')
compare('Paper','Paper')
"""

# Deze moet je zelf invullen met een raw_input:
"""
a = get_RPS()
b = get_RPS()
z= compare(a,b)
"""

# Method True or False
print "is_divisible(10, 5) == ", is_divisible(10,5)
print "is_divisible(18, 7) == ", is_divisible(18,7)
print "is_divisible(42, 0) == ",  is_divisible(42,0)

# De != operator als funcitie. Als not_equal == True dan is het dus
# hetzelfde als !=
print 'Are 5 and 6 not equal?', not_equal(5,6)
print 'Are 5 and 5 not equal?', not_equal(5,5)
print 'Are the words hello and hello not equal?', not_equal('hello','hello')

if not_equal(5,5)==True:
    print 'HELL YEAH'
if not_equal(5,5)==not_equal('hello', 'hello'):
    print 'Hell yeah AGAIN'
    
# De math operator! De multadd functie werkt
print 'Werkt mijn multadd functie als je getallen invoert?\
 Test voert in 3,5,100 en er komt uit:', multadd(3,5,100)
 
# Test voor multadd ANGLE_TEST
angle_test = multadd(0.5, math.cos((math.pi)/4), math.sin((math.pi)/4))
print 'De uitkomst van angle_test is:', angle_test

# Test voor multadd CEILING_TEST
ceiling_test=multadd(2,math.log(12,7),math.ceil(276.0/19))
print 'De uitkomst van de ceiling_test is:', ceiling_test

# Yikes
print 'Wat is de yikes van 5? Dat is:', yikes(5)

# 2.6
print 'The absolute value of -33 is:', absolute_value(-33)

print rand_divis_3()

print 'Mijn eerste dobbelsteen functie was heel kort maar gaf niet\
elke uitkomst appart!', roll_dice(6,3)

print 'Mijn tweede wel', roll_dice2(3,6)

number_list= [1,3,5,7]
print sum_list(number_list)

# Bij deze heb ik (voor de grap?) dat je zelf een input moet geven voor het element dat je zoek.
# print find_element(number_list, input('Vul hier het element dat je zoek in de lijst [1,3,5,7]'))

# print het maximum van de ingevulde lijst.
print find_maximum(number_list)

look = 'Look at me!'
now = 'NOW'

print look[:-1]+now+look[-1]
print look*2+look[:-1]+now+look[-1]


## PLOTTEN