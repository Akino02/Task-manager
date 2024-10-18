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

is_running = True

task_collection = []

user_menu = ["Create Task", "Change Task", "Delete Task" , "Print Tasks", "Close this app"]

priority_names = ["Not important", "Medium", "IMPORTANT"]
status_names = ["Plan", "Working", "Done"]

task_modifications = ["Change name", "Change priority", "Change status"]
task_deletation_approve = ["Yes", "No"]

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

def load_data():
    tasks = {}
    for row in cur.execute("SELECT * FROM task"):
        tasks[row[0]] = Task(row[1], row[2], row[3])

    return tasks

def create_task():
    data = []
    task_name = input("Enter task name: ")
    data.append(task_name)
    priority = try_int_input(f"Enter priority of task ({priority_names[0]} 0-{len(priority_names)-1} {priority_names[len(priority_names)-1]}): ")
    data.append(priority_names[priority])
    status = try_int_input(f"Enter status of task ({status_names[0]} 0-{len(status_names)-1} {status_names[len(status_names)-1]}): ")
    data.append(status_names[status])

    sql = f" INSERT INTO task (task_name, priority, status) VALUES (?, ?, ?) "

    cur.execute(sql, data)
    con.commit()

def change_task_atributs():
    print_tasks()

    tasks = load_data()

    task_id = try_int_input("Enter task number: ")

    if task_id not in tasks.keys():
        return

    for count, modification in enumerate(task_modifications):
        print(f"{count+1}) {modification}")
    
    chosen_modification = try_int_input("Enter atribute to be changed: ")

    # task = tasks[task_id]

    collums = ("task_name", "priority", "status")

    data = []
    if chosen_modification == 1:
        new_name = input("Enter new task name: ")
        data.append(new_name)
        # change_atribute(new_name)
        sql = f" UPDATE task SET {collums[chosen_modification-1]} = ? WHERE id = {task_id} "
        cur.execute(sql, data)
        # con.commit()
    
    elif chosen_modification == 2:
        new_atribute_number = try_int_input(f"Enter new priority value ({priority_names[0]} 0-{len(priority_names)-1} {priority_names[len(priority_names)-1]}): ")
        # change_atribute(new_atribute_number-1)
        data.append(priority_names[new_atribute_number])
        sql = f"UPDATE task SET {collums[chosen_modification-1]} = ? WHERE id = {task_id} "
        cur.execute(sql, data)
        # con.commit()

    elif chosen_modification == 3:
        new_atribute_number = try_int_input(f"Enter new status value ({status_names[0]} 0-{len(status_names)-1} {status_names[len(status_names)-1]}): ")
        # change_atribute(new_atribute_number-1)
        data.append(status_names[new_atribute_number])
        sql = f" UPDATE task SET {collums[chosen_modification-1]} = ? WHERE id = {task_id} "
        cur.execute(sql, data)
        # con.commit()
    else:
        return
    con.commit()

def detele_task():
    print_tasks()

    tasks = load_data()

    task_id = try_int_input("Enter task number: ")

    if task_id not in tasks.keys():
        return
    
    print("Are you really sure that you want to delete your task ?")
    for count, answear in enumerate(task_deletation_approve):
        print(f"{count+1}) {answear}")
    
    chosen_answear = try_int_input()

    if chosen_answear == 1:
        cur.execute(f"DELETE FROM task WHERE id = {task_id}")
        con.commit()
        print("Task deleted :))")
    else:
        return


def print_tasks():
    tasks = load_data()

    for id, task in tasks.items():
        print(f"{id}] {task}")

while is_running:
    for a in range(len(user_menu)):
        print(f"{a+1})", user_menu[a])
    
    user_pick = try_int_input()

    os.system("cls")

    if user_pick == 1:
        create_task()
    elif user_pick == 2:
        change_task_atributs()
    elif user_pick == 3:
        detele_task()
    elif user_pick == 4:
        print_tasks()
    elif user_pick == 5:
        is_running = False
    else:
        print("NOT VALID MY MAN")
    
    print("------------------")