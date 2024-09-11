from .models import Task

class TaskManager:
  def __init__(self):
    self.task = Task.objects.all()

  def get_task_by_id(self, task_id):
        try:
            return Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return None

  def add_task(self, title, description, priority, status):
    task = Task(title=title, description=description, priority=priority, status=status)
    task.save()

  def delete_task(self, task_id):
    task = self.get_task_by_id(task_id)
    if task:
      task.delete()

  def edit_task(self, task_id, new_data):
    task = self.get_task_by_id(task_id)
    if task:
      task.title = new_data.get('title',task.title)
      task.description = new_data.get('description', task.title)
      task.priority = new_data.get('priority', task.priority)
      task.status = new_data.get('status', task.status)
      task.save()

  def view_all_tasks(self):
     return Task.objects.all()
  
  def filter_tasks_by_priority(self, priority):
     return Task.objects.filter(priority=priority)
     


