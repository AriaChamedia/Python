from hf import generate_response

def reinforcement_learning():
    prompt=input("Please enter a prompt")
    response=generate_response(prompt)
    print(f"Response: {response}")
    rate=int(input("""Please give me a rating from 1-5
    1 being the lowest and 5 being the highest: """))
    
    if rate<1 and rate>5:
        print("invalid rating. Please enter a number between 1 and 5.")
        
    feedback=input("Please give me feedback on how to improve my response: ")
    new_prompt=f"""Initial prompt: {prompt}
    Initial response: {response}
    Feedback: {feedback}
    Rating: {rate}
    How can you improve your response based on the feedback and rating?"""
    new_response=generate_response(new_prompt)
    print(f"Improved Response: {new_response}")

def role_based_prompt():
    print("Role based prompt") 
    category=input("Enter a category (eg.science, history, math): ")
    item=input("Enter an item in that category (eg. Photosynthesis, World War II, Pythagorean theorem): ") 
    teacher_prompt=f"""You are a teacher, please explain this {item} in simple language """
    expert_prompt=f"""You are an expert in {category}, please explain this {item} in detail with technical terms"""
    teacher_response=generate_response(teacher_prompt)
    expert_response=generate_response(expert_prompt)
    print(f"Teacher response: {teacher_response}")
    print(f"Expert response: {expert_response}")
    
          
    

print("AI Learning")
print("Choose one")
print("1) Reinforcement learning")
print("2) Role based prompt")
choice=input("Enter 1 or 2: ")

if choice == "1":
    reinforcement_learning()
elif choice == "2":
    role_based_prompt() 
else:
    print("Invalid choice. Please enter 1 or 2.")    
       

