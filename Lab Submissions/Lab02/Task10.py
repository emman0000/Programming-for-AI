#Emman 23k0051


def build_message(**info):
  message = [] 

  for key, value in info.items():
      message.append(f"{key}: {value}")  

  message = ", ".join(message) 

  return message  


print(build_message(name="Emman", age=27, city="Karachi"))

  
