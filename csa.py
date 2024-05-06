import random
import time

print("Choose Some Adventure (C)")
print("2019 - 2024")

# Ask for the player's age
age = int(input("Please enter your age: "))

while True:
    print("Name:      Mr. Smith")
    print("Balance:   $35.50 AUD")
    print("You are down at Australia, Victoria, Bendigo at a Bendigo Marketplace when you realize that you forgot lol")
    print("1: Do a shopping spree of exactly $30.50 for no reason lol")
    print("2: Leave")

    choice = input("(1/2) --> ")

    if age >= 18:
        if choice == "1":
            print("Name:      Mr. Smith")
            print("Balance:   $0.00 AUD")
            print("You got the 'Broke' ending.")
            print("-Zeke")
            time.sleep(2)  # Wait for 2 seconds
            break
        elif choice == "2":
            place = "au:bendigo:market:carpark"
            print("Name:     Mr. Smith")
            print("Balance:  $35.50")
            print("You left your keys in the locked car.")
            print("1: Get a taxi (it costs $5)")
            print("2: Get a locksmith (it costs $10)")
            print("3: Stay")

            choice = input("(1/2/3) --> ")

            if choice == "1":
                place = "au:bendigo:market:carpark:taxi"
                print("Name:     Mr. Smith")
                print("Balance:  $30.50")
                print("1: Go home")
                print("2: Go to work (you're 10 minutes late)")
                print("3: Go to the pub")

                sub_choice = input("(1/2/3) --> ")

                if sub_choice == "1":
                    print("Name:     Mr. Smith")
                    print("Balance:  $30.50")
                    print("ayo this aint my house")
                    print("You got the 'Kidnapped' ending.")
                    time.sleep(2) # Wait for 2 seconds
                    break
                elif sub_choice == "2":
                    print("Name:     Mr. Smith")
                    print("Balance:  $30.50")
                    print("You got the 'Work' ending.")
                    print("-Zeke")
                    time.sleep(2)  # Wait for 2 seconds
                    break
                elif sub_choice == "3":
                    print("Name:     Mr. Smith")
                    print("Balance:  $30.50")
                    print("1: Have vodka  ($20)")
                    print("2: Have beer   ($20)")
                    print("3: Have wine   ($20)")

                    sub_choice = input("(1/2/3) --> ")

                    if sub_choice == "1":
                        print("Name:     Mr. Smith")
                        print("Balance:  $10.50")
                        print("You got the 'Drunk with Vodka' ending.")
                        print("-Zeke")
                        time.sleep(2)  # Wait for 2 seconds
                        break
                    elif sub_choice == "2":
                        print("Name:     Mr. Smith")
                        print("Balance:  $10.50")
                        print("You got the 'Drunk with Beer' ending.")
                        print("-Zeke")
                        time.sleep(2)  # Wait for 2 seconds
                        break
                    elif sub_choice == "3":
                        print("Name:     Mr. Smith")
                        print("Balance:  $10.50")
                        print("You got the 'Drunk with Wine' ending.")
                        print("-Zeke")
                        time.sleep(2)  # Wait for 2 seconds
                        break

            elif choice == "2":
                print("Name:     Mr. Smith")
                print("Balance:  $25.50")
                print("1: Go home")
                print("2: Go to work (you're 10 minutes late)")
                print("3: Go to the pub")

                sub_choice = input("(1/2/3) --> ")

                if sub_choice == "1":
                    randInt = random.randint(1, 10000)
                    print("Name:     Mr. Smith")
                    print("Balance:  $30.50")
                    print("1: Go do coding (like what im doing)")
                    print("2: Go play games (like what im making)")
                    if randInt == 69420:
                        print("3: <?> <?> <?> <?> <?> <?> <?> <?> <?> <?> <?> <?> <?>")

                    sub_choice = input("(1/2) --> ")

                    if sub_choice == 1:
                        print("loloololololollloollllo")
                    elif sub_choice == "2":
                        print("Name:     Mr. Smith")
                        print("Balance:  $30.50")
                        print("You got the 'Coding' ending.")
                elif sub_choice == "2":
                    print("Name:     Mr. Smith")
                    print("Balance:  $30.50")
                    print("You got the 'Work' ending.")
                    print("-Zeke")
                    time.sleep(2)  # Wait for 2 seconds
                    break
                elif sub_choice == "3":
                    print("Name:     Mr. Smith")
                    print("Balance:  $30.50")
                    print("1: Have vodka  ($20)")
                    print("2: Have beer   ($20)")
                    print("3: Have wine   ($20)")

                    sub_choice = input("(1/2/3) --> ")

                    if sub_choice == "1":
                        print("Name:     Mr. Smith")
                        print("Balance:  $10.50")
                        print("You got the 'Drunk with Vodka' ending.")
                        print("-Zeke")
                        time.sleep(2)  # Wait for 2 seconds
                        break
                    elif sub_choice == "2":
                        print("Name:     Mr. Smith")
                        print("Balance:  $10.50")
                        print("You got the 'Drunk with Beer' ending.")
                        print("-Zeke")
                        time.sleep(2)  # Wait for 2 seconds
                        break
                    elif sub_choice == "3":
                        print("Name:     Mr. Smith")
                        print("Balance:  $10.50")
                        print("You got the 'Drunk with Wine' ending.")
                        print("-Zeke")
                        time.sleep(2)  # Wait for 2 seconds
                        break

            elif choice == "3":
                print("Name:      Mr. Smith")
                print("Balance:   $35.50 AUD")
                print("You got the 'Lost' ending.")
                print("-Zeke")
                time.sleep(2)  # Wait for 2 seconds
                break
        else:
            print("no not that")
    else:
        import random
        import time

        print("Choose Some Adventure (C)")
        print("2019 - 2024")

        while True:
                print("Name:      Mr. Smith")
                print("Balance:   $35.50 AUD")
                print("You are down at Australia, Victoria, Bendigo at a Bendigo Marketplace when you realize that you forgot lol")
                print("1: Do a shopping spree of exactly $30.50 for no reason lol")
                print("2: Leave")

                choice = input("(1/2) --> ")

                if choice == "1":
                        print("Name:      Mr. Smith")
                        print("Balance:   $0.00 AUD")
                        print("You got the 'Broke' ending.")
                        print("-Zeke")
                        time.sleep(2)  # Wait for 2 seconds
                        break
                elif choice == "2":
                        place = "au:bendigo:market:carpark"
                        print("Name:     Mr. Smith")
                        print("Balance:  $35.50")
                        print("You left your keys in the locked car.")
                        print("1: Get a taxi (it costs $5)")
                        print("2: Get a locksmith (it costs $10)")
                        print("3: Stay")

                        choice = input("(1/2/3) --> ")

                        if choice == "1":
                                place = "au:bendigo:market:carpark:taxi"
                                print("Name:     Mr. Smith")
                                print("Balance:  $30.50")
                                print("1: Go home")
                                print("2: Go to work (you're 10 minutes late)")
                                print("3: Go to the pub")

                                sub_choice = input("(1/2/3) --> ")

                                if sub_choice == "1":
                                        print("Name:     Mr. Smith")
                                        print("Balance:  $30.50")
                                        print("ayo this aint my house")
                                        print("You got the 'Kidnapped' ending.")
                                        time.sleep(2) # Wait for 2 seconds
                                        break
                                elif sub_choice == "2":
                                        print("Name:     Mr. Smith")
                                        print("Balance:  $30.50")
                                        print("You got the 'Work' ending.")
                                        print("-Zeke")
                                        time.sleep(2)  # Wait for 2 seconds
                                        break
                                elif sub_choice == "3":
                                        print("Name:     Mr. Smith")
                                        print("Balance:  $30.50")
                                        print("1: Have vodka  ($20)")
                                        print("2: Have beer   ($20)")
                                        print("3: Have wine   ($20)")

                                        sub_choice = input("(1/2/3) --> ")

                                        if sub_choice == "1":
                                                print("Name:     Mr. Smith")
                                                print("Balance:  $10.50")
                                                print("You got the 'Drunk with Vodka' ending.")
                                                print("-Zeke")
                                                time.sleep(2)  # Wait for 2 seconds
                                                break
                                        elif sub_choice == "2":
                                                print("Name:     Mr. Smith")
                                                print("Balance:  $10.50")
                                                print("You got the 'Drunk with Beer' ending.")
                                                print("-Zeke")
                                                time.sleep(2)  # Wait for 2 seconds
                                                break
                                        elif sub_choice == "3":
                                                print("Name:     Mr. Smith")
                                                print("Balance:  $10.50")
                                                print("You got the 'Drunk with Wine' ending.")
                                                print("-Zeke")
                                                time.sleep(2)  # Wait for 2 seconds
                                                break

                        elif choice == "2":
                                print("Name:     Mr. Smith")
                                print("Balance:  $25.50")
                                print("1: Go home")
                                print("2: Go to work (you're 10 minutes late)")
                                print("3: Go to the pub")

                                sub_choice = input("(1/2/3) --> ")

                                if sub_choice == "1":
                                        randInt = random.randint(1, 10000)
                                        print("Name:     Mr. Smith")
                                        print("Balance:  $30.50")
                                        print("1: Go do coding (like what im doing)")
                                        print("2: Go play games (like what im making)")
                                        if randInt == 69420:
                                                print("3: <?> <?> <?> <?> <?> <?> <?> <?> <?> <?> <?> <?> <?>")

                                        sub_choice = input("(1/2) --> ")

                                        if sub_choice == 1:
                                                print("loloololololollloollllo")
                                        elif sub_choice == "2":
                                                print("Name:     Mr. Smith")
                                                print("Balance:  $30.50")
                                                print("You got the 'Coding' ending.")
                                elif sub_choice == "2":
                                        print("Name:     Mr. Smith")
                                        print("Balance:  $30.50")
                                        print("You got the 'Work' ending.")
                                        print("-Zeke")
                                        time.sleep(2)  # Wait for 2 seconds
                                        break
                                elif sub_choice == "3":
                                        print("Name:     Mr. Smith")
                                        print("Balance:  $30.50")
                                        print("1: Have vodka  ($20)")
                                        print("2: Have beer   ($20)")
                                        print("3: Have wine   ($20)")

                                        sub_choice = input("(1/2/3) --> ")

                                        if sub_choice == "1":
                                                print("Name:     Mr. Smith")
                                                print("Balance:  $10.50")
                                                print("You got the 'Drunk with Vodka' ending.")
                                                print("-Zeke")
                                                time.sleep(2)  # Wait for 2 seconds
                                                break
                                        elif sub_choice == "2":
                                                print("Name:     Mr. Smith")
                                                print("Balance:  $10.50")
                                                print("You got the 'Drunk with Beer' ending.")
                                                print("-Zeke")
                                                time.sleep(2)
                                                break  # Wait for 2 seconds
