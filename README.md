Исходный код телеграм бота [Vincent_vpn_bot](https://t.me/vincent_vpn_bot "Vincent_vpn_bot")

### Инструкция [Установка Outline VPN на Ubuntu 20.04](https://gist.github.com/JohnyDeath/3f93899dc78f90cc57ae52b41ea29bac "Установка Outline VPN на Ubuntu 20.04")

Когда скрипт закончит, то выведет примерно такое содержимое.

```
{ 
  "apiUrl": "https://0.0.0.0:0000/XXXXXXXXXXXX", 
  "certSha256": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" 
}
```
При добавлении сервера в Outline Manager укажите его в пункте 2.

### Подготовка к запуску
Переименуйте файл `env.dist` в `.env` 

Замените `BOT_TOKEN` на свой токен

В `ADMIN` укажите telegram user ID пользователя администратора или список через запятую.
Узнать свой user ID можно через бота [Get My ID bot](https://t.me/getmyid_bot "Get My ID bot")

Параметры `DB`, кроме `DB_HOST`, на ваше усмотрение

### Запуск

`docker compose up --detach`

#### Для добавления и удаления серверов используйте команду `/admin`