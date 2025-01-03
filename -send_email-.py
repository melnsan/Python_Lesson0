def send_email(message, recipient, sender = "university.help@gmail.com"):
    if(('@' not in recipient) or ('@' not in sender) or (recipient.endswith(".com") == False) or (sender.endswith(".com") == False)
        or (recipient.endswith(".ru") == False) or (sender.endswith(".ru") == False) or (recipient.endswith(".net") == False)
        or (sender.endswith(".net") == False)):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    elif (recipient == sender):
        print("Нельзя отправить письмо самому себе!")
    elif (sender == 'university.help@gmail.com'):
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('1) Hi, Alex!', 'test1@gmail.com', 'test1@gmail.com')
send_email('2) Hi, Alex!', 'test1@test1.com', 'test2.test2.com')
send_email('3) Hi, Alex!', 'test1@test1.com', 'test2@test2.ua')
send_email('4) Hi, Alex!', 'test1@test1.ua', 'test2@test2.net')
send_email('5) Hi, Alex!', 'test1@test1.ru', 'test1@test1.net')
send_email('6) Hi, Alex!', 'test1@test1.ru')
send_email('7) Hi, Alex!', 'test1@test1.ru', 'admin@test.net')