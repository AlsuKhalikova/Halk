# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, arg=","):
    list1 = first.split(arg)
    list2 = second.split(arg)

    common = list(set(list1).intersection(set(list2)))
    common.sort()

    return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print("Общие участники:", find_common_participants(participants_first_group, participants_second_group, "|"))
