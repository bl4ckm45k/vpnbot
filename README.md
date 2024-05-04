### [Русский язык](README_RU.md)
### Source code of the Telegram bot [bl4ckm45k_vpn_bot](https://t.me/bl4ckm45k_vpn_bot "bl4ckm45k_vpn_bot")

### If you need a bot for providing paid access:
#### [Description of the paid bot functionality](https://github.com/bl4ckm45k/vpnbot/blob/master/README_PAID_BOT.md "Description of the paid bot functionality")
#### [Contact on TG: pay4fallwall](https://pay4fallwall.t.me/ "pay4fallwall")

### Setup
- Clone this repository
- Navigate to the bot's directory
```bash
cd vpnbot
```

Rename the file `env.dist` to `.env`
```bash
cat env.dist > .env
```

Replace `BOT_TOKEN` with your token

In `ADMIN`, specify the Telegram user ID of the administrator.

You can find out your user ID through the [Get My ID bot](https://t.me/getmyid_bot "Get My ID bot")

Do not change the parameters `USE_WEBHOOK` and `False`, otherwise the bot will not work.

Other parameters are not used in the open-source version.

### Marzban Parameters
To set up the login and password, change the variables `SUDO_USERNAME` and `SUDO_PASSWORD` in the .env.marzban file.

### Launch
```bash
docker compose up --detach
```

Done. The bot will output all host keys from the Marzban panel.

### The Marzban panel will be accessible on port `8002`