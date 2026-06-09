import React,{useState} from 'react';
import LandingPage from './pages/LandingPage.jsx';
import StudioPage from './pages/StudioPage.jsx';
export default function App(){const [projectId,setProjectId]=useState(null);return projectId?<StudioPage projectId={projectId} onBack={()=>setProjectId(null)}/>:<LandingPage onOpenProject={setProjectId}/>;}