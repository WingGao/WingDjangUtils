from celery import Celery


def query_task(app, name):
    """
    查询
    Args:
        app (Celery): 主要app
        name (str): 任务名称
    Returns:
        list，包含所有taskid
    """
    tasks = app.control.inspect.active()
    return filter(lambda x: x == name, tasks)
