def show_info(**details):
    result = ""
    for key, value in details.items():
        result += f"{key.capitalize()}: {value}\n"
    
    return result


info = show_info(name="Emman", age=69, city="Karachi", occupation="Professional Sleeper")
print(info)

