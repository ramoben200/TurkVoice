from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Merhaba, Müzik asistanı hizmetidir.\n\n ❗️ kurallar:\n - Sohbete izin yok.\n - Bilgi ve Komutlarım için grup sohbetine **/bilgi** yazarsanız. komutlarımı ögrenebilirsiniz. \n - İstenmeyen postaya izin verilmez \n\n 🚨 **USERBOT GRUBUNUZA KATILAMAZSA GRUP DAVETI BAĞLANTISI VEYA KULLANICI ADI GÖNDER.**\n\n ⚠️ DİKKAT: Burada bir mesaj gönderiyorsanız Yöneticinin iletinizi göreceği anlamına gelir ve sohbete katılın\n - Bu kullanıcıyı gizli gruplara eklemeyin.\n   - Özel bilgileri burada paylaşmayınız. 📚 Bilgi için @BOT_RAMO\n\n")
  return                      
