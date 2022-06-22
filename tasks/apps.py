from django.apps import AppConfig
from schedule import every, repeat

class TasksConfig(AppConfig):
    name = 'tasks'

# @repeat(every(1).second)
# def check_for_overdue_tasks():
    #from tasks.models import Task
    # my_data = Task.objects.all().values()
    # get all users and tasks from db
    # for each user, 
    # for each task, 
    # if a task's due date is greater than the current date, 
    # send message via twillo
    # print(f"Checked for overdue tasks.")
    #print(my_data)

# while True:
#     schedule.run_pending()
#     time.sleep(1)