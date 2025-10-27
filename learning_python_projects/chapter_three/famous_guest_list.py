'''3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.'''
famous_guest_list = ['jon snow', 'the rock johnson', 'bilbo baggins', 'starsky hutchenson']
message_line_one = 'You are invited to dinner!'
message_line_two = 'Let me know if you can attend!'
signature = '- Thanks, Alex.'
print(famous_guest_list)
print(f'Dear \n{famous_guest_list[0].title()}, \n{message_line_one} \n{message_line_two} \n\t\t {signature} ')
print(f'Dear \n{famous_guest_list[1].title()}, \n{message_line_one} \n{message_line_two} \n\t\t {signature} ')
print(f'Dear \n{famous_guest_list[2].title()}, \n{message_line_one} \n{message_line_two} \n\t\t {signature} ')
print(f'Dear \n{famous_guest_list[-1].title()}, \n{message_line_one} \n{message_line_two} \n\t\t {signature} ')

'''3-5. Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print() call at the end of
your program, stating the name of the guest who can’t make it.
• Modify your list, replacing the name of the guest who can’t make it with the
name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still in
your list.'''

#Remove guest, and add Harry Potter
removed_guest = famous_guest_list.pop(-1)
print(f"{removed_guest.title()} unfortunately can't attend the dinner.")
famous_guest_list.append('harry potter'.title())
backup_guest = famous_guest_list[-1]
print(f'{backup_guest} was invited in place of {removed_guest.title()}. Now our dinner party is guest list is complete.')

# New Guest List
print(famous_guest_list)
print(f'Dear \n{famous_guest_list[0].title()}, \n{message_line_one} \n{message_line_two} \n\t\t {signature} ')
print(f'Dear \n{famous_guest_list[1].title()}, \n{message_line_one} \n{message_line_two} \n\t\t {signature} ')
print(f'Dear \n{famous_guest_list[2].title()}, \n{message_line_one} \n{message_line_two} \n\t\t {signature} ')
print(f'Dear \n{famous_guest_list[-1].title()}, \n{message_line_one} \n{message_line_two} \n\t\t {signature} ')

'''3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
end of your program, informing people that you found a bigger table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.'''

print('Great news, we got a larger table.')
guest_count = len(famous_guest_list)
print(guest_count)
famous_guest_list.insert(0,'hermione granger'.title())
guest_count = len(famous_guest_list)
print(guest_count)
famous_guest_list.insert(4,'ron weasley'.title())
famous_guest_list.append('severus snape'.title())
guest_count = len(famous_guest_list)
print(guest_count)
print(famous_guest_list)

print(f'Dear \n{famous_guest_list[0].title()}, \n{message_line_one} \n{message_line_two} \n\t\t {signature} ')
print(f'Dear \n{famous_guest_list[1].title()}, \n{message_line_one} \n{message_line_two} \n\t\t {signature} ')
print(f'Dear \n{famous_guest_list[2].title()}, \n{message_line_one} \n{message_line_two} \n\t\t {signature} ')
print(f'Dear \n{famous_guest_list[3].title()}, \n{message_line_one} \n{message_line_two} \n\t\t {signature} ')
print(f'Dear \n{famous_guest_list[4].title()}, \n{message_line_one} \n{message_line_two} \n\t\t {signature} ')
print(f'Dear \n{famous_guest_list[5].title()}, \n{message_line_one} \n{message_line_two} \n\t\t {signature} ')
print(f'Dear \n{famous_guest_list[6].title()}, \n{message_line_one} \n{message_line_two} \n\t\t {signature} ')

print(f'As it turns out, only two guests can now attend this marvelous dinner.')

removed_guest = famous_guest_list.pop()
print(f'Unfortunately, for you {removed_guest.title()}, there is no longer enough room at our table for you.\nYou are uninvited.')

removed_guest = famous_guest_list.pop()
print(f'Unfortunately, for you {removed_guest.title()}, there is no longer enough room at our table for you.\nYou are uninvited.')

removed_guest = famous_guest_list.pop()
print(f'Unfortunately, for you {removed_guest.title()}, there is no longer enough room at our table for you.\nYou are uninvited.')

removed_guest = famous_guest_list.pop()
print(f'Unfortunately, for you {removed_guest.title()}, there is no longer enough room at our table for you.\nYou are uninvited.')

removed_guest = famous_guest_list.pop()
print(f'Unfortunately, for you {removed_guest.title()}, there is no longer enough room at our table for you.\nYou are uninvited.')

print(f'Fortunately for {famous_guest_list[0].title()}, there IS room for you at my dinner party still!')
print(f'Fortunately for {famous_guest_list[1].title()}, there IS room for you at my dinner party still!')
print(f'This is how many guests are invited to my party {len(famous_guest_list)}.')
del famous_guest_list[1]
del famous_guest_list[0]

print(famous_guest_list)
print(len(famous_guest_list))