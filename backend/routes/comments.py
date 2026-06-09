from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional,Dict,Any
from services.store import add_comment,get_comments
router=APIRouter(prefix='/api/comments',tags=['comments'])
class CommentCreate(BaseModel):
    project_id:str; item_name:str; comment:str; position:Optional[Dict[str,Any]]=None
@router.post('/')
async def create_comment(payload:CommentCreate): return {'success':True,'comment':add_comment(payload.project_id,payload.model_dump())}
@router.get('/{project_id}')
async def list_comments(project_id:str): return get_comments(project_id)