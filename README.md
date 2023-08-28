# Arma3 Linux Server Tools
A package of tools i made for managing an Arma3 server on Linux.

If you have any questions, feel free to contact me or open an issue, although the support on this will be minimal.

# My server structure:

Everything is stored inside the home directory for the `steam` user.

- `Steam/` (directory for steam downloads (arma mods, etc))
- `arma3/` (directory containing arma3 dedicated server)
- `steamcmd/` (folder where steamcmd is installed)
- (all of the tools included here)

# Setup

### Create a `steam` user
```sh
useradd -m -s /bin/bash steam
sudo -i -u steam
```

### Download SteamCMD
```sh
mkdir ~/steamcmd && cd ~/steamcmd

sudo apt-get install lib32gcc-s1 # SteamCMD deps
curl -sqL "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" | tar zxvf -
```

### Download Arma3 dedicated server.
```sh
bash ~/steamcmd/steamcmd.sh
force_install_dir ./arma3/
login (user) (password)
app_update 233780 validate
exit
```

### Install mods
Install/update mods:
```sh
bash ~/steamcmd/steamcmd.sh
login (user) (password) # Account must own Arma3

# Do this for each mod:
workshop_download_item 107410 (modId) validate
# If the download timeouts, or errors, just repeat the command. It'll continue where it left off.
```

After installing/updating mods:
```sh
python ~/syncmods.py
```

Some info about syncmods.py:
- Creates a symlink between arma3 downloads, and the game dir
- Renames mod path's so that they work with linux
- Creates a mods.txt file and automatically passes it to run.sh (so that all the installed mods are loaded on startup)

### Run server:
```sh
bash ~/run.sh
```

### Kill server (if its not running in your current terminal)
```sh
ps -ef | grep steam # get the arma server pid from here
sudo kill (arma3server_x64 pid)
```