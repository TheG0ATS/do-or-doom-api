import schedule
import time
from tasks.models import Task
from accounts.models import CustomUser

def check_for_overdue_tasks():
    # for each user, 
    # for each task, 
    # if a task's due date is greater than the current date, 
    # send message via twillo
    print("Checked for overdue tasks.")

schedule.every(1).seconds.do(check_for_overdue_tasks)

while True:
    schedule.run_pending()
    time.sleep(1)