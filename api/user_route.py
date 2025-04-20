# Returns routes found by users between start and end

import csv
from urllib.parse import unquote

from os.path import dirname, abspath, join
dir = dirname(abspath(__file__))

# User paths stores an array of tuples (duration, user_path)
user_paths = []

# Read data
with open(join(dir, 'data', 'user_paths.tsv'), 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    
    for row in reader:
        # skip comments at top of file
        if len(row) == 0 or row[0][0] == '#': continue
        
        user_path = row[3].split(";")
        parsed_user_path = []
        for part in user_path:
            # Ignore back clicks
            if part == "<":
                continue
            parsed_user_path.append(unquote(part).lower())
        
        user_paths.append((row[2], parsed_user_path))


# Returns average path length, average duration to solve, and shortest path a user could find
def get_user_route(src, to):
    total_path_length = 0
    total_duration = 0
    shortest_user_path = None
    
    valid_paths = 0
    for user_path in user_paths:
        duration = int(user_path[0])
        path = user_path[1]
        
        if path[0] != src or path[-1] != to:
            continue
        valid_paths += 1
        
        total_path_length += len(path)
        total_duration += duration
        
        if shortest_user_path is None or len(path) < len(shortest_user_path):
            shortest_user_path = path
    
    # No user paths found
    if valid_paths == 0:
        return None, None, None
    
    avg_path_length = total_path_length / valid_paths
    avg_duration = total_duration / valid_paths
    
    return round(avg_path_length, 4), round(avg_duration, 4), shortest_user_path