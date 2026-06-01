from hf import generate_response

def get_essay_details():
    topic=input("what is the topic of your essay: ")
    essay_type=input("What type of essay are you writing (descriptive, persuasive, argumentative): ")
    length=int(input("What is the desired length of your essay (300, 900, 1200, 2000 words): "))
    target_audience=input("Who is your target audience (General public, students, professionals): ") 
    return {"topic": topic, "essay_type": essay_type, "length": length, "target_audience": target_audience}

def generated_essay(details):
    temperature=float(input("Enter a temperature setting (0.1-Structured, 0.7-Creative): "))
    if temperature<0.1 or temperature>0.9:
        temperature=0.3
    prompt=f"Write a {details['length']} word essay on the topic of {details['topic']} in a {details['essay_type']} style for a {details['target_audience']} audience."  
    response=generate_response(prompt, temperature=temperature, max_tokens=details['length'])  
    print(f"\nA full draft essay output is {response}")
    
    print("\nWould you like to generate a step-by-step outline for your essay? (yes/no): ")
    choice=input().lower()
    if choice=="yes":
        step_prompt=f"Createa detailed step-by-step outline for an essay on the topic of {details['topic']} providing evidence and reasoning for each argument "
        step_response=generate_response(step_prompt, temperature=temperature, max_tokens=details['length'])
        print(f"\nHere is a step-by-step outline for your essay: {step_response}")
        
        print("Please rate the response ona scale of 1-10 (1 being poor and 10 being excellent): ")
        rating=int(input())
        if rating<1 or rating>10:
            print("Invalid rating")
        elif rating>4 and rating<6: 
            print("Thank you for the feedback")   
        else:
            feedback=input("Please provide feedaback on hoe to improve the response: ")
            improved_prompt=f"Using the feedback: {feedback} imporve the following essay outline{step_response}"
            improved_response=generate_response(improved_prompt, temperature=temperature, max_tokens=details['length'])
            print(f"Here is the improved essay outline: {improved_response}")
                

print("Welcome to the AI writing asssistant")
details=get_essay_details()
if not details["topic"] or not details["essay_type"]:
    print("Please provide at least a topic or essay type to continue.")
else:
    generated_essay(details)
       

