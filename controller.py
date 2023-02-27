import model
import view
import datetime
import color_text


def klick_menu():
    while True:
        number = view.menu()
        if number == 4:  # функционал добавления новой заметки при нажатии кнопки 4
            g = model.add_task()
            return g
        elif number == 1:  # функционал распечатывания всей книжки при нажатии кнопки 1
            return model.print_all_task()
        elif number == 2:  # функционал поиска заметки по её номеру
            number_id = input("\t\t\t\033[34mВведите номер заметки, которую необходимо найти в записной книжке \033[0m")
            answer = model.find_task_id(number_id)
            return view.output(answer)
        elif number == 3:  # функционал фильтрации записной книжки по дате
            find_day = input("\t\t\t\033[34mВведите число месяца: \033[0m")
            find_month = input("\t\t\t\033[34mВведите месяц: \033[0m")
            find_year = input("\t\t\t\033[34mВведите год: \033[0m")
            result = model.find_task_date(find_day, find_month, find_year)
            dtn = str(datetime.datetime.now())
            with open(f'{find_day}_{find_month}_{find_year}_.txt', 'a', encoding='utf-8') as data:
                data.write("\n" + " список заметок на указанную дату отображен " + f'{dtn}' + "\n-----------"
                                                                                              "-----------------------"
                                                                                              "------------------------"
                                                                                              "------------------\n")
            return view.output(result)
        elif number == 5:  # функционал удаление змаетки из записной книжки
            number_id = input("\t\t\t\033[34mВведите номер заметки, которую необходимо удалить: \033[0m")
            return view.output(model.delete_task(number_id))
        elif number == 6:  # функционал редактирования заметки
            number_id = input("\t\t\t\033[34mВведите номер заметки, которую необходимо отредактировать: \033[0m")
            return view.output(model.edit_task(number_id))
        elif number == 7:  # функционал выхода из справочника
            return 0


def run():
    while klick_menu() != 0:
        klick_menu()
    return view.output("\t\t\tспасибо за работу c записной книжкой!!!")
