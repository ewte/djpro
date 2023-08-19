import socket

def client():
    host = 'localhost'  # IP-адрес сервера
    port = 12345  # Порт сервера

    # Создание сокета
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Подключение к серверу
    client_socket.connect((host, port))

    message = "Hello, server!"  # Сообщение для отправки

    # Отправка сообщения серверу
    client_socket.sendall(message.encode())

    # Получение ответа от сервера
    response = client_socket.recv(1024).decode()
    print("Ответ от сервера:", response)

    # Закрытие соединения
    client_socket.close()

# Вызов функции клиента
#client()

def pr():
    return 'hello im function'
