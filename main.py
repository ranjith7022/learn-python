def verify_tsp(paths, dist, actual_path):
    total = 0
    first = None
    for i in range(len(actual_path)):
        
        if i==0:
            first = actual_path[i]
            continue
            
        total += paths[first][actual_path[i]]
        first = actual_path[i]
            
        
    if total < dist:
        return True
    return False
        
        
        
