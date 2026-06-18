
# Auto Logger (conceptual)
# In real use: this would hook into chat output and append to logs automatically

def log_event(project, content):
    path = f'projects/{project}/logs/today.md'
    with open(path, 'a', encoding='utf-8') as f:
        f.write(content + '\n')
