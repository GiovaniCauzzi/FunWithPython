
from ImageLoading import OpenImage
from menu import clearConsole, freezeExecution, printPressEnter2Continue, printMenu


option = 0
while option != 10:
    clearConsole()
    printMenu()
    option = input()

    match option:
        case "1":
            clearConsole()
            print("Escreva o caminho relativo para a imagem e pressione ENTER")
            imagem = OpenImage(input())
            pass


        case "10": # EXIT
            option = 10
            clearConsole()
            pass


        case other:
            clearConsole()
            print("Input nao identificado...")
            freezeExecution()
            pass



