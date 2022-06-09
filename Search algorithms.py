
def get_node(name,heuristic=None,weight=None):
    node = {}
    node['name'] = name
    node['children'] = []
    node['heuristic']=heuristic
    node['weight']=weight
    node['path']=[]
    
    return node


def add_child(node, name, heuristic=None, weight=None):
    node['children'].append(get_node(name, heuristic, weight))

def get_heuristic_search_tree():
    tree = get_node('Kitchener',heuristic=130)

    add_child(tree, 'New Hamburg',heuristic=110)   
    add_child(tree, 'Guelph',heuristic=160) 

    add_child(tree['children'][0], 'Straford',heuristic=100) 

    add_child(tree['children'][1], 'Drayton',heuristic=100)
    add_child(tree['children'][0], ['children'][0],'Drayton', heuristic=100)
    add_child(tree['children'][0], ['children'][0], 'St.Marys', heuristic=130)
    add_child(tree['children'][1], ['children'][0], 'Listowel', heuristic=0)

    add_child(tree['children'][0], ['children'][0], ['children'][0],'Listowel', heuristic=0)
    add_child(tree['children'][0], ['children'][0], ['children'][1],'Mitchell', heuristic=100)
    add_child(tree['children'][0], ['children'][0], ['children'][1],['children'][0],'listowel', heuristic=0)

    return tree
   

def UCS_search_tree():
    tree = get_node('Kitchener',weight=None)
    add_child(tree, 'New Hamburg',heuristic=90)   
    add_child(tree, 'Guelph',heuristic=30)

    add_child(tree['children'][0], 'Straford',heuristic=25)
    add_child(tree['children'][1], 'Drayton',heuristic=100)

    add_child(tree['children'][0], ['children'][0], 'Drayton', heuristic=200)
    add_child(tree['children'][0], ['children'][0], 'St.Marys', heuristic=30)
    
    add_child(tree['children'][1], ['children'][0], 'Listowel', heuristic=100)


    add_child(tree['children'][0], ['children'][0], ['children'][0], 'Listowel', heuristic=100)
    add_child(tree['children'][0], ['children'][0], ['children'][1],'Mitchell', heuristic=80)
    add_child(tree['children'][0], ['children'][0], ['children'][1],['children'][0],'listowel', heuristic=100)

    return tree

def DFS(init_state,goal_name):
    frontier = [init_state] 
    explored = []
    while len(frontier):
        state = frontier.pop()
        explored.append(state['name'])
        state['path'].append(state['name'])
        if state['name'] == goal_name:
            return True
        for child in state['children']:
            if child['name'] not in explored:
                frontier.append(child)
                child['path'].extend(state['path'])
    return False

# BFS
def BFS(init_state, goal_name):
    frontier = [init_state]
    explored = []
    while len(frontier):
        state = frontier.pop()
        explored.append(state['name'])
        state['path'].append(state['name'])
        if state['name'] == goal_name:
            return state['path']
        for child in state['children']:
            if child['name'] not in explored:
                frontier.insert(0,child)
                child['path'].extend(state['path'])
    return False

#UCS
def find_min_weight(frontier):
    min_weight_i = 0
    if len(frontier) > 1:
        min_weight = frontier[min_weight_i]['weight'] 
        for i, state in enumerate(frontier):
            if state['weight'] < min_weight:
                min_weight_i = i
                min_weight = state['weight']
    return min_weight_i


def UCS(init_state, goal_name):
    frontier = [init_state] 
    explored = []
    while len(frontier):
        state = frontier.pop(find_min_weight(frontier))
        explored.append(state['name'])
        
        if state['name'] == goal_name:
            return True
        for child in state['children']:
            if child['name'] not in explored:
                child['weight'] += state['weight']
                frontier.append(child) 
    return False
    



#GreddySearch
def find_min_heuristic(frontier):
    min_h_i = 0
    if len(frontier) > 1:
        min_h = frontier[min_h_i]['heuristic'] 
        for i, state in enumerate(frontier):
            if state['heuristic'] < min_h: 
                min_h_i = i
                min_h = state['heuristic']
    return min_h_i
        

def GreedySearch(init_state, goal_name): 
    frontier = [init_state]
    explored = []
    while len(frontier):
        state = frontier.pop(find_min_heuristic(frontier))
        explored.append(state['name'])
        state['path'].append(state['name'])
        if state['name'] == goal_name:
            return state['path']
        for child in state['children']:
            if child['name'] not in explored:
                frontier.append(child)
                child['path'].extend(state["path"])
    return False

