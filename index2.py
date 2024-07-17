piket = {
    "Dea": 77,
    "Ereni": 81,
    "Ela": 75,
    "Trimi": 90,
    "Rita": 100 
        
        
}
key = input("Shkruaj qelsin qe deshironi me kontrollu: ")
if key in piket:
    print(f"Qelesi '{key}' ekziston ne dictonary me vleren {piket}.")
else:
    print(f"Qelesi '{key}' nuk ekziston ne dictonary.")
    total_score = sum(piket.values())
    num_students = len(piket)
    average_score = total_score / num_students
    print(f"Piket mesatare te te gjith nxenesve jane: {average_score:.2f}")