
print_number = 1;

while print_number <= 100:
    word = ''
    if((print_number % 3) == 0):
        word += 'FIZZ'
    
    if((print_number % 5) == 0):
        word += 'BUZZ'
    
    if(word != ''):
        print(word)
    else:
        print(print_number)
    print_number += 1

