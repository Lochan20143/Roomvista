from fastapi import APIRouter,UploadFile,File,Form
from typing import List
import os,uuid
from services.store import save_project,get_project,list_projects,now_iso
router=APIRouter(prefix='/api/projects',tags=['projects'])
BACKEND_URL='http://localhost:8000'
@router.post('/upload-model')
async def upload_model(model:UploadFile=File(...), name:str=Form('RoomVista Project')):
    ext=os.path.splitext(model.filename)[1].lower()
    if ext not in ['.glb','.gltf']:
        return {'success':False,'message':'Please upload a .glb or .gltf model exported from Polycam, RealityScan, Blender, or another scan tool.'}
    project_id=str(uuid.uuid4()); model_dir=f'storage/models/{project_id}'; os.makedirs(model_dir,exist_ok=True)
    filename='model'+ext; path=os.path.join(model_dir,filename)
    with open(path,'wb') as f: f.write(await model.read())
    project={'project_id':project_id,'name':name,'type':'uploaded_model','status':'ready','message':'3D model uploaded and ready.','created_at':now_iso(),'updated_at':now_iso(),'model_url':f'{BACKEND_URL}/models/{project_id}/{filename}','source_file':model.filename}
    save_project(project)
    return {'success':True,'project_id':project_id,'status':'ready','model_url':project['model_url']}
@router.post('/upload-images')
async def upload_images(files:List[UploadFile]=File(...), name:str=Form('Image Capture Project')):
    project_id=str(uuid.uuid4()); image_dir=f'storage/images/{project_id}'; os.makedirs(image_dir,exist_ok=True); saved=[]
    for file in files:
        safe=file.filename.replace(' ','_'); path=os.path.join(image_dir,safe)
        with open(path,'wb') as f: f.write(await file.read())
        saved.append(safe)
    project={'project_id':project_id,'name':name,'type':'image_set','status':'images_saved','message':'Images saved. Process them in Polycam/RealityScan and upload the exported GLB.','created_at':now_iso(),'updated_at':now_iso(),'model_url':None,'image_count':len(saved),'files':saved}
    save_project(project)
    return {'success':True,'project_id':project_id,'status':'images_saved','message':project['message']}
@router.get('/')
async def get_projects(): return list_projects()
@router.get('/{project_id}')
async def read_project(project_id:str):
    if project_id=='demo-room': return {'project_id':'demo-room','name':'Demo Living Room','type':'demo','status':'ready','message':'Demo room loaded.','model_url':None}
    p=get_project(project_id)
    return p if p else {'status':'not_found','message':'Project not found.'}