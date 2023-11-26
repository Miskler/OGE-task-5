from time import time
from progress.bar import Bar


## Изменяемые переменные
start_number:int = 1  # Начальное значение
end_number:int = 4762 # Искомое значение
operations_count:int = 17   # Максимальное количество действий

## Не изменяемые переменные
solutions_counter = 0 # Насчитано ответов
time_start = time() # Начало выполнения операции
hards = pow(2, operations_count)-1 # Рассчитываем примерное количество вызовов функции calc_result
hard_complete = 0 # Сколько прошло вызовов функции calc_result

bar = Bar(max=hards, stream=1) # Объект %-бар


# Рассчитываем все возможные варианты решения задачи
def calc_result(number:int, id:int = 0):
    operator_i = number * 2 # Операция "номер 1"
    operator_ii = number + 3 # Операция "номер 2"

    intermediate_result = {}
    global solutions_counter
    global operations_count
    if id < operations_count and end_number != number:
        global bar
        global hard_complete

        bar.next()
        hard_complete += 1

        try:
            actual_percent = (float(hard_complete)/float(hards))*100.0
        except:
            actual_percent = 0

        bar.bar_prefix = f"Рассчетное время: {who_percent(secs=time()-time_start, percent=actual_percent)} сек | {solutions_counter} решений найдено |"
        bar.update()
        
        
        i = calc_result(operator_i, id+1)
        ii = calc_result(operator_ii, id+1)

        if i == False and ii == False:
            return False

        if i != False:
            intermediate_result["I"] = operator_i if i == True else [operator_i, i]
        if ii != False:
            intermediate_result["II"] = operator_ii if ii == True else [operator_ii, ii]
    else:
        if end_number == number:
            solutions_counter += 1
        
        if id <= operations_count:
            current_nesting += 1
            bar.bar_suffix = f"| {current_nesting} текущая вложенность {f-current_nesting} |"
            bar.update()

        return end_number == number
    return intermediate_result

# Рассчитываем сколько примерно осталось времени до завершения операции
def who_percent(secs, percent):
    try:
        return round((secs / percent) * (100-percent))
    except:
        return "N"


# Выводим результат рассчитаный calc_result
show_result_counter:int = 0
def show_result(results:dict, result:str = "", actions:int = 0):
    global show_result_counter
    for key in results.keys():
        result += key
        actions += 1

        if type(results[key]) is list:
            result += " -> "
            show_result(results=results[key][1], result=result, actions=actions)
        else:
            show_result_counter += 1
            print(f"{show_result_counter}. ({actions} действий) "+result)


if __name__ == '__main__': 
    result = calc_result(number=start_number)
    bar.bar_prefix = f"Операция выполнялась {round(time()-time_start, 2)} сек |"
    bar.update()
    bar.finish()

    if solutions_counter > 0:
        show_result(results=result)
        print(f"У задачи {solutions_counter} решений")
    else:
        print("Решений нет!")
