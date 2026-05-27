from hf import generate_response

print("Zero shot, One shot, Few shot learning activity")
category = input("Please select a category (eg.food, animals, etc): ")
item = input("Please select an item in that category (eg. pizza, dog, etc.): ")
if not category or not item:
    print("Please enter category and item to continue")
else:    
    zero_shot_prompt = f"Is {item} a {category}? "
    zero_shot_response=generate_response(zero_shot_prompt, temperature=0.8, max_tokens=512)
    print(f"Zero shot response: {zero_shot_response}")
    
    one_shot_prompt=f"""For example:
    Category: Food
    Item: Pizza
    Answer: Yes, pizza is a food item.
    
    Now you try: 
    Category: {category}
    Item: {item}
    Answer: """
    one_shot_response=generate_response(one_shot_prompt, temperature=0.8, max_tokens=512)
    print(f"One shot response: {one_shot_response}")
    
    few_shot_prompt=f"""For example:
    Category: Food
    Item:Pizza
    Answer: Yes, pizza ia a food item 
    Category: Animal
    Item: Dog
    Answer: Yes, dogs are animals that are often kept as pets
    
    Now you try:
    Category: {category}
    Item: {item}
    Answer: """
    few_shot_response=generate_response(few_shot_prompt, temperature=0.9, max_tokens=512) 
    print(f"Few shot response: {few_shot_response}")
       
    
    
    
    
    
    
    

