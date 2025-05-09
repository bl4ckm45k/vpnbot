### Описание бота для Telegram
[Telegram канал с историей разработки](https://t.me/cvb_poject)

Писать в ТГ  [pay4fallwall](https://t.me/pay4fallwall)

**Стоимость:** 
- 20,000₽ / USDT По курсу - [Цена по запросу](https://t.me/pay4fallwall)

- [Пример работающего бота](https://t.me/Bl4ckm45k_cvb_bot).

#### Стэк технологий:
- Docker
- Nginx
- - Certbot
- PostgreSQL
- Redis
- Marzban
- Python
- aiogram3
- FastAPI

#### Основной функционал:

1. **Бот взаимодействует с панелью Marzban на базе Xray Core**
   - Поддерживаемые протоколы: Vless, Vmess, Trjoan, Shadowsocks, Wireguard

2. **Платежные системы:**
   - **ЮКасса:** Прямо в Телеграм
   - **Aaio, LAVA:** Ссылка или Telegram WebApp
   - **CryptoBot** Оплата переходом в [CryptoBot](https://t.me/send)
   - **Cryptomus:** Ссылка или Telegram WebApp
   - **Добавление платежной системы по запросу** 
   
3. **Реферальная система:**
   - Настройка количества дней доступа для пригласившего и приглашенного после оплаты рефералом.

4. **Отдельные сервисы:**
   - Проверка и оповещение о сроках подписки.
   - Оповещение об исчерпании лимита ключей.
   - Генерация динамических ключей, маскировка подключения, настройка Nginx и SSL сертификатов.
   - Доступ к БД через SSH Port Forwarding.

5. **Личный кабинет пользователя:**
   - Информация о текущих доступах, срок, стоимость, локация.
   - Меню с ключами.
   - Изменение локации доступа.

6. **Панель администратора:**
   - Добавление/удаление серверов.
   - Замена сервера через админ-панель.
   - Управление тарифами, лимитами, рассылка сообщений, статистика.
   - Добавление серверов в одной стране с минимальным количеством выданных ключей.



#### Дополнительная информация:

- **GitHub и Docker** используются для запуска и обновлений.
- Помощь в настройке сервера, домена, бота, договора ЮКассы, настройка Aaio. Ключи LAVA предоставляются менеджером.
- Планируемые доработки и исправления/улучшения существующего функционала предоставляются бесплатно.
- Обновления из приватного репозитория GitHub.
- Для доступа к функционалу администрации сообщите свой Telegram ID узнав через [@getmyid_bot](https://t.me/getmyid_bot).

#### Тестовые платежные данные ЮКассы:
- Карта: 1111 1111 1111 1026
- Дата: 12/22
- CVV: 000

**Примечание:** Тестовый бот может лагать из-за одновременного запуска нескольких проектов на сервере.
****
