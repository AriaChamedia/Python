from hf import generate_response

def bias_mitigation():
    print("Bias Mitigation")
    prompt=input("Enter prompt to check for bias (eg. Describe an ideal doctor): ")
    response=generate_response(prompt)
    print("response:", response)
    bias=input("Do you feel that the prompt is biased? (yes/no): ")
    if bias.lower()=="yes":
        modified_prompt=input("Enter modified prompt to mitigate bias: ")
        modified_response=generate_response(modified_prompt)
        print("Modified response:", modified_response)
    
def token_limits(): 
    print("Token Limits ")  
    prompt=input("Enter a long prompt (eg. a detailed story more than 300 words): ") 
    if len(prompt)>300:
        print("Prompt exceeds token limit")
        prompt=prompt[:300]
    response=generate_response(prompt)
    print("Response:", response)

print("AI Learning Activity")
print("1) Bias mitigation")
print("2) Token Limits")
choice=int(input("Choose 1 or 2: "))
if choice==1:
    bias_mitigation()
elif choice==2:
    token_limits()    
    