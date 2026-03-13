#!/usr/bin/env python3
"""
People List Manager
An interactive program that allows users to remove people from a list and view remaining names
"""

# Initialize the list with 10 people's names
# This is our main data structure that stores all the people
people_list = [
    "Alice Johnson",      # Person 1
    "Bob Smith",          # Person 2  
    "Charlie Brown",      # Person 3
    "Diana Prince",       # Person 4
    "Ethan Hunt",         # Person 5
    "Fiona Apple",        # Person 6
    "George Lucas",       # Person 7
    "Hannah Montana",     # Person 8
    "Ian McKellen",       # Person 9
    "Julia Roberts"       # Person 10
]

def display_menu():
    """Display the main menu options to the user"""
    # Print a formatted menu with visual separators
    print("\n" + "="*50)
    print("PEOPLE LIST MANAGER")
    print("="*50)
    print("1. Show current list")           # Option to view remaining people
    print("2. Remove a person from the list") # Option to delete someone
    print("3. Exit")                        # Option to quit the program
    print("="*50)

def show_list():
    """Display the current list of people"""
    # Check if the list is empty first
    if not people_list:
        print("\n❌ The list is currently empty!")
        return  # Exit the function early if empty
    
    # Display the number of people remaining in the list
    print(f"\n📋 Current list ({len(people_list)} people):")
    print("-" * 40)
    
    # Use enumerate to number each person starting from 1
    # Format with right-aligned numbers for clean presentation
    for i, person in enumerate(people_list, 1):
        print(f"{i:2d}. {person}")
    
    print("-" * 40)

def remove_person():
    """Remove a person from the list based on user input (name or number)"""
    # Check if the list is empty before trying to remove
    if not people_list:
        print("\n❌ The list is empty! Nothing to remove.")
        return  # Exit early if no people to remove
    
    # Show current list to help user see available names and numbers
    print("\n👥 Current people in the list:")
    for i, person in enumerate(people_list, 1):
        print(f"{i:2d}. {person}")
    
    # Prompt user for input with clear instructions for both options
    print("\n📝 Enter the name OR the number of the person you want to remove:")
    print("   Option 1: Type the full name as shown above")
    print("   Option 2: Type the number (1-10) next to the person")
    
    # Get user input and remove any extra whitespace
    user_input = input("➡️  Name or Number: ").strip()
    
    # Try to handle as a number first (more efficient for this case)
    try:
        # Convert input to integer to check if it's a valid number
        person_number = int(user_input)
        
        # Check if the number is within valid range
        if 1 <= person_number <= len(people_list):
            # Calculate the index (lists are 0-indexed, but display is 1-indexed)
            index_to_remove = person_number - 1
            person_to_remove = people_list[index_to_remove]
            
            # Remove the person from the list
            people_list.pop(index_to_remove)
            print(f"\n✅ Successfully removed '{person_to_remove}' from the list!")
        else:
            print(f"\n❌ Invalid number! Please enter a number between 1 and {len(people_list)}.")
            
    except ValueError:
        # If conversion to int fails, treat input as a name
        name_to_remove = user_input
        
        # Check if the entered name exists in our list
        if name_to_remove in people_list:
            people_list.remove(name_to_remove)  # Remove the person from the list
            print(f"\n✅ Successfully removed '{name_to_remove}' from the list!")
        else:
            # Handle case where name wasn't found
            print(f"\n❌ '{name_to_remove}' was not found in the list.")
            print("   Please make sure you typed the name exactly as it appears.")
            print("   Or enter the number next to the person instead.")

def main():
    """Main program loop"""
    # Display welcome message
    print("🎯 Welcome to the People List Manager!")
    print("   Manage your list by removing people and viewing the remaining names.")
    
    # Main program loop - continues until user chooses to exit
    while True:
        display_menu()  # Show menu options
        
        try:
            # Get user's menu choice
            choice = input("\n🔢 Enter your choice (1-3): ").strip()
            
            # Handle each menu option
            if choice == '1':
                show_list()  # Display current list
            elif choice == '2':
                remove_person()  # Remove someone from list
            elif choice == '3':
                # User wants to exit - show final list and goodbye message
                print("\n👋 Thank you for using People List Manager!")
                print("   Final list:")
                show_list()
                break  # Exit the while loop
            else:
                # Handle invalid menu choices
                print("\n⚠️  Invalid choice. Please enter 1, 2, or 3.")
                
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\n👋 Program interrupted. Goodbye!")
            break
        except Exception as e:
            # Handle any other unexpected errors
            print(f"\n❌ An error occurred: {e}")

# This ensures the main() function only runs when the script is executed directly
# (not when imported as a module)
if __name__ == "__main__":
    main()
