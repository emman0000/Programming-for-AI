#Practice Task 2 
def interact_with_user():
    user_name = input("What is your good name? ")
    print(f"Hello, {user_name.title()}!")

    print("I hope you are fine. Let me know how I can help you! (Start asking)")
    response = input("Are you doing well? (yes/no): ").strip().lower()

    if response == "yes":
        problem = input("Please share your problem with us: ")
        print("Thanks for your feedback, we will resolve your problem.")
    else:
       
        goodbye_message = "Okay! Good to see you, stay connected"
        print(goodbye_message.center(80))
      
interact_with_user()

