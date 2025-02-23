from flask import Flask, render_template, request, jsonify
from celery import Celery
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# MongoDB configuration
mongo_client = MongoClient('mongodb://mongodb:27017/')
db = mongo_client.taskdb

# Celery configuration
celery = Celery('tasks', broker='redis://redis:6379/0')

@app.route('/')
def index():
    return render_template('index.html', 
                         name="Gaurav Malave",
                         roll_number="2022BCD0017",
                         bio="A highly motivated Data Science and AI undergraduate from India with a strong interest in finance, machine learning, and software development. You enjoy reading books, watching movies, playing football, and learning something new every day.")

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = list(db.tasks.find({}, {'_id': False}))
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    task['status'] = 'pending'
    db.tasks.insert_one(task)
    
    # Send task to worker
    celery.send_task('process_task', args=[task])
    return jsonify({"message": "Task created successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)