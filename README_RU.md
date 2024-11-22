### [English](README.md)
### Исходный код телеграм бота [bl4ckm45k_vpn_bot](https://t.me/bl4ckm45k_vpn_bot "bl4ckm45k_vpn_bot")

`В целях безопасности и простоты настройки этот бот поддерживает только протоколы VLESS tcp или grpc
с автоматической генерацией приватных ключей и ShortID. 
Для более надежного шифрования всегда устанавливайте сертификаты TLS для протоколов VLESS, VMESS и Trojan.
`

### Если вам нужен бот для предоставления платного доступа: 
#### [Описание  платного бота](https://github.com/bl4ckm45k/vpnbot/blob/master/README_PAID_BOT_RU.md "Описание функционала платного бота")
#### [Писать в TG: pay4fallwall](https://pay4fallwall.t.me/ "pay4fallwall")


### Подготовка к запуску
- Клонируйте данный репозиторий
- Перейдите в папку с ботом
```pycon
cd vpnbot
```

Переименуйте файл `env.dist` в `.env` 
```pycon
cat env.dist > .env
```

Замените `BOT_TOKEN` на свой токен

В `ADMIN` укажите telegram user ID пользователя администратора.

Узнать свой user ID можно через бота [Get My ID bot](https://t.me/getmyid_bot "Get My ID bot")

Параметры `USE_WEBHOOK` и `False` не изменять, иначе бот не будет работать.

Остальные параметры не используются в опенсорс версии.

### Параметры Marzban
Для установки логина и пароля измените переменные `SUDO_USERNAME` и `SUDO_PASSWORD` в файле .env.marzban

### Запуск
```pycon
docker compose up --detach
```

Готово. Бот будет выдавать все ключи хостов из панели Marzban

### Панель Marzban будет работать на порту `8002`

