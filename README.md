### [Русский язык](README_RU.md)
### Recommended Hosting Providers

| Provider | Features | Link |
|---------|----------|------|
| **Veesp** | Mid-range price, fast, unlimited traffic, clean business IPs | [Visit](https://secure.veesp.com/?affid=1374) |
| **VDSka** | Cheap, fast, 3 TB traffic | [Visit](https://vdska.ru?p=21892) |
| **VDSina** | Expensive, fast, reliable — **10% Discount** | [Visit](https://www.vdsina.com/?partner=bv6a5sjwaj) |

### Source code of the Telegram bot [bl4ckm45k_vpn_bot](https://t.me/bl4ckm45k_vpn_bot "bl4ckm45k_vpn_bot")

`For security purposes and easy setup, this bot supports only VLESS tcp or grpc protocols with REALITY 
with automatic generation of private keys and ShortID. 
For more reliable encryption, always install TLS certificates for the VLESS, VMESS and Trojan protocols
`
### Setup
```bash
sudo apt update -y && sudo apt upgrade -y
sudo apt install git nano ufw curl cron -y
```

- Install docker 
```bash
sudo curl https://get.docker.com | sh
```
- Clone this repository
```bash
git clone https://github.com/bl4ckm45k/vpnbot.git
```

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
```bash
chmod +x update.sh
./update.sh
```
```

Done. The bot will output all host keys from the Marzban panel.

### The Marzban panel will be accessible on port `8002`
