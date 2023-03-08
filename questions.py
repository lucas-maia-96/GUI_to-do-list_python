import json

with open("questions.json", 'r') as file:
    content = file.read()
    
data = json.loads(content)

score = 0

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index+1}-{alternative}")
    user_choice = int(input("What do you think ?  "))
    question["user_choice"] = user_choice
    if user_choice == question["correct_answer"]:
        score += 1
    print()

rate = 100*(score/len(data))

print(f"Your Score: {score}/{len(data)} -> {rate}% \n")

see =  input("Do you want to know more about your answers? (y/n)  ")

if see == 'n':
    print("Ok, bye !")
elif see == 'y':
    for index, question in enumerate(data):
        if question['user_choice'] == question['correct_answer']:
            result = "Correct"
        else:
            result = "Wrong"
            
        message = f"Q{index+1} {result} -> You: {question['user_choice']} | Correct: {question['correct_answer']}"
        print(message)
