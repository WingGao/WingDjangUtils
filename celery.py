from celery import Celery
from celery.utils.saferepr import saferepr


def query_task(app, name, args=None, one=False):
    """
    查询
    Args:
        app (Celery): 主要app
        name (str): 任务名称
        args (tuple|func(item)): 任务参数
        one (bool): 只获取一个
    Returns:
        list，包含所有taskid
    """
    inspect = app.control.inspect()
    out = []
    for i in range(10):
        workers = None
        if i == 0:
            workers = inspect.active()  # 正在执行
        else:
            break

        if workers is None:
            continue

        argsrepr = None
        argsfunc = None
        if args is not None:
            if callable(args):
                argsfunc = args
            else:
                argsrepr = saferepr(args)

        def check_task(task):
            if task['name'] == name:
                if argsrepr is not None and argsrepr == task['args']:
                    return True
                elif argsfunc is None:
                    return argsfunc(task)
            return False

        for k, worker in list(workers.items()):
            for t in worker:
                if check_task(t):
                    out.append(t)
                    if one:
                        return out
    return out


def get_first_task(res):
    """
    获取第一个任务
    Args:
        res:

    Returns:
        详细 ((string, dict)):
    """
    for k, ts in list(res.items()):
        for k2 in ts:
            return ts[k2]
    return None
