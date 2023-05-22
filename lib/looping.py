i = 0
while i < 5:
    print("looping")
    i += 1



for i in range(10):
    print("looping")
    print(f"i is :{i}")



# list comprehensions
player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]


player_heights = [height * 7920 for height in player_heights] 

print(player_heights)

i = 0
while i < 10:
    print('happening new year')
    i += 1




def square_integers(int_list):
    square_integers = list()
    for integer in int_list:
        square_integers.append(integer**2)
        return square_integers
    

    # Write a function fizzbuzz() that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz".
def fizzbuzz():
    num = 0
    while num < 100:
        if num % 3 == 0 and num % 5 != 0:
            print("Fizz")
        elif  num % 5 == 0 and num % 3 != 0:  
            print("Buzz")
        elif num % 5 == 0 and num % 3 == 0:
            print("FizzBuzz")   
        else:
            print(num)  


fizzbuzz()
print(square_integers([1,2,3,4,5]))
