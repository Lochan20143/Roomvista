import axios from 'axios';
export const API_BASE='http://localhost:8000';
export async function uploadModel(modelFile,name){const fd=new FormData();fd.append('model',modelFile);fd.append('name',name||'RoomVista Project');return (await axios.post(`${API_BASE}/api/projects/upload-model`,fd,{headers:{'Content-Type':'multipart/form-data'}})).data;}
export async function uploadImages(files,name){const fd=new FormData();files.forEach(f=>fd.append('files',f));fd.append('name',name||'Image Capture Project');return (await axios.post(`${API_BASE}/api/projects/upload-images`,fd,{headers:{'Content-Type':'multipart/form-data'}})).data;}
export async function getProject(id){return (await axios.get(`${API_BASE}/api/projects/${id}`)).data;}
export async function getProjects(){return (await axios.get(`${API_BASE}/api/projects/`)).data;}
export async function saveComment(payload){return (await axios.post(`${API_BASE}/api/comments/`,payload)).data;}
export async function getComments(id){return (await axios.get(`${API_BASE}/api/comments/${id}`)).data;}