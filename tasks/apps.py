from django.apps import AppConfig
import schedule
import time
from tasks.models import Task

app_ready = False

class TasksConfig(AppConfig):
    name = 'tasks'
    def ready(self):
        app_ready=True


def check_for_overdue_tasks():
    my_data = Task.objects.all().values()

    # get all users and tasks from db
    # for each user, 
    # for each task, 
    # if a task's due date is greater than the current date, 
    # send message via twillo
    print("Checked for overdue tasks.")
    print(my_data)

schedule.every(1).seconds.do(check_for_overdue_tasks)

while app_ready:
    schedule.run_pending()
    time.sleep(1)