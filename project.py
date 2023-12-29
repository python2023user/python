# Проект - Мениджър на Задачи с конзолен интерфейс. Запазва въведената информация до изход от програмата.

tasks = {}
choise = ""
while True:
    if choise == "":
        print("################################\nМениджър на задачи (главно меню)\n################################\n-\n 1 -> Добавяне на задача\n \
2 -> Показване на списък\n 3 -> Промяна на заглавието по индекс\n \
4 -> Пренареждане на задача по индекс\n 5 -> Изтриване на задача\n \
6 -> Автоматично пренареждане на индекси\n 7 -> Изход от програмата\n-")
        choise = ""
        while choise != None:
            choise = input("Въведете индекс от менюто: ").strip(" ")
            if not choise.isnumeric():
                print(f">> Невалидна команда \"{choise}\"")
                continue
            else:
                choise = int(choise)
                if choise not in range(1,8):
                    print(f">> Невалидна команда \"{choise}\"")
                    continue
                else:
                    break
    match choise:
        case 1:
            print("======================\n< ДОБАВЯНЕ НА ЗАДАЧИ >\n======================")
            print("-\n> Натиснете \"Enter\" за връщане към главното меню\n-")
            data = " "
            while data != "":
                if len(tasks) > 0:
                    num = max(tasks.keys())
                else:
                    num = 0
                data = input(f"Въведете задача {num + 1}: ").strip(" ")
                if data == "":
                    choise = None
                    break
                tasks.update({num + 1:data})
        case 2:
            print(f"==============================\n< СПИСЪК СЪС ЗАДАЧИ (общо {len(tasks)}) >\n==============================\n-" )
            if len(tasks) != 0:
                for x in tasks.keys():
                    print(f"Задача \"{x}\" -> {tasks[x]}")
                    retrn = " "
                while retrn != "":
                    print("-\nНатиснете \"Enter\" за връщане към главното меню")
                    retrn = input("").strip(" ")
                    if retrn == "":
                        choise = None
                        break
                    else:
                        print(f">> Невалидна команда \"{retrn}\"!")
                        continue
            else:
                print(">> Списъкът със задачи е празен!")
                retrn = " "
                while retrn != "":
                    print("-\nНатиснете \"Enter\" за връщане към главното меню")
                    retrn = input("").strip(" ")
                    if retrn == "":
                        choise = None
                        break
        case 3:
            inpt = None
            if len(tasks) == 0:
                print("-\n>> Списъкът със задачи е празен!")
                while inpt != "":
                    print("-\n> Натиснете \"Enter\" за връщане към главното меню")
                    inpt = input("").strip(" ")
                    if inpt == "":
                        choise = None
                        break
                    else:
                        print(">> Невалидна команда \"{inpt}\"")
                        continue
            else:
                print("=================================\n< ПРОМЯНА НА ЗАГЛАВИЕ ПО ИНДЕКС >\n=================================")
                print("> Текущи задачи:\n-")
                for x in tasks:
                    print(f"{x} -> {tasks[x]}")
                while inpt != "":
                    print("-\n> Натиснете \"Enter\" за връщане към главното меню")
                    inpt = input(f"> Въведете номер на задача за промяна: ").strip()
                    if inpt.isnumeric() and x != "":
                        inpt = int(inpt)
                        if inpt in tasks.keys():
                            break
                        else:
                            print(f">> Невалиден номер \"{inpt}\"")
                            continue
                    else:
                        print(f">> Невалиден номер \"{inpt}\"")
                        if inpt == "":
                            break
                if inpt == "":
                    choise = None
                    continue
                print(f"> Текуща задача с номер {inpt}: \"{tasks[inpt]}\"")
                newtask = " "
                while newtask != "":
                    newtask = input(f"> Нова задача {inpt}: ").strip(" ")
                    if newtask == "":
                        continue
                    else:
                        tasks[inpt] = newtask
                        print(f"-\n> Задача \"{x}\" е успешно променена на \"{newtask}\"")
                        break
                inpt = None
                while inpt != "":
                    print("-\n> Натиснете \"Enter\" за връщане към главното меню")
                    print("> Въведете \"1\" за промяна на други номера")
                    inpt = input("").strip(" ")
                    if inpt == "":
                        choise = None
                        break
                    if inpt == "1":
                        choise = 3
                        break
                    else:
                        print(f">> Невалидна команда \"{inpt}\"")
                        continue
        case 4:
            if len(tasks) != 0:
                print("====================================\n< ПРЕНАРЕЖДАНЕ НА ЗАДАЧА ПО ИНДЕКС >\n====================================")
                print("> Текущи задачи:\n-")
                for x in tasks:
                    print(f"Задача {x} -> {tasks[x]}")
                change1 = " "
                while change1 != "":
                     print("-\n> Натиснете \"Enter\" за връщане към главното меню")
                     change1 = input("> Въведете първи номер за размяна: ").strip(" ")
                     if change1.isnumeric():
                         change1 = int(change1)
                         if change1 not in tasks.keys() and change1 != "":
                            print(f">> Невалиден номер: \"{change1}\"")
                            continue
                         else:
                             break
                     else:
                        print(f">> Невалиден номер: \"{change1}\"")
                        continue
                if change1 == "":
                    choise = None
                    continue
                change2 = " "
                while change2 != "":
                    print("-\n> Натиснете \"Enter\" за връщане към главното меню")
                    change2 = input(f"> Въведете втори номер за размяна на номер \"{change1}\" ({tasks[change1]}): ").strip(" ")
                    if change2.isnumeric():
                         change2 = int(change2)
                         if change2 not in tasks.keys() and change2 != "":
                            print(f">> Невалиден номер: \"{change2}\"")
                            continue
                         else:
                             break
                    else:
                        print(f">> Невалиден номер: \"{change2}\"")
                        continue
                if change2 == "":
                    print("Връщане към главното меню...")
                    continue
                val1 = tasks[change1]
                val2 = tasks[change2]
                tasks.update({change1:val2})
                tasks.update({change2:val1})
                print(f"-\n>> Успешно разменени стойности на индекс \"{change1}\" ({val1}) с \"{change2}\" ({val2})")
                inpt = None
                while inpt != "":
                    print("-\n> Натиснете \"Enter\" за връщане към главното меню")
                    print("> Въведете \"1\" за промяна на други номера")
                    inpt = input().strip(" ")
                    if inpt != "" and inpt != "1":
                        continue
                    elif inpt != "" and inpt == "1":
                        break
                if inpt == "":
                    choise = None
                    continue
                if inpt == "1":
                    choise = 4
                    continue
            else:
                print("-\n>> Списъкът със задачи е празен!")   
                inpt = None
                while inpt != "":
                    print("-\n> Натиснете \"Enter\" за връщане към главното меню")
                    inpt = input().strip(" ")
                    if inpt != "":
                        continue
                if inpt == "":
                    choise = None
                    continue   
        case 5:
            if len(tasks) != 0:
                print("========================\n< ИЗТРИВАНЕ НА ЗАДАЧА >\n========================")
                print("> Текущи задачи:\n-")
                for x in tasks:
                    print(f"Задача {x} -> {tasks[x]}")
                inpt = None
                while inpt != "":
                    print("-\n> Натиснете \"Enter\" за връщане към главното меню")
                    print("> Въведете \"1\" за изтриване по индекс\n> Въведете \"2\" за изтриване по заглавие")
                    inpt = input("Избор: ").strip(" ")
                    if inpt == "1":
                        avkeys = [k for k in tasks.keys()]
                        key = input(f"Въведете индекс за изтриване {avkeys}: ").strip(" ")
                        if key.isnumeric():
                            key = int(key)
                            keystat = ""
                            for k in tasks:
                                if key == k:
                                    keystat = "detected"
                            if keystat == "detected":
                                delvalue = tasks[key]
                                tasks.pop(key)
                                print(f"-\n>> Задача с индекс \"{key}\" съдържаща заглавие \"{delvalue}\" беше изтрита!")
                                if len(tasks) > 0:
                                    print("-\n> Въведете \"1\" за изтриване на други задачи")
                                else:
                                    print("-\n>> Списъкът със задачи е празен!")
                                print("> Натиснете \"Enter\" за връщане към главното меню")
                                inpt = input().strip(" ")
                                if inpt == "":
                                    choise = None
                                    break
                                elif inpt == "1" and len(tasks) > 0:
                                    choise = 5
                                    break
                                else:
                                    print(f">> Невалидна команда \"{inpt}\"")
                            if keystat == "":
                                print(f"-\n>> Задача с индекс {key} не е намерена!")
                                print("-\n> Натиснете \"Enter\" за връщане към главното меню")
                                print("> Въведете \"1\" за изтриване на други задачи")
                                inpt = input("").strip(" ")
                                if inpt == "":
                                    choise = None
                                    break
                                elif inpt == "1" and len(tasks) > 0:
                                    choise = 5
                                    break
                                elif inpt == "2" and len(tasks) > 0:
                                    choise = 5
                                    break
                                else:
                                    print(f"-\n>> Невалидна команда \"{inpt}\"")
                                    choise = 5
                                    continue
                        else:
                            print(f"-\n>> Невалидна команда \"{key}\"")
                            choise = 5
                            continue
                    elif inpt == "2":
                        title = input(f"Въведете заглавие за изтриване: ").strip(" ")
                        titlestats = ""
                        delkey = []
                        for key, val in tasks.items():
                            if title == val:
                                delkey.append(key)
                                titlestats = "detected"
                        if titlestats == "detected":
                            for d in delkey:
                                print(f">> Задача с индекс \"{d}\" съдържаща \"{title}\" беше изтрита!")
                                tasks.pop(d)
                            if len(tasks) > 0:
                                print("-\n> Въведете \"1\" за изтриване на други задачи")
                            else:
                                print("-\n>> Списъкът със задачи е рпазен!")
                            print("-\n> Натиснете \"Enter\" за връщане към главното меню")
                            inpt = input().strip(" ")
                            if inpt == "":
                                choise = None
                                break
                            elif inpt == "1" and len(tasks) > 0:
                                choise = 5
                                break
                            else:
                                print(f">> Невалидна команда \"{inpt}\"")
                        elif titlestats == "":
                            print(f"-\n>> Задача със заглавие \"{title}\" не е намерена!")
                            print("-\n> Натиснете \"Enter\" за връщане към главното меню")
                            print("> Въведете \"1\" за изтриване на други задачи")
                            inpt = input("").strip(" ")
                            if inpt == "":
                                choise = None
                                break
                            elif inpt == "1" and len(tasks) > 0:
                                choise = 5
                                break
                            elif inpt == "2" and len(tasks) > 0:
                                choise = 5
                                break
                            else:
                                print(f"-\n>> Невалидна команда \"{inpt}\"")
                                choise = 5
                                continue
                    elif inpt != "1" and inpt != "2":
                        print(f"-\n>> Невалидна команда \"{inpt}\"")
                        choise = 5
                        continue
                if inpt == "":
                    choise = None
                    continue   
            else:
                print("-\n>> Списъкът със задачи е празен!")
                print("-\n> Натиснете \"Enter\" за връщане към главното меню") 
                inpt = None
                while inpt != "":
                    inpt = input().strip(" ")
                    if inpt == "":
                        choise = None
                        continue
                    else:
                        print(f">> Невалидна команда \"{inpt}\"")
                        choise = 5
                        continue
        case 6:
            print("=======================================\n< АВТОМАТИЧНО ПРЕНАРЕЖДАНЕ НА ИНДЕКСИ >\n=======================================")
            if len(tasks) > 0:
                temptasks = {}
                tnum = 1
                for index in tasks:
                    temptasks.update({tnum:tasks[index]})
                    tnum += 1
                tasks = temptasks
                print("-\n> Индексите са пренаредени!\n> Показване на резултатите...\n-") 
                for x in tasks.keys():
                    print(f"Задача \"{x}\" -> {tasks[x]}")
            else: 
                print("-\n>> Списъкът със задачи е празен!")
            inpt = None
            print("-\n> Натиснете \"Enter\" за връщане към главното меню") 
            while inpt != "":
                inpt = input().strip(" ")
                if inpt == "":
                    choise = None
                    continue
                else:
                    print(f">> Невалидна команда \"{inpt}\"")
                    choise = 6
                    continue
        case 7:
            print("Изход от програмата...")
            break
                            
        case _:
           choise = ""
           continue
                    

    