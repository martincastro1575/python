users_web = ['car79','ela90','admin','sunr23','uier65']

for user in users_web:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a status report?")
    elif user != 'admin':
        print(f"Hello {user}, thank you for logging in again")