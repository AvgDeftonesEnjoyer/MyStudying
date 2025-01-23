check = int(input("Choose homework number: 1, 2, 3: "))

if check == 1: # Використовуй бібліотеку requests, щоб зробити HTTP-запит до будь-якого публічного API і вивести отримані дані.    
    import requests

    url = 'https://loripsum.net/api/1/short/plaintext'

    responce = requests.get(url)

    with open('my_requests/story.txt', 'w') as file:
        file.write(responce.text)

    print(responce.status_code, 'Now you can check the story.txt file in my_requests folder')