from hf import generate_response 

print("Part 1: Temperature Exporation")
base=input("Enter a prompt: ")
print("0.1: Low temperature, Deterministic output ")
print("0.5: Medium temperature, balanced output")
print("0.9: High temperature, Creative output")
temperature=float(input("Enter a temperature (0.1, 0.5, 0.9): "))
response= generate_response(base, temperature=temperature,max_tokens=512)
print(f"The response for {temperature} is: {response}")

print("Part 2: Instruction based prompt" )
topic= input("Enter a topic: ")
prompt=[f"Write a detailed article about {topic} with an introduction, main body and       conclusion. Consider this topic as a grade 9 student more focused on the IGSCE curriculum. Use simple language and provide examples where neccersary."]
for i,p in enumerate(prompt, 1):
    print(f"Instruction {i}: {p}")
    response=generate_response(p, temperature=0.5, max_tokens=512)
    print(f"Response {i}: {response}")


