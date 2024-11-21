import random
import os
from flask import Flask, send_from_directory, jsonify, request

app = Flask(__name__)

# App sets endpoint at "localhost:3000/content" and receives GET requests with query string containing parameter 'type'. 
# If parameter value is 'task', microservice returns random task in JSON-format as 'task:(value)' pair.
# If parameter value is 'image', microservice return random image.
# Otherwise error message is returned.
@app.route('/content', methods=['GET'])
def get_content():
    content_type = request.args.get('type')
    
    if content_type == 'task':
        task_file = open('tasks.txt', 'r')
        tasks = task_file.read().splitlines()
        task_file.close() 
        return jsonify({"task": random.choice(tasks)})
    elif content_type == 'image':
        return send_from_directory(directory='images', path=random.choice(os.listdir('images')))
    else:
        return "Wrong 'type' parameter value. Use 'tasks' or 'image'.", 400


if __name__ == '__main__':
    app.run(port=3000)