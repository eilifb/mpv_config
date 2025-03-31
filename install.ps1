### Init                ###
mkdir script-opts
mkdir fonts

### ModernX             ###
New-Item -Path ./fonts/fluent-system-icons.ttf -ItemType HardLink -Value ./scripts/ModernX/fluent-system-icons.ttf

### Menu Plugin         ###
Invoke-WebRequest -Uri "https://github.com/tsl0922/mpv-menu-plugin/releases/download/2.4.1/menu.zip" -OutFile ./mpv-menu-plugin.zip
Expand-Archive -Path ./mpv-menu-plugin.zip -DestinationPath ./scripts -Force
Move-Item .\scripts\menu\ .\scripts\mpv-menu-plugin
Write-Output 'require("dyn_menu")' >> ./scripts/mpv-menu-plugin/main.lua
New-Item -Path ./scripts/menu.dll -ItemType HardLink -Value ./scripts/mpv-menu-plugin/menu.dll
Remove-Item -Path ./mpv-menu-plugin.zip -Force

### Thumbfast           ###
Copy-Item ./scripts/thumbfast ./script-opts/thumbfast.conf

### Open IMDb Page      ###
pip install guessit
pip install git+https://github.com/cinemagoer/cinemagoer

### Auto Deinterlace    ###
Invoke-WebRequest -Uri https://raw.githubusercontent.com/mpv-player/mpv/refs/heads/master/TOOLS/lua/autodeint.lua -Outfile ./scripts/autodeint.lua

### Auto Crop           ###
Invoke-WebRequest -Uri https://raw.githubusercontent.com/mpv-player/mpv/refs/heads/master/TOOLS/lua/autocrop.lua -Outfile ./scripts/autocrop.lua