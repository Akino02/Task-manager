#Vytvorte tridu tank, ktera bude mit atributy pro nazev ukolu, proritu a stav (napr zadano, hotovo)
#ve tride vytvorte funkce pro vypis informaci o úkolu (dunder metoda str), zmena stavu projektu a zmenu priority
#vytvorte kolekci, ve ktere se budeou ukladat vytvorene ukoly
#vytvorte uzivatelske rozhrani (nekonecny cyklus s nabidkou)
#uzivatel bude moct vybrat z moznosti vytvorit ukol, upravit ukol, vypsat seznam ukolu
#vytvorte funkce pro jednotlive moznosti, ktere uzivatel muze vybrat a zajistete celkovou funkcnost projektu

import os

is_running = True

task_collection = []

user_menu = ["Create Task", "Change Task", "Print Tasks", "Close this app"]
priority_names = ["Not important", "Medium", "IMPORTANT"]
status_names = ["Plan", "Working", "Done"]

user_want_change = ["Change name", "Change priority", "Change status"]

def Create_task():
    task_name = input("Enter task name: ")
    priority = int(input("Enter priority of task: "))
    status = int(input("Enter status of task: "))
    task_name = Task(task_name, priority_names[priority-1], status_names[status-1])

    task_collection.append(task_name)
    print(task_name)

def Change_task_atributs():
    Print_tasks()

    change_task_input = int(input("Enter task number: "))
    change_task_input_index = change_task_input-1

    for a in range(len(user_want_change)):
        print(f"{a+1})", user_want_change[a])

    user_change = int(input())
    if user_change == 1:
        atribute_change = input("Enter new task name: ")
        task_collection[change_task_input_index].Change_name(atribute_change)
    elif user_change == 2:
        atribute_change = int(input("Enter new task priority: "))
        task_collection[change_task_input_index].Change_priority(priority_names[atribute_change-1])
    elif user_change == 3:
        atribute_change = int(input("Enter new task status: "))
        task_collection[change_task_input_index].Change_status(status_names[atribute_change-1])
    print(task_collection[change_task_input_index])

def Print_tasks():
    for a in range(len(task_collection)):
        print(f"{a+1}]{task_collection[a]}")

class Task():
    def __init__(self, task_name, priority, status):
        self.task_name = task_name
        self.priority = priority
        self.status = status
    
    def Change_name(self, user_name):
        self.task_name = user_name
        self.__str__()

    def Change_status(self, user_status):
        self.status = user_status
        self.__str__()
    
    def Change_priority(self, user_priority):
        self.priority = user_priority
        self.__str__()

    def __str__(self):
        return f"Task: {self.task_name}, priority: {self.priority}, status: {self.status}"

task_one = Task("Tank game", 2, "Working")
task_two = Task("MVC", 1, "Plan")
task_three = Task("Kill someone", 1, "Done")

task_collection.append(task_one)
task_collection.append(task_two)
task_collection.append(task_three)

while is_running:
    for a in range(len(user_menu)):
        print(f"{a+1})", user_menu[a])
    
    user_pick = int(input())

    os.system("cls")

    if user_pick == 1:
        Create_task()
    elif user_pick == 2:
        Change_task_atributs()
    elif user_pick == 3:
        Print_tasks()
    elif user_pick == 4:
        is_running = False
    else:
        print("NOT VALID MY MAN")
    
    print("------------------")