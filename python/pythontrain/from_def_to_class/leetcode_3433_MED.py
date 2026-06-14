# Количество пользователей и сколько раз они упоминались
class Solution(object):
    def countMentions(self, numberOfUsers, events):
        # Проверку на типы данных
        if self.num_is_integer(numberOfUsers):
            self.numberOfUsers=numberOfUsers

        self.events=events
        # Счетчик по времени статусы
        # Проверка вложенных списков
        x=0
        timestamp_before=0
        self.status_mess = None
        self.timestamp_current = 0
        self.type_of_mess = None
        self.get_message = None
        self.for_who = None
        self.count_user = []
        self.list_end = []
        zed = self.numberOfUsers
        while zed != 0:
            zed -= 1
            self.list_end.append(0)
        # print(f"Это self.events: {self.events}")
        

        for event in self.events:
            time_dif = 0
            status = "online"
            x+=1
            print(f"---------------- Итерация номер: {x}")
            self.num_is_list(event)
            len_event=len(event)
            if len(event) > 3:
                return f"Количество элементов {event} больше 3: {len_event} "
            # Проверка типа сообщения и соответствующие действия
            self.status_mess=event[0]
            self.timestamp_current=event[1]
            self.type_of_mess=event[2]

            

            # Просчет статуса пользователей


            
                    # Проверка есть ли данный пользователь. 
                    # Если нет добавляем, если есть обновляем
                    # Обращаемся по имени к словарю

            # Получать время
            # Постоянная проверка разницы во времени
            # Определить пользователей
            # раздавать статус
            
            if x>1:
                print(f"timestamp_before: {timestamp_before}, timestamp_current: {self.timestamp_current}")
                self.timestamp_current= int(self.timestamp_current)
                timestamp_before = int(self.timestamp_current)
                time_dif = self.timestamp_current - timestamp_before
                print(f"time_dif: {time_dif}")
                timestamp_before = self.timestamp_current
                if time_dif > 59:
                    status = "online"

            if self.status_mess == "MESSAGE":
                print("Отправляем сообщение")
            elif self.status_mess == "OFFLINE":
                print("Кого отправляем в OFFLINE")

            self.type_of_mess = self.type_of_mess.split()

            if len(self.type_of_mess) == 1:
                if self.type_of_mess[0] == "HERE":
                    self.for_who = "HERE"
                    self.update_for_all()
                elif self.type_of_mess[0] == "ALL":
                    # Присобачить функцию которая в зависимости от статуса обновляет данные
                    self.for_who = "ALL"
                    print("Сообщение вообще всем")
                    self.update_for_all()
                else:
                    print(f"Это пользователь: {self.type_of_mess}")
                    self.user_checker(self.type_of_mess)
                    # Проверка есть ли данный пользователь. 
                    # Если нет добавляем, если есть обновляем
                    # Обращаемся по имени к словарю
            else:
                count_range_user = self.type_of_mess
                count_range_user = sorted(count_range_user)
                for count_usr in count_range_user:
                    print(f"count_usr: ----------- {count_usr}")
                    self.user_checker(count_usr)

                    print("Проверка количества пользователей")
                    print("Это надо разобрать")
            print(f"Пользователи: {self.count_user}")
            print("В итоге понять кто в онлайне и кто получил письмо")
            print("В итоге просто считать поользователей и сколько раз им приходило письмо")
        # list_end[1] - количество пользователей
        # list_end[0] - сколько раз были в сети
        self.count_all_info()
        print(f"Кому адресовано сообщение {self.for_who}")
        # print(f"Сколько пользователей: {self.list_end[0]}")
        # print(f"Сколько сообщений: {self.list_end[1]}")

        return(self.list_end)
        """
        :type numberOfUsers: int
        :type events: List[List[str]]
        :rtype: List[int]
        """
    def user_checker(self, getUser):
        print(f"self.timestamp_current {self.timestamp_current} ---------------------------")
        # Здесь же должны и обновлять статус
        # Получать статус у пользователя делать анализ и добавлять
        # Какое self.type_of_mess = Here
        # Высчитываем в сети или нет
        try:
            getUser = int(getUser[0])
        except:
            getUser = getUser
        print(f"getUser: {getUser}, {getUser} {self.num_is_integer(getUser)}")
        if self.num_is_integer(getUser):
            print(f"Это пользователь. По индексу {getUser}")
            if getUser < len(self.count_user):
                print(f"Пользователь {self.count_user[getUser]["user"]} существует")
                print(f"Обновляем данные")
                prev_time_diff = self.count_user[getUser]["time_diff"]
                diff_time = self.timestamp_current - prev_time_diff
                print(f"Разница во времени diff_time: {diff_time}")
                # self.count_user[getUser]["time_diff"] = 0 # Исправить
                # Получать статус у пользователя делать анализ и добавлять
                # Какое self.type_of_mess = Here
                # Высчитываем в сети или нет
                if diff_time > 59:
                    self.count_user[getUser]["status"] = "online" # Исправить
                    self.count_user[getUser]["time_diff"] = self.timestamp_current
                elif self.status_mess == "OFFLINE":
                    self.count_user[getUser]["status"] = "offline"
                    self.count_user[getUser]["time_diff"] = self.timestamp_current

                # if self.status_mess == "MESSAGE":
                #     if self.count_user[getUser]["status"] == "online":
                #         self.count_user[getUser]["count_mess"] += 1 # Исправить
                #         self.count_user[getUser]["time_diff"] = self.timestamp_current

                if self.status_mess == "MESSAGE":
                    if self.for_who == "ALL":
                        self.count_user[getUser]["count_mess"] += 1 # Вообще может отдельной функцией обновлять
                    elif self.for_who == "HERE":
                        if self.count_user[getUser]["status"] == "online":
                            self.count_user[getUser]["count_mess"] += 1
                            self.count_user[getUser]["time_diff"] = self.timestamp_current
            else:
                print(f"Пользователь {getUser} не существует")
                print(f"Добавляем пользователя")
                count_mess = 0
                if self.status_mess == "MESSAGE":
                    count_mess += 1
                self.count_user.append({
                    "user": getUser,
                    "time_diff": 0,
                    "status": "online",
                    "count_mess": count_mess
                })
                print(f"1. User: {self.count_user[getUser]}")
            # Проверка есть ли данный пользователь. 
            # Если нет добавляем, если есть обновляем
            # Обращаемся по массиву
        else:
            print(f"Это пользователь. По имени {getUser}")
            find_index = None
            print(f"self.count_user {self.count_user}")
            # Если пользователей больше нуля
            if len(self.count_user) > 0:
                for count_usr1 in self.count_user:
                    if count_usr1["user"] == getUser:
                        print(count_usr1["user"])
                        find_index = count_usr1
                        break
                if find_index is not None:
                    self.count_user[find_index]
                    print(f"Пользователь {self.count_user[getUser]["user"]} существует")
                    print(f"Обновляем данные")


                    prev_time_diff = self.count_user[find_index]["time_diff"]
                    diff_time = self.timestamp_current - prev_time_diff
                    print(f"Разница во времени diff_time: {diff_time}")
                    # count_user_getUser = self.count_user[getUser]["time_diff"] = 0 # Исправить
                    # Получать статус у пользователя делать анализ и добавлять
                    # Какое self.type_of_mess = Here
                    # Высчитываем в сети или нет
                    if diff_time > 59:
                        self.count_user[find_index]["status"] = "online" # Исправить
                    elif self.status_mess == "OFFLINE":
                        self.count_user[find_index]["status"] = "offline"
                        self.count_user[find_index]["time_diff"] = self.timestamp_current

                    # if self.status_mess == "MESSAGE":
                    #     if self.count_user[find_index]["status"] == "online":
                    #         self.count_user[find_index]["count_mess"] += 1 # Исправить
                    #         self.count_user[find_index]["time_diff"] = self.timestamp_current
                    
                    if self.status_mess == "MESSAGE":
                        if self.for_who == "ALL":
                            self.count_user[find_index]["count_mess"] += 1 # Вообще может отдельной функцией обновлять
                        elif self.for_who == "HERE":
                            if self.count_user[find_index]["status"] == "online":
                                self.count_user[find_index]["count_mess"] += 1
                                self.count_user[find_index]["time_diff"] = self.timestamp_current


                    # self.count_user[find_index]["time_diff"] = 0 # Исправить
                    # self.count_user[find_index]["status"] = 0 # Исправить
                    # self.count_user[find_index]["count_mess"] = 0 # Исправить
                else:
                    print(f"Пользователь {getUser} не существует")
                    print(f"Добавляем пользователя")
                    count_mess = 0
                    if self.status_mess == "MESSAGE":
                        count_mess += 1
                    self.count_user.append({
                        "user": getUser,
                        "time_diff": 0,
                        "status": "online",
                        "count_mess": count_mess
                    })
                    
            else:
                print(f"Пользователь {getUser} не существует")
                print(f"Добавляем пользователя")
                count_mess = 0
                if self.status_mess == "MESSAGE":
                    count_mess += 1
                self.count_user.append({
                    "user": getUser,
                    "time_diff": 0,
                    "status": "online",
                    "count_mess": count_mess
                })
                print(f"2. User: {self.count_user}")
                
    def update_for_all(self):
        if len(self.count_user) > 0:
            for count_usr1 in self.count_user:
                print(f"отдельно count_usr1: {count_usr1}")
                print(f"отдельно Пользователь {count_usr1["user"]} существует")
                print(f"отдельно Обновляем данные")

                prev_time_diff = count_usr1["time_diff"]
                print(f"prev_time_diff: {prev_time_diff}")
                diff_time = self.timestamp_current - prev_time_diff
                print(f"Разница во времени diff_time: {diff_time}")
                # count_user_getUser = self.count_user[getUser]["time_diff"] = 0 # Исправить
                # Получать статус у пользователя делать анализ и добавлять
                # Какое self.type_of_mess = Here
                # Высчитываем в сети или нет
                if diff_time > 59:
                    count_usr1["status"] = "online" # Исправить
                elif self.status_mess == "OFFLINE":
                    count_usr1["status"] = "offline"
                    count_usr1["time_diff"] = self.timestamp_current

                # if self.status_mess == "MESSAGE":
                #     if count_usr1["status"] == "online":
                #         count_usr1["count_mess"] += 1 # Исправить
                #         count_usr1["time_diff"] = self.timestamp_current

                if self.status_mess == "MESSAGE":
                    if self.for_who == "ALL":
                            count_usr1["count_mess"] += 1 # Вообще может отдельной функцией обновлять
                            count_usr1["time_diff"] = self.timestamp_current
                    elif self.for_who == "HERE":
                        if count_usr1["status"] == "online":
                            count_usr1["count_mess"] += 1
                            count_usr1["time_diff"] = self.timestamp_current
    
    def count_all_info(self):
        for count_usr1 in range(len(self.count_user)):
            print(f"Подсчет количества:\n{count_usr1}")
            self.list_end[count_usr1] = self.count_user[count_usr1]["count_mess"]

        if self.list_end[1] == 0:
            print("++++++++++++++++")
            print(sorted(self.list_end, reverse=False))
            self.list_end = sorted(self.list_end, reverse=False)



    def num_is_integer(self, numberOfUsers):
        return isinstance(numberOfUsers, int)
    def num_is_list(self, events):
        return isinstance(events, int)


