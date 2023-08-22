from .exceptions import OutOfBoundException
def display_menu_prompt(title: str, options: list, question: str):
    print("===============================================================")
    print(title)
    index = 0
    for option in options:
        print(f'{index+1}. {option}')
        index+=1
    print()
    answer = int(str(input(question)).strip())-1
    if (answer <= 0 or answer > len(options)):
        raise OutOfBoundException('Invalid option selected!')
    return answer
    