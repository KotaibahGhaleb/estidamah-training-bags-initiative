@echo off
set "PATH=C:\Program Files\Git\cmd;%PATH%"
cd /d "D:\proramming project\Estidamah\Estidamah"
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/KotaibahGhaleb/estidamah-training-bags-initiative.git
git push -u origin main
echo DONE=%ERRORLEVEL%
