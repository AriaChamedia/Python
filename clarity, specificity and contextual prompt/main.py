from groq import generate_response

print("Welcome to the AI Prompt Engineering Tutorial!")
vague = input("Enter a vague prompt: ")
print("\nAI's response to vague prompt:")
print(generate_response(vague))

specific = input("Now make it more specific: ")
print("\nAI's response to specific prompt:")
print(generate_response(specific))

contextual = input("Finally, make it contextual: ")
print("\nAI's response to contextual prompt:")
print(generate_response(contextual))