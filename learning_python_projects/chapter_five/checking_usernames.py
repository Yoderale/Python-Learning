current_users = [
    'yoderale', 'yodi', 'kysaa',
    'admin', 'SAAKY', 'kyodi'
    ]

new_users = [
    'yods', 'YODERALE', 'saaky', 
    'patrick', 'kyodi', 'spongebob'      
]

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Please pick another username! This one is taken.")
    else: print(f"Congratulations, {new_user.title()}! You made your account successfully!")