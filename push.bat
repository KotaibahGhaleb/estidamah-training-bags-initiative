@echo off
set "PATH=C:\Program Files\Git\cmd;%PATH%"
cd /d "D:\proramming project\Estidamah\Estidamah"
set /p MSG="Commit message: "
git add .
git -c user.name="KotaibahGhaleb" -c user.email="KotaibahGhaleb@users.noreply.github.com" commit -m "%MSG%"
git push
echo DONE=%ERRORLEVEL%
pause
