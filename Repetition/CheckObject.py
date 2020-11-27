def grade(b,cell,t):
    wrongExercises = []
    if 'Sadly you' in cell.stdout:
        wrongExercises.append(1)
        
    if not ('MewtwoMega Mewtwo X' in cell.stdout and '190' in cell.stdout):
        wrongExercises.append(2)
        
    if not ('Ekans' in cell.stdout and 'Dragalge' in cell.stdout):
        wrongExercises.append(3)
        
    if not ('\nSteelixMega Steelix\n' in cell.stdout):
        wrongExercises.append(4)

    if (len(wrongExercises))>0:
        b.button_style = 'Danger'
    else:
        b.button_style = 'Success'
    t.value = ''
    if (len(wrongExercises) == 1):
        t.value = f'Exercise {wrongExercises[0]} is wrong'
    else:
        t.value = f'Exercises {",".join(str (x) for x in wrongExercises)} are wrong.'