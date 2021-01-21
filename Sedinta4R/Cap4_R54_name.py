def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name"""
    if middle_name:
        full_name = first_name + ' ' +  middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
    
musician = get_formatted_name('Paul', 'Ionescu')
print(musician)

musician = get_formatted_name('George', 'Constantin', 'L.')
print(musician)

def get_fname_lname(fullname):
    """Return a full name"""
    if len(fullname.split()) == 3:
        first_name =  fullname.split()[0]
        last_name = fullname.split()[2]
        middle_name = fullname.split()[1]
    elif len(fullname.split()) == 2:
        first_name = fullname.split()[0]
        last_name = fullname.split()[1]
        middle_name = ''
    else:
        print('error name')
    print( """First name: {0} 
Last name: {1} 
Middle name: {2}""".format(first_name.title(),last_name.title(),middle_name.title()))

get_fname_lname(musician)

def gfl(fullname):
    """Return a full name"""
    if len(fullname.split()) == 3:
        first_name =  fullname.split()[0]
        last_name = fullname.split()[2]
        middle_name = fullname.split()[1]
    elif len(fullname.split()) == 2:
        first_name = fullname.split()[0]
        last_name = fullname.split()[1]
        middle_name = ''
    else:
        print('error name')
    print( 'First name: {0}'.format(first_name.title()) +\
           '\nLast name: {0}'.format(last_name.title()) +\
           '\nMiddle name: {0}'.format(middle_name.title()))

get_fname_lname('vasile vasile')

gfl('vasile vasile')