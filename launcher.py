import logging
import sys
import pkg_resources
import subprocess

logging.basicConfig(level=logging.INFO)

requirements = {}
installed = {pkg.key for pkg in pkg_resources.working_set}

with open('requirements.txt') as f:
    # noinspection PyRedeclaration
    requirements = set(f.read().splitlines())

missing = requirements - installed

if missing:
    logging.info(f"Missing required package: {', '.join(x for x in missing)} | Starting installation(s).")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])

import hoyolab_daily_reward

client = hoyolab_daily_reward.genshin_claim('accounts.json')
client()
