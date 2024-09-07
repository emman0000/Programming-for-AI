import json

def save_to_json_file (file_path , data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data , file)
            print("Data saved to JSON file")
    except IOError:
        print("IOError")



def load_data_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except IOError:
        print("IOError")




def find_age(data):
    try:
        #finding maximum age here
        max_age = max(data.values())
        people_in_order = [name for name , age in data.items() if age == max_age]

        print (f"People that are the oldest: ({max_age}): {' , '.join(people_in_order)}")
        # check for all people and their ages
        for age in set(data.values()):
            same_age_people = [name for name, age_val in data.items() if age_val == age]
            if len(same_age_people) > 1:
                print(f"People with the same age ({age}):{',' .join(same_age_people)}")


    except Exception as e:
        print(e)

#Sample

file_path ='Ages.json'
people_ages = {'Ali': 23, 'Saad': 24, 'Salman': 15, 'Shams': 25, 'Sadiq': 46, 'Hammad': 23}

save_to_json_file(file_path , people_ages)
loaded_Data = load_data_from_json(file_path)

if loaded_Data:
    find_age(loaded_Data)
#enter code
