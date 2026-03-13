#!/usr/bin/env python3
"""
My Own List - Private Transport Vehicles
A collection of 10 private transport vehicles with personalized ownership aspirations
"""

# Define a list containing 10 different private transport vehicles
# Mix includes both cars and motorcycles from various manufacturers
vehicles = [
    "Honda Civic",           # Reliable Japanese compact car
    "Toyota Supra",          # Legendary Japanese sports car
    "BMW R 1250 GS",         # German adventure motorcycle
    "Ford Mustang GT",       # Iconic American muscle car
    "Yamaha YZF-R1",         # Japanese high-performance sport bike
    "Mercedes-Benz G-Class", # German luxury off-road vehicle
    "Ducati Panigale V4",    # Italian superbike
    "Tesla Model S Plaid",   # American electric performance sedan
    "Harley-Davidson Street Glide", # American cruiser motorcycle
    "Porsche 911 Turbo S"    # German sports car
]

# Create personalized messages for each vehicle using f-strings
# Each message is unique and captures the essence of what makes each vehicle special
messages = [
    # Honda Civic message - focuses on reliability and daily driving experience
    f"I would like to own a {vehicles[0]} - the perfect blend of reliability and style that would make every daily commute feel like a celebration of practical elegance.",
    
    # Toyota Supra message - emphasizes performance and driving excitement
    f"I would like to own a {vehicles[1]} - to experience the legendary performance and turbocharged symphony that turns every open road into a personal racetrack.",
    
    # BMW R 1250 GS message - highlights adventure and capability
    f"I would like to own a {vehicles[2]} - to conquer both city streets and mountain passes with the confidence of knowing I'm riding one of the most capable adventure motorcycles ever engineered.",
    
    # Ford Mustang GT message - focuses on American muscle and sound
    f"I would like to own a {vehicles[3]} - to feel the raw American muscle and hear that iconic V8 roar, transforming ordinary drives into thunderous declarations of automotive passion.",
    
    # Yamaha YZF-R1 message - emphasizes technology and speed
    f"I would like to own a {vehicles[4]} - to experience the cutting-edge technology and race-bred performance that makes every twist of the throttle feel like touching pure, unadulterated speed.",
    
    # Mercedes-Benz G-Class message - focuses on timeless design and capability
    f"I would like to own a {vehicles[5]} - to command the road with timeless boxy elegance and unmatched off-road capability, proving that true icons never go out of style.",
    
    # Ducati Panigale V4 message - describes it as art and performance
    f"I would like to own a {vehicles[6]} - to own a rolling work of Italian art that delivers spine-tingling performance and head-turning beauty at every stoplight.",
    
    # Tesla Model S Plaid message - focuses on futuristic technology
    f"I would like to own a {vehicles[7]} - to experience the future of transportation with instant electric acceleration that makes supercars feel like they're moving in slow motion.",
    
    # Harley-Davidson Street Glide message - emphasizes freedom and classic appeal
    f"I would like to own a {vehicles[8]} - to embrace the freedom of the open road with classic American styling and that deep, rumbling exhaust note that speaks to the soul of every rider.",
    
    # Porsche 911 Turbo S message - highlights engineering and luxury
    f"I would like to own a {vehicles[9]} - to possess the ultimate combination of everyday usability and track-ready performance, where engineering perfection meets everyday luxury."
]

# Display the title and introduction
print("=== MY OWN LIST OF DREAM VEHICLES ===\n")

# Print the numbered list of vehicles
print("10 Private Transport Vehicles I'd Love to Own:\n")
# Use enumerate to number each vehicle starting from 1
# Format with right-aligned numbers for clean presentation
for i, vehicle in enumerate(vehicles, 1):
    print(f"{i:2d}. {vehicle}")

# Add visual separator and title for messages section
print("\n" + "="*60)
print("PERSONALIZED OWNERSHIP ASPIRATIONS")
print("="*60 + "\n")

# Display each personalized message with numbering
for i, message in enumerate(messages, 1):
    print(f"{i:2d}. {message}\n")

# Add concluding statement about the significance of these vehicles
print("Each vehicle represents not just transportation, but a different facet of automotive passion,")
print("engineering excellence, and the pure joy of the open road.")
