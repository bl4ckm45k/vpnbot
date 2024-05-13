#!/bin/bash

# Останавливаем все контейнеры с образом free_vpn_bot
docker ps -a | grep free_vpn_bot | awk '{print $1}' | xargs docker stop
# Удаляем все контейнеры с образом free_vpn_bot
docker ps -a | grep free_vpn_bot | awk '{print $1}' | xargs docker rm
# Удаляем образ free_vpn_bot
docker rmi free_vpn_bot
# Создаем новый образ free_vpn_bot
docker build -t free_vpn_bot .
# Останавливаем и удаляем контейнер marzban
docker stop free_vpn_bot_marzban
docker rm free_vpn_bot_marzban
# Поднимаем контейнеры
docker compose up -d --remove-orphans