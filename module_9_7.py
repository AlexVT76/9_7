

def is_prime(func):
    def  wrapper(*args):
       value = func(*args)
       if value>2:
           for i in range(2,int(value**0.5+1)):
               if value % i ==0:
                  print ('Составное')
                  break

           print('Простое')

         

       else:
            print('Не является простым числом')


       return value
    return wrapper

@is_prime
def sum_three(x,y,z):
    return x+y+z

result = sum_three(2, 3, 6)
print(result)