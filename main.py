from time import sleep
import admin
from library immport do_demons, eq, dailies, knighthood, claim_mail, coin_shopping, send_friends_coin, do_pvp, check_in, patrol, do_free_stages
if not admin.isUserAdmin():
    admin.runAsAdmin()

check_in()
sleep(1.5)
do_free_stages()
sleep(0.25)
do_demons()
sleep(0.25)
do_pvp()
sleep(0.25)
knighthood()
sleep(0.25)
patrol()
sleep(0.25)
send_friend_coin()
sleep(0.25)
claim_mail()
sleep(0.25)
coin_shopping()
sleep(0.25)
eq()
sleep(0.25)
dailies()
print("done")
