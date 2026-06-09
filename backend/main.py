from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routes.projects import router as projects_router
from routes.comments import router as comments_router
import os
app=FastAPI(title='RoomVista Backend')
app.add_middleware(CORSMiddleware,allow_origins=['*'],allow_credentials=True,allow_methods=['*'],allow_headers=['*'])
for folder in ['storage/models','storage/images','storage/projects','storage/comments']:
    os.makedirs(folder,exist_ok=True)
app.mount('/models',StaticFiles(directory='storage/models'),name='models')
app.mount('/images',StaticFiles(directory='storage/images'),name='images')
app.include_router(projects_router)
app.include_router(comments_router)
@app.get('/')
async def root(): return {'message':'RoomVista FastAPI backend running','docs':'http://localhost:8000/docs'}