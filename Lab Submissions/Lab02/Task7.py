def average(temp_list):
    total_sum = sum(temp_list) 
   
    avg_temp = ( total_sum / len(temp_list))
     
     print("Average temperature over the span of 30 days is:", avg_temp)
  
    sorted_temps = sorted(temp_list) print("Sorted temperatures:", sorted_temps)
    max_temp = max(temp_list) print("Maximum Temperature:", max_temp) 
    min_temp = min(temp_list) print("Minimum Temperature:", min_temp) 
    
    # List of temperatures over 30 days
    temp_list = [12, 15, 33, 45, 22, 12, 15, 15, 17, 20, 12, 15, 33, 45, 22, 12, 15, 15, 17, 20, 12, 15, 33, 45, 22, 12, 15, 15, 17, 20] 


    average(temp_list)  
