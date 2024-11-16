# CS361-MicroserviceA

- This microservice is to allow clients to request random profile picture images or to-do tasks.


## How to Request Data
To request data/content from the microservice, the client application must make a GET request to the microservice's URL-endpoint `/content` with a query string. It must contain parameter `type=`, with values `image` or `task`. 

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
To handle the response data, the client application must be able to save the image file in a directory if the value for the parameter `type=` in the query string was `image`.


```python
import requests

url = f'http://localhost:3000/content?type=image'
response = requests.get(url)

file = open("images/profile_picture.jpg", 'wb') # This path can be changed depending on where the image should be saved instead.
file.write(response.content)
file.close()
```

This code shows how a client can handle a JSON response body containing the `task` name and its value.

```python
import requests

url = f'http://localhost:3000/content?type=task'
response = requests.get(url)

file = open("tasks.txt", 'w') # The file path should be changed depending on where the to-do task (plain text) should be written/stored in.
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
        file = open("tasks.txt", 'w')
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
```

## Notes
Latest commit has some images stored under "/images" and some (text) to-do tasks under "tasks.txt".

To run the server application, Flask must be installed: 
##### `pip install flask`
To run the client app, the "requests" library must be installed: 
##### `pip install requests`

## Sequence Diagram
