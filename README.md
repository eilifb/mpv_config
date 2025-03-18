# MPV Config
## Index
1. [Scripts Used](#scripts)
3. [Installation](#inst)
2. [Todo](#todo)

<a name="#scripts" />

## Scripts Used
1. [ModernX](https://github.com/eilifb/ModernX)
2. [Menu Plugin](https://github.com/tsl0922/mpv-menu-plugin)
3. [Thumbfast](https://github.com/eilifb/thumbfast)
4. [Auto Sub](https://github.com/eilifb/mpv-autosub)
5. [Auto Sub Sync](https://github.com/Ajatt-Tools/autosubsync-mpv)
6. [Auto Deinterlace](https://github.com/mpv-player/mpv/blob/master/TOOLS/lua/autodeint.lua)
7. [Open IMDb](https://github.com/eilifb/mpv-open-imdb-page)
8. [Open MAL](https://github.com/eilifb/mpv-open-mal-page) (WIP)

<a name="#inst" />

## Installation

* Menu Plugin
    ```powershell
    Invoke-WebRequest -Uri "https://github.com/tsl0922/mpv-menu-plugin/releases/download/2.4.1/menu.zip" -OutFile ./mpv-menu-plugin.zip
    Expand-Archive -Path ./mpv-menu-plugin.zip -DestinationPath ./scripts -Force
    mv .\scripts\menu\ .\scripts\mpv-menu-plugin
    echo 'require("dyn_menu")' >> ./scripts/mpv-menu-plugin/main.lua
    New-Item -Path ./scripts/menu.dll -ItemType HardLink -Value ./scripts/mpv-menu-plugin/menu.dll
    Remove-Item -Path ./mpv-menu-plugin.zip -Force
    ```

* ModernX
    ```powershell
    New-Item -Path ../fonts/fluent-system-icons.ttf -ItemType HardLink -Value ./scripts/ModernX/fluent-system-icons.ttf
    ```

* Auto Sub
    ```powershell
    pip install subliminal
    ```

    Set up `script-opts/autosub.conf`

* Auto Sub Sync

    Set up `script-opts/autosubsync.conf`

* mpv-open-imdb-page
    ```powershell
    pip install guessit
    pip install git+https://github.com/cinemagoer/cinemagoer
    ```

* Auto Deinterlace
    ```powershell
    Invoke-WebRequest -Uri https://raw.githubusercontent.com/mpv-player/mpv/refs/heads/master/TOOLS/lua/autodeint.lua -Outfile ./scripts/autodeint.lua
    ```


<a name="#todo" />

## TODO

- [] Vertify HDR profile quality
- [] Vertify audio downmixing settings
- [] Look into audio normalization
- [] Clean up `input.conf`
. [] Clean up `mpv.conf`
- [] Look into upscaling shaders
- [] Write install script
- [] Complete `mpv-open-mal-page`