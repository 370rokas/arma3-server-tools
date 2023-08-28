#!/bin/bash

cd /home/steam/arma3/
./arma3server_x64 -config=server.cfg $(cat "mods/mods.txt")