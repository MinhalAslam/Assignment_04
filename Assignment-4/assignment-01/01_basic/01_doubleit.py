def main():
    # User input a number
    curr_value = int(input("Enter a number: "))  
    
    # Jab tak value 50 se choti hai, tab tak loop chalega
    while curr_value < 50:
        curr_value = curr_value * 2  # double a value
        print(curr_value, end=" ")  # Print karna (ek hi line me output dikhane ke liye)

# Main function ko call karna
if __name__ == '__main__':
    main()