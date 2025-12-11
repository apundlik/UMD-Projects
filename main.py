def main():
    # In Python, we don't need to import a Scanner; we use the built-in input() function.
    
    questions = [
        "I give clear explanations of what is expected of others.",
        "I show interest in followers’ personal concerns.",
        "I invite followers to participate in decision making.",
        "I challenge followers to continuously improve their work performance.",
        "I give followers explicit instructions for how to do their work.",
        "I show concern for the personal well-being of my followers.",
        "I solicit followers’ suggestions before making a decision.",
        "I encourage followers to consistently raise their own standards of performance.",
        "I give clear directions to others for how to proceed on a project.",
        "I listen to others and give them encouragement.",
        "I am receptive to ideas and advice from others.",
        "I expect followers to excel in all aspects of their work."
    ]
    
    definitions = ("Respond with the frequency you do this behavior by typing the following: \n"
                   "'1' for never, '2' for seldom, '3' for sometimes, '4' for often, and '5' for always")

    scores = []

    # Input Loop
    for question in questions:
        print(definitions)
        print(question)
        
        # We use a while loop to ensure the user actually enters an integer
        valid_input = False
        while not valid_input:
            try:
                user_input = int(input("Enter score: "))
                scores.append(user_input)
                valid_input = True
            except ValueError:
                print("Please enter a valid integer number.")
        
        print("\n\n")

    # Python lists allow us to define the size implicitly, 
    # but here we calculate the sums based on the specific indices from the Java code.
    final_scores = [0] * 4

    # Directive Leadership (Indices 0, 4, 8)
    final_scores[0] = scores[0] + scores[4] + scores[8]
    # Supportive Leadership (Indices 1, 5, 9)
    final_scores[1] = scores[1] + scores[5] + scores[9]
    # Participative Leadership (Indices 2, 6, 10)
    final_scores[2] = scores[2] + scores[6] + scores[10]
    # Achievement-oriented Leadership (Indices 3, 7, 11)
    final_scores[3] = scores[3] + scores[7] + scores[11]

    # Find the highest score
    largest = max(final_scores)

    # Determine Result
    # Logic note: If there is a tie, this prioritizes the styles in the order they appear below.
    if largest == final_scores[0]:
        print("Your leadership style is: Directive Leadership")
    elif largest == final_scores[1]:
        print("Your leadership style is: Supportive Leadership")
    elif largest == final_scores[2]:
        print("Your leadership style is: Participative Leadership")
    else:
        print("Your leadership style is: Achievement-oriented Leadership")

if __name__ == "__main__":
    main()
