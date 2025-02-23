from celery import Celery
from pymongo import MongoClient
import time

# Celery configuration
celery = Celery('tasks', broker='redis://redis:6379/0')

# MongoDB configuration
mongo_client = MongoClient('mongodb://mongodb:27017/')
db = mongo_client.taskdb

@celery.task(name='process_task')
def process_task(task):
    # Simulate processing time
    time.sleep(5)
    
    # Update task status in database
    db.tasks.update_one(
        {'name': task['name']},
        {'$set': {'status': 'completed'}}
    )
    
    return 'Task processed successfully'