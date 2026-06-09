import json
from pathlib import Path
from datetime import datetime
PROJECT_DIR=Path('storage/projects'); COMMENT_DIR=Path('storage/comments')
PROJECT_DIR.mkdir(parents=True,exist_ok=True); COMMENT_DIR.mkdir(parents=True,exist_ok=True)
def now_iso(): return datetime.utcnow().isoformat()+'Z'
def project_path(project_id): return PROJECT_DIR/f'{project_id}.json'
def comment_path(project_id): return COMMENT_DIR/f'{project_id}.json'
def save_project(project):
    project['updated_at']=now_iso()
    with open(project_path(project['project_id']),'w',encoding='utf-8') as f: json.dump(project,f,indent=2)
    return project
def get_project(project_id):
    p=project_path(project_id)
    if not p.exists(): return None
    return json.loads(p.read_text(encoding='utf-8'))
def list_projects():
    out=[]
    for p in PROJECT_DIR.glob('*.json'):
        out.append(json.loads(p.read_text(encoding='utf-8')))
    return sorted(out,key=lambda x:x.get('updated_at',''),reverse=True)
def add_comment(project_id,comment):
    p=comment_path(project_id); comments=[]
    if p.exists(): comments=json.loads(p.read_text(encoding='utf-8'))
    comment['created_at']=now_iso(); comments.append(comment)
    p.write_text(json.dumps(comments,indent=2),encoding='utf-8')
    return comment
def get_comments(project_id):
    p=comment_path(project_id)
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else []