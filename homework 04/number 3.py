for num in range(0, 101, 1):
    print(num)
    answer = input('Should we break?')
    while True:
        if answer == 'yes':
            break
        elif answer == 'no':
            continue
    print("Don't understand you")
    answer = input('Should we break?')


