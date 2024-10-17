#Vytvorte tridu tank, ktera bude mit atributy pro nazev ukolu, proritu a stav (napr zadano, hotovo)
#ve tride vytvorte funkce pro vypis informaci o úkolu (dunder metoda str), zmena stavu projektu a zmenu priority
#vytvorte kolekci, ve ktere se budeou ukladat vytvorene ukoly
#vytvorte uzivatelske rozhrani (nekonecny cyklus s nabidkou)
#uzivatel bude moct vybrat z moznosti vytvorit ukol, upravit ukol, vypsat seznam ukolu
#vytvorte funkce pro jednotlive moznosti, ktere uzivatel muze vybrat a zajistete celkovou funkcnost projektu

import os
import sqlite3

con = sqlite3.connect("tutorial.db")

cur = con.cursor()

try:
    cur.execute(
        """CREATE TABLE task
        (id INTEGER PRIMARY KEY,task_name VARCHAR(32), priority VARCHAR(32), status VARCHAR(32))"""
        )
except:
    pass

#cur.execute("""
#    INSERT INTO task VALUES
#        ('Tank game', 'IMPORTANT', 'Working'),
#        ('MVC', 'Medium', 'Done')
#""")
# con.commit()
# res = cur.execute("SELECT * FROM task")
# print(res.fetchall())

# task_one = Task("Tank game", 2, "Working")
# task_two = Task("MVC", 1, "Plan")
# task_three = Task("Kill someone", 1, "Done")


is_running = True

task_collection = []

user_menu = ["Create Task", "Change Task", "Print Tasks", "Close this app"]

priority_names = ["Not important", "Medium", "IMPORTANT"]
status_names = ["Plan", "Working", "Done"]

task_modifications = ["Change name", "Change priority", "Change status"]

class Task():
    def __init__(self, task_name: str, priority: str, status: str):
        self.task_name = task_name
        self.priority = priority
        self.status = status
    
    def Change_name(self, user_name):
        self.task_name = user_name
        self.__str__()

    def Change_status(self, status_index: int):
        self.status = status_names[status_index]
        self.__str__()
    
    def Change_priority(self, priority_index: int):
        self.priority = priority_names[priority_index]
        self.__str__()

    def __str__(self):
        return f"Task: {self.task_name}, priority: {self.priority}, status: {self.status}"

def try_int_input(prompt: str = "Enter number: "):
    try:
        return int(input(prompt))
    except:
        return try_int_input("Try again: ")

def Load_data():
    # for a in cur.execute("SELECT * FROM task"):
    #     tasks.append(a)

    # res = cur.execute("SELECT * FROM task")
    # tasks = res.fetchall()

    tasks = {}
    for row in cur.execute("SELECT * FROM task"):
        tasks[row[0]] = Task(row[1], row[2], row[3])

    return tasks

def Create_task():
    task_name = input("Enter task name: ")
    priority = try_int_input("Enter priority of task: ")
    status = try_int_input("Enter status of task: ")

    # TODO: list                       opravit kys injection
    cur.execute(f" INSERT INTO task (task_name, priority, status) VALUES ('{task_name}', '{priority_names[priority-1]}', '{status_names[status-1]}') ")
    con.commit()
    
    # task_name = Task(task_name, priority_names[priority-1], status_names[status-1])

    # task_collection.append(task_name)
    # print(task_name)


# UDĚLAT UPRAVOVANI TASKU S TIM, ZE SE BUDOU UPRAVOVAT DO DATABAZE
def Change_task_atributs():
    Print_tasks()

    tasks = Load_data()

    task_id = try_int_input("Enter task number: ")

    if task_id not in tasks.keys():
        return

    for count, modification in enumerate(task_modifications):
        print(f"{count+1}) {modification}")
    
    chosen_modification = try_int_input("Enter atribute to be changed: ")

    task = tasks[task_id]

    # modifications = [task.Change_name, task.Change_status, task.Change_priority]

    # change_atribute = modifications[chosen_modification-1]
    collums = ("task_name", "priority", "status")

    if chosen_modification == 1:
        new_name = input("Enter new task name: ")
        # change_atribute(new_name)
        cur.execute(f" UPDATE task SET {collums[chosen_modification-1]} = '{new_name}' WHERE id = {task_id} ")
        con.commit()
    
    elif chosen_modification == 2:
        new_atribute_number = try_int_input("Enter new priority value: ")
        # change_atribute(new_atribute_number-1)
        cur.execute(f" UPDATE task SET {collums[chosen_modification-1]} = '{priority_names[new_atribute_number-1]}' WHERE id = {task_id} ")
        con.commit()

    elif chosen_modification == 3:
        new_atribute_number = try_int_input("Enter new status value: ")
        # change_atribute(new_atribute_number-1)
        cur.execute(f" UPDATE task SET {collums[chosen_modification-1]} = '{status_names[new_atribute_number-1]}' WHERE id = {task_id} ")
        con.commit()
    else:
        return

    # if user_change == 1:
    #     # atribute_change = input("Enter new task name: ")
    #     # task_collection[change_task_input_index].Change_name(atribute_change)
    #     pick_data[change_task_input-1][user_change-1] = "ahoj"

    # elif user_change == 2:
    #     atribute_change = int(input("Enter new task priority: "))
    #     task_collection[change_task_input_index].Change_priority(priority_names[atribute_change-1])
    # elif user_change == 3:
    #     atribute_change = int(input("Enter new task status: "))
    #     task_collection[change_task_input_index].Change_status(status_names[atribute_change-1])
    
    # print(pick_data[change_task_input-1])
    # print(task_collection[change_task_input_index])

def Print_tasks():
    tasks = Load_data()
    # index = 1
    # for a in cur.execute("SELECT * FROM task"):
    #     print(f"{index}]", end=" ")
    #     for b in a:
    #         print(b, end=", ")
    #     print(" ")
    #     index+=1

    # for a in range(len(task_collection)):
    #     print(f"{a+1}]{task_collection[a]}")

    for id, task in tasks.items():
        print(f"{id}] {task}")

# task_one = Task("Tank game", 2, "Working")
# task_two = Task("MVC", 1, "Plan")
# task_three = Task("Kill someone", 1, "Done")

# task_collection.append(task_one)
# task_collection.append(task_two)
# task_collection.append(task_three)

while is_running:
    for a in range(len(user_menu)):
        print(f"{a+1})", user_menu[a])
    
    user_pick = try_int_input()

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