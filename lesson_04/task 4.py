is_moving = input('is it moving?')
should_move = input('should it move?')
if is_moving == 'yes' and should_move == 'no':
    print('use glue')
elif is_moving == 'no' and should_move == 'yes':
    print('use oil')
else:
    print("dont touch")
