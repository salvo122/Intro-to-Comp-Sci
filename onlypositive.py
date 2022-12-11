def ask():
    while True:
        try: 
            number= int(input("Enter ONLY a positive number: "))
            while number <= 0:
                number= int(input("Enter ONLY a positive number: "))
                if number > 0:
                    break
                else: 
                    print "Try again!"
            return number    
        except ValueError:
            print "That's not a number"
    
print ask()