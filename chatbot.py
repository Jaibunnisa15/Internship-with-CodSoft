import re
from datetime import datetime

def chatbot_response(user_input):
  user_input=user_input.lower()
  
  patterns_responses={
    r'hello|hi|hey':"Hello!",
    r'bye|exit|quit':"Good bye! Have a great day!",
    r'can you help me?':"sure! How can I help you?",
    r'okay|ok':"How can I assist you today?",
    r'what can you do?':"I can chat with you based on predefined rules",
    r'thank you':"Your Wellcome",
    r'weather|temperature':"I'm  not sure about the wether right now,but you can check your local weather forecast online.",
    r'time|clock':f"The current time is {datetime.now().strftime('%H:%M:%S')}.",
    r'date|day':f"The Today's Date is {datetime.now().strftime('%Y:%M:%D')}.",
    r'name|who are you':"I am a simple rule-based chatbot created to assisst you with basic queries.",
    r'language|programming':"I am programmed inpython."
  }    
  for pattern,response in patterns_responses.items():
    if re.search(pattern, user_input):
      return response
  return "I'm sorry, I don't understand that.Can you please rephrase or ask somethig else?"    

#Main function to interact with chatboat
def chat():
  print("Welcome to the simple rule-based chatbot!")
  print("Type 'bye','exit',or'quit' to end the conversation.")
  
  while True:
    user_input=input("You: ")
    if user_input.lower()in["bye","goodbye"]:
      print(f"Chatbot:{chatbot_response(user_input)}")
      break
    else:
      print(f"Chatbot:{chatbot_response(user_input)}")
chat()             