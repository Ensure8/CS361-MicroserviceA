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

## How to Handle Response Data
To handle the response data, the client application must be able to save or store the requested content appropriately. 

This python example code shows how to get the response content (image) and save it as "profile_picture" under '/images' as JPG:

```python
import requests

url = f'http://localhost:3000/content?type=image'
response = requests.get(url)

file = open("images/profile_picture.jpg", 'wb') # This path can be changed depending on where the image should be saved instead.
file.write(response.content)
file.close()
```

This python code shows how a client can handle tasks by saving the content (value of "task" name in the JSON response body) under a text file called "task.txt".

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
Commit has images stored under "/images" and some to-do tasks under "tasks.txt".

To run the server application locally, Flask must be installed: 
##### `pip install flask`
To run the test program, the "requests" library must be installed: 
##### `pip install requests`

## Sequence Diagram
![Sequence diagram](https://github.com/user-attachments/assets/170f2b57-4649-4b68-9f1f-1b64c4cccab4)

