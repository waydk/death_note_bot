from pathlib import Path

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("admins")
IP = env.str("ip")
DB_HOST = IP
PGUSER = env.str("PGUSER")
PGPASSWORD = env.str("PGPASSWORD")
DATABASE = env.str("DATABASE")

POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{DB_HOST}/{DATABASE}"

I18N_DOMAIN = 'death_note_bot'
BASE_DIR = Path(__file__).parent.parent.parent
LOCALES_DIR = BASE_DIR / 'locales'

