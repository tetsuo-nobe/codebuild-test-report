"""
 FizzBuzz 
   3 の倍数なら 'Fizz' を返す
   5 の倍数なら 'Buzz' を返す
   3 と 5 の公倍数なら 'FizzBuzz' を返す
"""
def fizzbuzz(i):
    if i % 15 == 0:
        return 'FizzBuzz'
    if i % 3 == 0:
        return 'Fizz'
    if i % 5 == 0:
        return 'Buzz'
    return str(i)