def generate_name_invite(name):
    final_position = len(name)
    initial_positon = final_position - 4
    part_01 = name[0:4]
    part_02 = name[initial_positon:final_position]
    return part_01 + ' ' + part_02

def send_invite(formated_name):
    print 'Sendo invite to %s' % (formated_name)

def process_invite(guest_name):
    formated_name = generate_name_invite(guest_name)
    send_invite(formated_name)