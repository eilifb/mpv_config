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
7. [Open IMDb Page](https://github.com/eilifb/mpv-open-imdb-page)
8. [Open MAL Page](https://github.com/eilifb/mpv-open-mal-page) (WIP)

<a name="#inst" />

## Installation

### Setup
The files can either go directly into `C:\users\USERNAME\AppData\Roaming\mpv`
or into a directory named `portable_config` in your `mpv` install location
(e.g. `C:\Program Files\mpv\portable_config`)

```powershell
git clone --recurse-submodules -j8 https://github.com/eilifb/mpv_config
cd mpv_config
```
From here you can either set up each script manually as described below,
or you can run
```powershell
./install.ps1
```
You need configure some of the scripts`script-opts` configuration files regardless.


#### Script setup

* ModernX

    - `fonts/fluent-system-icons.ttf`
    - `script-opts/modernx.conf` (Optional)
    ```powershell
    New-Item -Path ../fonts/fluent-system-icons.ttf -ItemType HardLink -Value ./scripts/ModernX/fluent-system-icons.ttf
    ```

* Menu Plugin

    Needs to be downloaded seperately. The files can be placed in the main `scripts` folder or
    in a sub directory with a `main.lua` file. Exception is `menu.dll` which needs to be in the `scripts` folder.

    I chose to create a sub-directory and hard-link `menu.dll` (for some reason).
    ```powershell
    Invoke-WebRequest -Uri "https://github.com/tsl0922/mpv-menu-plugin/releases/download/2.4.1/menu.zip" -OutFile ./mpv-menu-plugin.zip
    Expand-Archive -Path ./mpv-menu-plugin.zip -DestinationPath ./scripts -Force
    mv .\scripts\menu\ .\scripts\mpv-menu-plugin
    echo 'require("dyn_menu")' >> ./scripts/mpv-menu-plugin/main.lua
    New-Item -Path ./scripts/menu.dll -ItemType HardLink -Value ./scripts/mpv-menu-plugin/menu.dll
    Remove-Item -Path ./mpv-menu-plugin.zip -Force
    ```

* Thumbfast

    - `script-opts/thumbfast.conf`

    I chose to copy over the example conf file.
    ```powershell
    cp ./scripts/thumbfast ./script-opts/thumbfast.conf
    ```

* Auto Sub

    - [subliminal Python package](https://pypi.org/project/subliminal/)
    - `script-opts/autosub.conf`
    ```powershell
    pip install subliminal
    ```

* Auto Sub Sync

    - `script-opts/autosubsync.conf`

* mpv-open-imdb-page

    - [GuessIt Python package](https://pypi.org/project/guessit/)
    ```powershell
    pip install guessit
    pip install git+https://github.com/cinemagoer/cinemagoer
    ```

* mpv-open-mal-page

    - [GuessIt Python package](https://pypi.org/project/guessit/)
    ```powershell
    pip install guessit
    pip install git+https://github.com/cinemagoer/cinemagoer
    ```

* Auto Deinterlace

    Has to be downloaded seperately.
    ```powershell
    Invoke-WebRequest -Uri https://raw.githubusercontent.com/mpv-player/mpv/refs/heads/master/TOOLS/lua/autodeint.lua -Outfile ./scripts/autodeint.lua
    ```


<a name="#todo" />

## TODO

- [ ] Vertify HDR profile quality
- [ ] Vertify audio downmixing settings
- [ ] Look into audio normalization
- [ ] Clean up `input.conf`
- [ ] Clean up `mpv.conf`
- [ ] OSX/Linux support
- [ ] Look into upscaling shaders
- [x] Write install script
- [x] Complete `mpv-open-mal-page`