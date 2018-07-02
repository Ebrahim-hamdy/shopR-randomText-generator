def typesFinder():
    genFile = r'writeRandom.txt'

    try:
        openFile = open(genFile, 'r')
        randTypes = openFile.read()
        typesList = randTypes.split(',')

        for typ in typesList:
            if typ.__contains__(' '):
                # case alphanumeric
                print(typ.strip() + ' - alphanumeric')
            elif typ.__contains__('.'):
                # case float
                print(typ + ' - real numbers')
            elif typ.isdigit():
                # case integer
                print(typ + ' - integer')
            elif typ.isalpha():
                # case strings
                print(typ + ' - alphabetical strings')

    except:
        print("Make sure the file exists")

typesFinder()