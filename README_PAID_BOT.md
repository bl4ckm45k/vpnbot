### Telegram Bot Description
Contact in Telegram: [pay4fallwall](https://t.me/pay4fallwall)

**Cost:** $300 in crypto

- [Example of a working bot](https://t.me/Bl4ckm45k_cvb_bot).

#### Technology Stack:
- Docker
- Nginx
- - Certbot
- PostgreSQL
- Redis
- Marzban
- Python
- aiogram3
- FastAPI

#### Main Functionality:

1. **Bot interacts with Marzban panel based on Xray Core**
   - Supported protocols: Vless, Vmess, Trojan, Shadowsocks, Wireguard
   - Support 4 languages: English, Persian, Arabic, Russian

2. **Payment Systems:**
   - **YooMoney:** Directly in Telegram
   - **Aaio, LAVA:** Link or Telegram WebApp
   - **CryptoBot:** Payment via [CryptoBot](https://t.me/send)
   - **Cryptomus:** Link or Telegram WebApp
   - **Adding any other payment systems at your request** 

3. **Referral System:**
   - Setting the number of access days for the referrer and the invitee after the referral's payment.

4. **Additional Services:**
   - Subscription expiration check and notification.
   - Notification of key limit exhaustion.
   - Dynamic key generation, connection masking, Nginx and SSL certificate configuration.
   - Database access via SSH Port Forwarding.

5. **User Dashboard:**
   - Information about current accesses, duration, cost, location.
   - Menu with keys.
   - Change access location.

6. **Administrator Panel:**
   - Adding/removing servers.
   - Server replacement through the admin panel.
   - Tariff management, limits, message broadcasting, statistics.
   - Adding servers in one country with the minimum number of issued keys.

#### Additional Information:

- **GitHub and Docker** are used for launching and updates.
- Assistance in server, domain, bot setup, YooMoney agreement, Aaio setup. LAVA keys are provided by the manager.
- Planned enhancements and fixes/improvements to existing functionality are provided for free.
- Updates from private GitHub repository.
- To access administration functionality, provide your Telegram ID obtained via [@getmyid_bot](https://t.me/getmyid_bot).

#### YooMoney Test Payment Details:
- Card: 1111 1111 1111 1026
- Date: 12/22
- CVV: 000

**Note:** The test bot may lag due to simultaneous launching of multiple projects on the server.