# events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]
events = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]
push_events = Solution()
result = push_events.countMentions(2, events)
print(f"Полученнный ответ: {result}")







# # Правильный короткий вариант

# class Solution:
#     def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
#         # Сортируем события: по времени, при равном времени OFFLINE раньше MESSAGE
#         events.sort(key=lambda x: (int(x[1]), x[0] == 'MESSAGE'))
        
#         mentions = [0] * numberOfUsers
#         offline_until = [0] * numberOfUsers  # до какого времени пользователь оффлайн
        
#         for event_type, timestamp, data in events:
#             timestamp = int(timestamp)
            
#             if event_type == "OFFLINE":
#                 user_id = int(data)
#                 offline_until[user_id] = timestamp + 60
                
#             else:  # MESSAGE
#                 if data == "ALL":
#                     # Все пользователи получают +1
#                     for i in range(numberOfUsers):
#                         mentions[i] += 1
                        
#                 elif data == "HERE":
#                     # Только онлайн пользователи
#                     for i in range(numberOfUsers):
#                         if offline_until[i] <= timestamp:
#                             mentions[i] += 1
                            
#                 else:
#                     # Список конкретных id
#                     ids = data.split()
#                     for id_str in ids:
#                         user_id = int(id_str[2:])  # отрезаем 'id'
#                         mentions[user_id] += 1
        
#         return mentions
