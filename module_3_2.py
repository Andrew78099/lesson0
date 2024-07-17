def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    flag = bool
    for i in recipient and sender:
        if i == "@":
            flag = True
            break
        else:
            flag = False
            continue
    if flag == False:
        print("Невозможно отправить письмо с адреса <sender> на адрес <recipient>")
    elif recipient[:-5:-1] != "moc." and recipient[:-4:-1] != "ur." and recipient[:-5:-1] != "ten.":
        print(f'"Невозможно отправить письмо с адреса {sender} "на адрес" {recipient}.')
    elif sender[:-5:-1] != "moc." and sender[:-4:-1] != "ur." and recipient[:-5:-1] != "ten.":
        print(f'"Невозможно отправить письмо с адреса {sender} "на адрес" {recipient}.')
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f'"Письмо успешно отправлено с адреса" {sender} "на адрес" {recipient}.')
    else:
        print(f'"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('Это сообщение для проверки связи', 'vasyok1337gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')