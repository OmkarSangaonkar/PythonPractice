questions = [
    "1. What is the capital of France?",
    "2. Which planet is known as the 'Red Planet'?",
    "3. Which gas do plants absorb from the atmosphere during photosynthesis?",
    "4. Who wrote the play 'Romeo and Juliet'?",
    "5. What is the chemical symbol for gold?",
    "6. Which of the following is not a primary color in the subtractive color model?",
    "7. What is the largest mammal in the world?",
    "8. Which country is famous for the Great Wall?",
    "9. What is the main function of the mitochondria in a cell?",
    "10. Who was the first person to set foot on the moon?",
    "11. Who won most world cup in fifa in south America?",
    "12. Which Captain won all ICC trophies?",
    "13. What is National Sports of India?",
    "14. Which gas is more abondant in earth atmosphere?",
]

options = [
    ["London", "Berlin", "Paris", "Madrid"],
    ["Venus", "Jupyter", "Mars", "Saturn"],
    ["Oxyzen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
    ["Charles Dickens", "William Shakespeare", "Jane Austen", "Martin King"],
    ["Go", "Gold", "Ag", "Au"],
    ["Red", "Green", "Blue", "Yellow"],
    ["Elephant", "Tiger", "Blue Whale", "Camel"],
    ["China", "Itally", "India", "Egypt"],
    ["Photosynthesis", "Energy production", "Cell Division", "Waste elimination"],
    ["Neil Armstrong", "Buzz Aldrin", "John Glenn", "Yuri Gagarin"],
    ["Brazil", "Argentina", "Uruguay", "Chile"],
    ["AB devillers", "Michel Clark", "Eon Morgan", "M.S.Dhoi"],
    ["Cricket", "Football", "Hockey", "None"],
    ["Oxyzen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
]

answers = [3, 3, 2, 2, 4, 4, 3, 1, 2, 1, 1, 4, 4, 3]

levels = [
    1000,
    2000,
    5000,
    10000,
    20000,
    40000,
    80000,
    160000,
    320000,
    640000,
    1280000,
    2500000,
    5000000,
    10000000,
]


money = 0


money = 0

for i in range(0, len(questions)):
    print(f"Question for level {levels[i]}")
    print(questions[i])
    print(f"a. {options[i][0]}      b. {options[i][1]}")
    print(f"c. {options[i][2]}      d. {options[i][3]}")

    reply = int(input("Enter your answer: "))
    print("\n")
    if reply == answers[i]:
        print(f"Congrats! YOU WON Rs. {levels[i]}\n")
        if i == 13:
            money = 10000000
        elif i == 8:
            money = 320000
        elif i == 4:
            money = 10000
    else:
        print("Wrong answer! ")
        break

# Display the final money won based on the last level reached
print(f"Total money you won Rs. {money}")
