
#task 3 
def convert_URL():
    user_url=input("Enter a URL link that starts with 'https://www.' = ")
    
    link = user_url.split("https://www.")
    if len(link)>1:
     user_url = link.pop()
     converted_url = user_url + ".com"
     return converted_url
    else:
       return "Invalid URL link!"
       
result = convert_URL()
print("Converted URL: "+result)

