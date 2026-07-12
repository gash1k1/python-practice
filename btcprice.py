import requests 
from telegram.ext import ApplicationBuilder

token = '8717909976:AAGu4GcWTPFPvbCo_qrerC9d4dn-YWf_zPY'
CHANNEL = '@BTCpriceSaas'

async def send_price(context):
    response = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
    price = float(response.json()['price'])
    await context.bot.send_message(chat_id = CHANNEL, text = f'*$ {price:.2f}*', parse_mode = 'Markdown')

app = ApplicationBuilder().token(token).build()
app.job_queue.run_repeating(send_price, interval=60, first=0)
app.run_polling()