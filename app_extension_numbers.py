phonebook_dict = {
  'David': '281-456-1234',
  'Adam': '456-123-1234',
  'Karen': '678-893-1234'
}

print(phonebook_dict['Karen'])

phonebook_dict['Larry'] = '938-489-1234'

del phonebook_dict['David']

phonebook_dict['Adam'] = '968-345-2345'

print(phonebook_dict)