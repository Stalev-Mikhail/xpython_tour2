import time

def delayed_print(message, delay=0.8):
    print(message)
    time.sleep(delay)

delayed_print("--HALL--")
delayed_print("Mom: Mike, look who is there!")
delayed_print("You: Oh! I didn't expect to see you here! What do you need?")
delayed_print("Friend: It's sunny outside. Want to go out, bro?")
delayed_print("You: I need to ask my mom.")
delayed_print("Friend: Okay.")
delayed_print("--KITCHEN--")
delayed_print("You: Mom, can I go outside?")

while True:
    try:
        temp = int(input("Mom: What's the temperature? Isn't it cold? "))
        break
    except ValueError:
        delayed_print("Mom: I didn't understand you. Can you say it again?")

if temp <= 0:
    delayed_print("Mom: It's cold, isn't it?")
    delayed_print("You: So?")
    delayed_print("Mom: Next time, if it's too cold...")
    decision = input("Decide what you will do: 1 - give up, 2 - ask: ")
    
    if decision == '1':
        delayed_print("You: Okay, Mom.")
        delayed_print("--HALL--")
        delayed_print("You: Mom banned me from going outside.")
        delayed_print("Friend: Okay, next time!")
        delayed_print("&MIDDLE-BAD ENDING&")
        
    elif decision == '2':
        delayed_print("You: But why can't I go outside?")
        delayed_print("Mom: Because I care about your health!")
        delayed_print("You: Please!")
        delayed_print("Mom: NO!")
        delayed_print("You: But...")
        delayed_print("*Aggressive slap*")
        delayed_print("&BAD ENDING&")
        
elif temp > 0 and temp < 10:
    delayed_print("Mom: Cool!")
    delayed_print("Mom: Okay, but don’t forget to put on a cap")
    delayed_print("You: Yay! Thanks, Mom.")
    delayed_print("--HALL--")
    delayed_print("You: Mom allowed it!")
    delayed_print("Friend: Yes! Let’s go!")
    delayed_print("--STREET--")
    delayed_print("You: It's really warm! Why did I put on this cap?")
    delayed_print("Friend: What cap?")
    delayed_print("You: What!?")
    delayed_print("Friend: Uh, on...")
    delayed_print("Mom: YOU DIDN’T PUT ON A CAP!")
    delayed_print("You: B...")
    delayed_print("*Very aggressive slap with an axe*")
    delayed_print("&DEAD ENDING&")
    
elif temp >= 10:
    delayed_print("Mom: Nice weather we're having.")
    delayed_print("Mom: Okay, go!")
    delayed_print("You: Yay! Thanks, Mom.")
    delayed_print("--HALL--")
    delayed_print("You: Mom allowed it!")
    delayed_print("Friend: Yes! Let’s go!")
    delayed_print("--STREET--")
    delayed_print("&GOOD ENDING&")
