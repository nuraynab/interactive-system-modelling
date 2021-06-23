def read_Maude_file():
    f = open("Maude-2/proj/cifma-2020-2.maude", "r")
    list_of_lines = f.readlines()
    f.close()
    return list_of_lines


def write_to_Maude_file(list_of_lines):
    f = open("Maude-2/proj/cifma-2020-2.maude", "w")
    f.writelines(list_of_lines)
    f.close()


def find_line(list_of_lines, look_up):
    for i, line in enumerate(list_of_lines, 1):
        if look_up in line:
            break
    return i


def write_stm_capacity_to_Maude(list_of_lines, stm_capacity):
    look_up = "op stmCapacity : -> Nat ."
    i = find_line(list_of_lines, look_up)
    addition = "   eq stmCapacity = " + stm_capacity + " .\n"
    list_of_lines[i] = addition
    write_to_Maude_file(list_of_lines)


def write_cognitive_load_to_Maude(list_of_lines, cogn_load):
    look_up = "eq theHuman = < human : Human | cognitiveLoad"
    i = find_line(list_of_lines, look_up)
    addition = "  eq theHuman = < human : Human | cognitiveLoad : " + cogn_load + ",\n"
    list_of_lines[i - 1] = addition
    write_to_Maude_file(list_of_lines)


def write_decay_time_to_Maude(list_of_lines, decay_time):
    look_up = "ops DECAY-TIME MAX-RETRIEVAL-TIME : -> TimeInf ."
    i = find_line(list_of_lines, look_up)
    addition = "   eq DECAY-TIME = " + decay_time + " .\n"
    list_of_lines[i] = addition
    write_to_Maude_file(list_of_lines)


def write_rewrite_steps_to_Maude(list_of_lines, rewrite_steps, in_time):
    look_up = "quit"
    i = find_line(list_of_lines, look_up)
    addition = "(trew [" + rewrite_steps + "] in EXAMPLE-DOGS : {init} in time <= " + in_time + " .)\n"
    list_of_lines[i - 3] = addition
    write_to_Maude_file(list_of_lines)


def write_sem_mem_to_Maude(list_of_lines, sem_mem_dict):
    look_up = "op initSemanticMem : -> SemanticMemory ."
    i = find_line(list_of_lines, look_up)
    i += 1
    list_of_lines[i] = '  eq initSemanticMem =  \n'
    for y in sem_mem_dict:
        i += 1
        domain = sem_mem_dict[y][0]
        time = str(sem_mem_dict[y][1])
        cat = sem_mem_dict[y][2]
        typ = sem_mem_dict[y][3]
        attr = sem_mem_dict[y][4]
        addition = '("' + domain + '" : "' + cat + '" |- ' + time + ' ->| (' + typ + ' "' + attr + '")) \n'
        list_of_lines.insert(i, addition)
    list_of_lines[i + 1] = '.\n'
    write_to_Maude_file(list_of_lines)
    return list_of_lines


def write_exp_to_Maude(list_of_lines, exp_dict, is_learn):
    look_up = "semanticMem : initSemanticMem > ."
    i = find_line(list_of_lines, look_up)
    i += 1
    list_of_lines[i] = '  eq init = \n'
    for y in exp_dict:
        i += 1
        domain = exp_dict[y][0]
        item = exp_dict[y][1]
        time = str(exp_dict[y][2])
        cat = exp_dict[y][3]
        typ = exp_dict[y][4]
        attr = exp_dict[y][5]
        time_in = str(exp_dict[y][6])
        if is_learn:
            rep = str(exp_dict[y][7])
            rep_time_in = str(exp_dict[y][8])
            if item == "fact":
                addition = '(repeat ' + rep + ' times starting in ' + rep_time_in + ' : exp(((a "' + cat + '" ' + typ + ' "' + attr + '") for ' + time + ') in ' + time_in + ')) \n'
                # print (addition)
                list_of_lines.insert(i, addition)
            if item == "question":
                i -= 1
        else:
            if item == "question":
                if typ == "is a":
                    addition = '(exp(((' + typ + ' "' + cat + '" "' + attr + '" ?) for ' + time + ') in ' + time_in + ')) \n'
                else:
                    addition = '(exp(((' + typ + ' a "' + cat + '" "' + attr + '" ?) for ' + time + ') in ' + time_in + ')) \n'
                list_of_lines.insert(i, addition)
            elif item == "fact":
                i -= 1
    if is_learn:
        list_of_lines[i + 1] = 'theHuman .\n'
        write_to_Maude_file(list_of_lines)
    else:
        return list_of_lines, i


def write_env_to_Maude(list_of_lines, env_dict, i):
    for y in env_dict:
        i += 1
        domain = env_dict[y][0]
        item = env_dict[y][1]
        time = str(env_dict[y][2])
        cat = env_dict[y][3]
        typ = env_dict[y][4]
        attr = env_dict[y][5]
        if item == "question":
            addition = '(perc((' + typ + ' a "' + cat + '" "' + attr + '" ?) for ' + time + ')) \n'
            list_of_lines.insert(i, addition)
        elif item == "fact":
            i -= 1

    list_of_lines[i + 1] = 'theHuman .\n'
    write_to_Maude_file(list_of_lines)
    return list_of_lines


def write_stm_to_Maude(list_of_lines, exp_dict, env_dict, is_learn):
    look_up = "ops init-STM : -> ShortTermMemory ."
    i = find_line(list_of_lines, look_up)
    i += 1
    list_of_lines[i] = '  eq init-STM = \n'
    if is_learn:
        for y in exp_dict:
            i += 1
            domain = exp_dict[y][0]
            item = exp_dict[y][1]
            cat = exp_dict[y][3]
            typ = exp_dict[y][4]
            attr = exp_dict[y][5]
            if item == "fact":
                addition = '(chunk goal("' + domain + '", rehearsed, 0, 5) decay INF of DECAY-TIME) ; \n'
                list_of_lines.insert(i, addition)
                i += 1
                addition = '(chunk a "' + cat + '" ' + typ + ' "' + attr + '" decay INF of DECAY-TIME) ; \n'
                list_of_lines.insert(i, addition)
            if item == "question":
                i -= 1
    else:
        for y in exp_dict:
            i += 1
            domain = exp_dict[y][0]
            item = exp_dict[y][1]
            if item == "question":
                addition = '(chunk goal("' + domain + '", foundAnswer, 0, 5) decay INF of DECAY-TIME) ; \n'
                list_of_lines.insert(i, addition)
            if item == "fact":
                i -= 1

        for y in env_dict:
            i += 1
            domain = env_dict[y][0]
            item = env_dict[y][1]
            if item == "question":
                addition = '(chunk goal("' + domain + '", foundAnswer, 0, 5) decay INF of DECAY-TIME) ; \n'
                list_of_lines.insert(i, addition)
            if item == "fact":
                i -= 1
    list_of_lines[i] = list_of_lines[i][:-4]
    list_of_lines[i + 1] = '\n .\n'
    return list_of_lines