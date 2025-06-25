### [English](README.md)
### Рекомендуемые хостеры

| Хостинг | Особенности | Ссылка |
|--------|-------------|--------|
| **Veesp** | Средний, быстрый, неограниченный трафик, чистые бизнесовые IP | [Перейти](https://secure.veesp.com/?affid=1374) |
| **VDSka** | Дешевый, быстрый, 3 ТБ трафика | [Перейти](https://vdska.ru?p=21892) |
| **VDSina** | Дорогой, быстрый, надёжный — **Скидка 10%** | [Перейти](https://www.vdsina.com/?partner=bv6a5sjwaj) |

### Исходный код телеграм бота [bl4ckm45k_vpn_bot](https://t.me/bl4ckm45k_vpn_bot "bl4ckm45k_vpn_bot")

`В целях безопасности и простоты настройки этот бот поддерживает только протоколы VLESS tcp или grpc
с автоматической генерацией приватных ключей и ShortID. 
Для более надежного шифрования всегда устанавливайте сертификаты TLS для протоколов VLESS, VMESS и Trojan.
`

### Подготовка к запуску
```bash
sudo apt update -y && sudo apt upgrade -y
sudo apt install git nano ufw curl cron -y
```
- Установите Docker
```bash
sudo curl https://get.docker.com | sh
```
- Клонируйте данный репозиторий
```bash
git clone https://github.com/bl4ckm45k/vpnbot.git
```
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
```bash
chmod +x update.sh
./update.sh
```

Готово. Бот будет выдавать все ключи хостов из панели Marzban

### Панель Marzban будет работать на порту `8002`

