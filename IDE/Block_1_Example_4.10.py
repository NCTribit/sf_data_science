from collections import defaultdict, deque


# tasks = [(36871, 'office', False),
#          (40690, 'office', False),
#          (35364, 'voltage', False),
#          (41667, 'voltage', True),
#          (33850, 'office', False)]
 

def task_manager(task_list: list) -> defaultdict:
    dd = defaultdict(deque)
    for task, server, is_prio in task_list:
        if is_prio:
            dd[server].appendleft(task)
        else:
            dd[server].append(task)
    return dd
    
 
# print(task_manager(tasks))
print(task_manager(tasks = [(36871, 'office', False), (40690, 'office', False), (35364, 'voltage', False), (41667, 'voltage', True), (33850, 'office', False)]))
# defaultdict(, {'voltage': deque([41667, 35364]),
# 'office': deque([36871, 40690, 33850])})


from collections import defaultdict, deque

def task_manager(tasks):
    servers = defaultdict(deque)
    for task in tasks:
        if task[-1]:
            servers[task[1]].appendleft(task[0])
        else:
            servers[task[1]].append(task[0])
    return servers