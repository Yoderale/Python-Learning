username = [
    'yoderale', 'yodi', 'kysaa',
    'admin', 'saaky', 'kyodi'
]
for user in username:
    if user == 'admin':
        print(f"Hello Admin, would you like to view the most recent report.")
    else: print(f"Hello {user.title()}, Welcome back!")