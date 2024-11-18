# CS361-MicroserviceA

This microservice can provide client-applications random profile picture images or to-do tasks.


## How to Request Data
To request data/content from the microservice, the client application must make a GET request to the microservice's URL-endpoint, `localhost:3000/content`, with a query string. The query string must contain parameter `type`, with values `image` or `task` depending on what content is being requested. 

#### The following python test code requests a random image:

```python
import requests

url = f'http://localhost:3000/content?type=image'
response = requests.get(url)
```
#### This python test code requests a random to-do task (text):
```python
import requests

url = f'http://localhost:3000/content?type=task'
response = requests.get(url)
```

## How to Handle and Receive Response Data
If a client application makes a GET request to the endpoint, a GET response will be provided by the microservice with the appropriate content. A random image will be provided or a JSON body containing the "task" key and the to-do task as the value. If the response was a task, the client should be able to parse the content of the JSON string. If the response was an image, the client application should be able to store it in an appropriate place.

This python example code shows how to get the response content (image) and save it as "profile_picture" under '/images' as JPG:

```python
import requests

url = f'http://localhost:3000/content?type=image'
response = requests.get(url)

file = open("images/profile_picture.jpg", 'wb') # This path can be changed depending on where the image should be saved instead.
file.write(response.content)
file.close()
```

This python code shows how a client can handle tasks by saving the content (value of "task" key) under a text file called "task.txt".

```python
import requests

url = f'http://localhost:3000/content?type=task'
response = requests.get(url)

file = open("task.txt", 'w') # The file path should be changed depending on where the to-do task (plain text) should be written/stored in.
file.write(response.json().get("task"))
file.close()
```

## Test Program Code
```python
import requests

type = input("Enter 'task' for a to-do task or 'image' for a profile picture image: ").strip()
url = f'http://localhost:3000/content?type={type}'
response = requests.get(url)

if response.status_code == 200:
    if type == 'task':
        file = open("task.txt", 'w')
        file.write(response.json().get("task"))
        file.close()
    elif type == 'image':
        file = open("images/profile_picture.jpg", 'wb')
        file.write(response.content)
        file.close()
else:
    print("Error:", response.text)
```

## Notes
Commit has images (from Kaggle) stored under "/images" and some to-do tasks under "tasks.txt".

To run the server application locally, Flask must be installed: 
##### `pip install flask`
To run the test program, the "requests" library must be installed: 
##### `pip install requests`

## Sequence Diagram
![Copy of Sequence diagram](https://github.com/user-attachments/assets/778814d6-0d82-48b8-a0ed-815f1f5bc831)




