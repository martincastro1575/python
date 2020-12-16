current_users = ['car79','ela90','admin','sunr23','uier65']
new_users = ['perez34','mari89','marj35','Ela90','ADMIN']

if new_users:
    for user in new_users:
        if user.lower() in current_users:
            print(f"The username: {user} is not available!")
        elif user.lower() not in current_users:
            print(f"The username: {user} is available")
else:
    print("We need more users!!!")

