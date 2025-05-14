# Microservice A

# How to request
  To request my microservice to sort/filter provided data, a list containing '0', '1', '2', '3', or '4' must be added to the 0 index of the provided data.
  This lets the microservice know what actions to complete and what to return.

  # Example call
    leaderboard.insert(0, [user_input])
  
    with open('leaderboard.json', 'w') as f:
        json.dump(leaderboard, f, ensure_ascii=False, indent=2)
  
# How to receive 
  To receive data from my microservice, you must first check if the JSON file contains information. Then you need to load the data from the JSON file and check if to see if the 0 index is 'Name', if it is, then the microservice has sent the data.

  # example call
    while True:
      if os.path.getsize('leaderboard.json') > 0:
          time.sleep(1)
          with open('leaderboard.json', 'r') as f:
              data = json.load(f)
              if data[0][0] == 'Name':
                  break

![image](https://github.com/user-attachments/assets/2262f318-3f8d-41e8-b0e1-5a94edbf82cf)
