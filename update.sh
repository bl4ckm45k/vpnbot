#!/bin/bash

# Останавливаем все контейнеры с образом custom_vpn_bot
docker ps -a | grep free_vpn_bot | awk '{print $1}' | xargs docker stop
# Удаляем все контейнеры с образом custom_vpn_bot
docker ps -a | grep free_vpn_bot | awk '{print $1}' | xargs docker rm
# Удаляем образ custom_vpn_bot
docker rmi free_vpn_bot
# Создаем новый образ custom_vpn_bot
docker build -t free_vpn_bot .
# docker ps -a | grep gozargah/marzban:latest | awk '{print $1}' | xargs docker stop
# Удаляем все контейнеры с образом custom_vpn_bot
# docker ps -a | grep gozargah/marzban:latest | awk '{print $1}' | xargs docker rm
# Выполним скрипт install.sh
./install.sh