
#CodingBat Exercises
# Source: http://codingbat.com/

'''Warmup-1 > sleep_in 
http://codingbat.com/prob/p173401
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
'''
def sleep_in(weekday, vacation):
  return not weekday or vacation


'''
Given a non-empty string like "Code" return a string like "CCoCodCode".
string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
'''
def string_splosion(str):
    if not str:
        return ''
    splosion_word = ''
    for position in range(0, len(str)):
        splosion_word += str[:position + 1]
    return splosion_word

'''
Warmup-1 > monkey_trouble 
http://codingbat.com/prob/p120546
Given a non-empty string like "Code" return a string like "CCoCodCode".
string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
'''

def monkey_trouble(a_smile, b_smile): #a smile - false || b smile true
    we_are_in_trouble = (a_smile and b_smile) or (not a_smile and not b_smile)
    return we_are_in_trouble

def sum_double(a, b):
  return a + b if a != b else (a + b) * 2

'''
Logic-2 > make_bricks 
http://codingbat.com/prob/p118406
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
'''
def make_bricks(small, big, goal):
    #Function to test if sum of all bricks is smaller than goal. If so,
    #obviously we will never match the goal :)
    is_total_smaller_than_goal = lambda goal, small, big : (small * 1 + big * 5) < goal
    
    #Here we test if small brickes are enough to match the goal.
    #E.g: Suppose we have as entries:
    # small=3 Small bricks (Remember: each one represents 1 inch)
    # big=1 brick (Remeber: each one represents 1 inch)
    # goal=8 (This is the number we need to match in order to know whether is possible or not)
    #First, we know that our both entries small and big (3 + 5 = 8 inches) are not smaller
    #than goal.(we know that by previous function is_total_smaller_than_goal return)
    #Now, we must know if it's possible to match that value.
    #If we divide the goal by five (8 / 5 in this case) and obtain the module (3 in this case)
    #it's fairly possible to get to know if it's possible to match the goal number.
    #(If the module from 8 / 5 results 3 (3 inches), so we need AT LEAST 3 small bricks)
    # to get to goal number! (5 + 3 = 8)
    does_small_bricks_matches_goal = lambda goal, small_bricks_quantity : small_bricks_quantity < (goal % 5)
    if is_total_smaller_than_goal(goal, small, big) or \
    does_small_bricks_matches_goal(goal, small):
        return False
    return True
  

''' A simple method for testing-solution purposes.'''
def test(current, expected):
    message = 'Current : \'{0}\' - Expected: \'{1}\''.format(repr(current), repr(expected))
    if current == expected:
        message += '[Success]'
    else:
        message += '[Failed]'
    print(message)
 
def main():
    print('\n|--- String Splosion Test ---|')
    test(string_splosion('Code'), 'CCoCodCode')
    test(string_splosion('abc'), 'aababc')
    test(string_splosion('ab'), 'aab')

    print('\n|--- Sleep_in Tests ---|')

    test(sleep_in(False, False), True)
    test(sleep_in(True, False), False)
    test(sleep_in(False, True), True)

    print('\n|--- Monkey_trouble Tests ---|')
    test(monkey_trouble(True, True), True)
    test(monkey_trouble(False, False), True)
    test(monkey_trouble(True, False), False)
    test(monkey_trouble(False, True), False)

    print('\n|--- Monkey_trouble Tests ---|')
    test(monkey_trouble(True, True), True)
    test(monkey_trouble(False, False), True)
    test(monkey_trouble(True, False), False)
    test(monkey_trouble(False, True), False)

    print('\n|--- make_bricks Tests ---|')
    test(make_bricks(0, 3, 10), True)
    test(make_bricks(1, 4, 12), False)
    test(make_bricks(3, 1, 7), True)
    test(make_bricks(1, 1, 7), False)
    test(make_bricks(2, 1, 7), True)
    test(make_bricks(7, 1, 11), True)
    test(make_bricks(7, 1, 8), True)
    test(make_bricks(7, 1, 13), False)
    test(make_bricks(43, 1, 46), True)
    test(make_bricks(40, 1, 46), False)
    test(make_bricks(1000000, 1000, 1000100), True)

if __name__ == '__main__':
    main()
