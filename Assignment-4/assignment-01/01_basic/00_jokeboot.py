# Constants
PROMPT = "What would you like? (Type 'Fact' for a fun fact): "
FACT = "Here is a fun fact! 🧠 Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still perfectly edible!"
SORRY = "Sorry, I only share fun facts!"

def main():
    # Asking the user for input
    user_input = input(PROMPT)
    
    # Checking if the user input is "Fact"
    if user_input == "Fact":
        print(FACT) 
    else:
        print(SORRY)

# Main function ko call karna
if __name__ == '__main__':
    main()
