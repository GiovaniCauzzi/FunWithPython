import os

def clearConsole():
    os.system('cls')

def freezeExecution():
    printPressEnter2Continue()
    return input()

def printPressEnter2Continue():
    print("\nPressione ENTER para continuar")
    

def printMenu():
    print("SELECIONE UMA AÇÃO!\n")
    print("1.  Importar imagem")
    print("2.  Salvar imagem")
    print("10. Exit")
    print("\nDigite uma opção e pressione enter!")
