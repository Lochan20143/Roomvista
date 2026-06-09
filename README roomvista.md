# RoomVista AI — Working No-Docker Project

This version removes the failing Meshroom dependency and uses the reliable scan-app workflow.

## What works
- React landing page
- FastAPI backend
- Upload GLB/GLTF 3D room models
- Upload/store image sets
- Demo realistic room
- Three.js model viewer
- WASD walkthrough mode
- Mouse look
- Left-click to show item name
- Right-click to add comment
- Save comments locally
- Reopen projects
- Export current 3D view as PNG

## Recommended workflow
1. Capture the room using Polycam, RealityScan, Kiri Engine, or any scan app.
2. Export the scan as GLB or GLTF.
3. Upload that GLB/GLTF in RoomVista.
4. Open walkthrough mode.
5. Add comments and export images.

## Start backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

## Start frontend
```bash
cd frontend
npm install
npm run dev
```

Open: http://localhost:5173