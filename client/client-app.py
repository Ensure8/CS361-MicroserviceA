import requests

type = input("Enter 'task' for a to-do task or 'image' for a profile picture image: ").strip()
url = f'http://localhost:3000/content?type={type}'
response = requests.get(url)

if response.status_code == 200:
    if type == 'task':
        file = open("task.txt", 'w')
        file.write(response.json().get("task"))
        file.close()
        print(f"Task saved to tasks.txt.")
    elif type == 'image':
        file = open("images/profile_picture.jpg", 'wb')
        file.write(response.content)
        file.close()
        print(f"Picture image saved under /images.")
else:
    print("Error:", response.text)