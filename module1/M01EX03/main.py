from coding_exercise import ex1, ex2, ex3, ex4


def main():
    while True:
        exercise_number = 'ex' + \
            input('Please input exercise number(1-4) or anything else to exit: \n>> ')
        if exercise_number in globals():
            globals()[exercise_number]()
        else:
            print("Exit...")
            return
        print('-' * 25)


if __name__ == '__main__':
    main()
