number_of_completed_tasks = 12
number_of_hours_spent: float = 1.5
course_name = "Python"
time_for_one_task: float = number_of_hours_spent / number_of_completed_tasks

print("Курс:", course_name + ",", "всего задач:", str(number_of_completed_tasks) + ",", "затрачено часов:",
      str(number_of_hours_spent) + ",", "среднее время выполнения:", time_for_one_task, "часа")
