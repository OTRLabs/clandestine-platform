# Project Routes
PROJECT_INDEX: str = '/api/projects/'
PROJECT_DETAIL: str = '/api/projects/{project_id:uuid}/'  # More descriptive name

# Project Tasks Routes
PROJECT_TASKS: str = PROJECT_DETAIL + 'tasks/'
PROJECT_ADD_TASK: str = PROJECT_TASKS + 'add/'
PROJECT_TASK_DETAIL: str = PROJECT_TASKS + '{task_id:uuid}/'
PROJECT_TASK_UPDATE: str = PROJECT_TASK_DETAIL + 'update/'
PROJECT_TASK_DELETE: str = PROJECT_TASK_DETAIL + 'delete/'
PROJECT_TASK_ASSIGN: str = PROJECT_TASK_DETAIL + 'assign/'
PROJECT_TASK_REVOKE: str = PROJECT_TASK_DETAIL + 'revoke/'
PROJECT_TASK_COMMENTS: str = PROJECT_TASK_DETAIL + 'comments/'