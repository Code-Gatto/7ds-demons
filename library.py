from windowcapture import WindowCapture
from vision import Vision
from time import time, sleep
import cv2 as cv
import admin
import threading
import pyautogui as ag


def click_im(rectangles, im):
    (gx, gy) = wincap.get_game_position()
    (x, y) = im.get_click_point(rectangles)
    (x, y) = ((x + gx), (y + gy))
    wincap.click(x, y)

def sleep_and_click(sec, im, confidence=0.6):
    sleep(sec)
    global screenshot
    rectangles = im.find(screenshot, confidence)
    if rectangles.size != 0:
        click_im(rectangles, im)

def double_press(key):
    sleep(2)
    ag.press(key)
    sleep(1.5)
    ag.press(key)

wincap = WindowCapture('The Seven Deadly Sins: Grand Cross')

def check_in():
    if True:
        checkin = Vision('Screenshots/check_in/check in.jpg')
        check_in_reward = Vision('Screenshots/check_in/check_in_reward.jpg')
        close_chat = Vision('Screenshots/check_in/close_chat.jpg')
        open_chat = Vision('Screenshots/check_in/open_chat.jpg')
        dont_open = Vision('Screenshots/check_in/no chat noti.jpg')
        green_ok = Vision('Screenshots/green_ok.jpg')
        green_chonk_ok = Vision('Screenshots/green_chonk_ok.jpg')
        shopup = Vision('Screenshots/shopup.jpg')
        no_reward = Vision('Screenshots/check_in/already checked in.jpg')
        log_ins = Vision ('Screenshots/log in rewards/orange_ok.jpg')
    last_clicked = None
    clicked = False
    global screenshot
    loop_time = time()
    thread_time = 0
    while True:
        sleep(0.05)
        screenshot = wincap.get_screenshot()
        cv.imshow('Matches', screenshot)
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break
        if (time() - loop_time) >= (thread_time + 2):
            # check for green ok
            if clicked == False:
                rectangles = green_ok.find(screenshot, 0.7)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), green_ok, 0.7])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = green_ok
                    print("k")
                rectangles = green_chonk_ok.find(screenshot, 0.7)
                if rectangles.size != 0 and clicked == False:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), green_chonk_ok, 0.7])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = green_ok
                    print("k")
                rectangles = log_ins.find(screenshot, 0.85)
                if rectangles.size != 0 and clicked == False:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), green_chonk_ok, 0.85])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = green_ok
                    print("k")
            # check for pop up shop
            if clicked == False:
                rectangles = shopup.find(screenshot, 0.8)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), shopup, 0.8])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = shopup
                    print("pop up shop wow!!")
            #open chat
            if clicked == False and (last_clicked == None or last_clicked == close_chat or last_clicked == shopup or last_clicked == green_ok or (last_clicked == open_chat and (time() - loop_time) >= 45)):
                rectangles = open_chat.find(screenshot, 0.85)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), open_chat, 0.8])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = open_chat
                    print("opening chat")
                rectangles = dont_open.find(screenshot, 0.85)
                if rectangles.size != 0:
                    loop_time = time()
                    print("no chat noti")
                    break
            #check in
            if clicked == False and (last_clicked == open_chat or (last_clicked == checkin and (time() - loop_time) >= 45)):
                rectangles = checkin.find(screenshot, 0.85)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), checkin, 0.8])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = checkin
                    print("checking in")
                if (time() - loop_time) >=15:
                    print("already checked in today")
                    break
            if clicked == False and (last_clicked == open_chat or (last_clicked == no_reward and (time() - loop_time) >= 45)):
                rectangles = no_reward.find(screenshot, 0.85)
                if rectangles.size != 0:
                    loop_time = time()
                    last_clicked = check_in_reward
                    print("there was no reward")
                    clicked = True
            #check in rewards
            if clicked == False and (last_clicked == None or last_clicked == checkin or (last_clicked == check_in_reward and (time() - loop_time) >= 45)):
                rectangles = check_in_reward.find(screenshot, 0.85)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), check_in_reward, 0.8])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = check_in_reward
                    print("got rewards")
            #close chat
            if clicked == False and (last_clicked == None or last_clicked == check_in_reward or last_clicked == shopup or last_clicked == green_ok or (last_clicked == close_chat and (time() - loop_time) >= 45) or (open_chat == close_chat and (time() - loop_time) >= 45)):
                rectangles = close_chat.find(screenshot, 0.85)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), close_chat, 0.8])
                    t.start()
                    clicked = True
                    loop_time = time()
                    print("closing chat")
                    if last_clicked == check_in_reward:
                        break
                    last_clicked = close_chat
            if (time() -  loop_time) >= 20:
                last_clicked == check_in_reward
            clicked = False

def knighthood():
    if True:
        k = Vision('Screenshots/pvp/another_green.jpg')
        shopup = Vision('Screenshots/shopup.jpg')
        battle_menu = Vision('Screenshots/battle_menu.jpg')
        knighthood = Vision('Screenshots/knighthood/knighthood.jpg')
        diff = Vision('Screenshots/knighthood/diff.jpg')
        start = Vision('Screenshots/knighthood/start!.jpg')
        pause = Vision('Screenshots/knighthood/pause.jpg')
        ff = Vision('Screenshots/knighthood/ff.jpg')
    global screenshot
    last_clicked = None
    loop_time = time()
    done = False
    thread_time = 0
    clicked = False
    while True:
        if (today := datetime.date.today().weekday()) != 3 and (today := datetime.date.today().weekday() != 4):
            break
        screenshot = wincap.get_screenshot()
        cv.imshow('Matches', screenshot)
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break
        if (time() - loop_time) >= (thread_time + 1):
            #green ok
            if clicked == False and (last_clicked == None or last_clicked == ff or last_clicked == shopup or (last_clicked == k and (time() - loop_time) >= 5)):
                rectangles = k.find(screenshot, 0.9)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), k, 0.9])
                    t.start()
                    clicked = True
                    loop_time = time()
                    print("k")
                    if last_clicked == ff:
                        done = True
                    last_clicked = k
            #pop up shop
            if clicked == False and (last_clicked == None or last_clicked == k or (last_clicked == shopup and (time() - loop_time) >= 5)):
                rectangles = shopup.find(screenshot, 0.8)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 0.5), shopup, 0.8])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = shopup
                    print("pop up shop wow!!")
            #battle menu
            if clicked == False and (last_clicked == None or last_clicked == shopup or (last_clicked == k and (time() - loop_time >= 13)) or (last_clicked == battle_menu and (time() - loop_time) >= 10)):
                rectangles = battle_menu.find(screenshot, 0.65)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 2), battle_menu, 0.65])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = battle_menu
                    print("clicking battle menu")
            #knighthood boss menu
            if clicked == False and (last_clicked == None or last_clicked == battle_menu or (last_clicked == knighthood and (time() - loop_time) >= 10)):
                rectangles = knighthood.find(screenshot, 0.8)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), knighthood, 0.8])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = knighthood
                    print("knighthood")
            #GB difficulty
            if clicked == False and (last_clicked == None or last_clicked == knighthood or last_clicked == k or (last_clicked == diff and (time() - loop_time) >= 10)):
                rectangles = diff.find(screenshot, 0.7)
                if rectangles.size != 0:
                    if done == True:
                        t = threading.Thread(target=double_press, args=[('esc',)])
                        t.start()
                        print("leaving gb menu")
                        t.join()
                        break
                    else:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), diff, 0.7])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = diff
                        print("diff")
            #start
            if clicked == False and (last_clicked == None or last_clicked == diff or (last_clicked == start and (time() - loop_time) >= 10)):
                rectangles = start.find(screenshot, 0.8)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), start, 0.8])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = start
                    print("start")
            #pause menu
            if clicked == False and (last_clicked == None or last_clicked == start or (last_clicked == pause and (time() - loop_time) >= 10)):
                rectangles = pause.find(screenshot, 0.8)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), pause, 0.8])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = pause
                    print("pause")
            #ff
            if clicked == False and (last_clicked == None or last_clicked == pause or (last_clicked == ff and (time() - loop_time) >= 10)):
                rectangles = ff.find(screenshot, 0.8)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), ff, 0.8])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = ff
                    print("ff")
            #undo click
            if clicked == True:
                clicked = False
        if (time() - loop_time) >= 30:
            last_clicked = None
            loop_time = time()

def send_friend_coin():
    if True:
        green_ok = Vision('Screenshots/green_ok.jpg')
        green_chonk_ok = Vision('Screenshots/green_chonk_ok.jpg')
        shopup = Vision('Screenshots/shopup.jpg')
        menu = Vision('Screenshots/menu.jpg')
        friends_tab = Vision('Screenshots/friend_coin/friends.jpg')
        send_coin = Vision('Screenshots/friend_coin/send_all.jpg')
        sendnt_coin = Vision('Screenshots/friend_coin/sendnt.jpg')
    global screenshot
    last_clicked = None
    loop_time = time()
    thread_time = 0
    clicked = False
    while True:
        screenshot = wincap.get_screenshot()
        cv.imshow('Matches', screenshot)
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break
        if (time() - loop_time) >= thread_time:
            # check for green ok
            if clicked == False and (last_clicked == None or last_clicked == send_coin or last_clicked == shopup or (last_clicked == green_ok and (time() - loop_time) >= 5)):
                rectangles = green_ok.find(screenshot, 0.7)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), green_ok, 0.7])
                    t.start()
                    loop_time = time()
                    if last_clicked == send_coin:
                        break
                    last_clicked = green_ok
                    print("k")
                rectangles = green_chonk_ok.find(screenshot, 0.7)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), green_chonk_ok, 0.7])
                    t.start()
                    loop_time = time()
                    if last_clicked == send_coin:
                        break
                    last_clicked = green_ok
                    print("k")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            # check for pop up shop
            if clicked == False and (last_clicked == None or last_clicked == green_ok or (last_clicked == shopup and (time() - loop_time) >= 5)):
                rectangles = shopup.find(screenshot, 0.8)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), shopup, 0.8])
                    t.start()
                    loop_time = time()
                    last_clicked = shopup
                    print("pop up shop wow!!")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            # go to menu
            if clicked == False and (last_clicked == None or last_clicked == green_ok or last_clicked == shopup or (last_clicked == menu and (time() - loop_time) >= 5)):
                rectangles = menu.find(screenshot, 0.8)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), menu, 0.8])
                    t.start()
                    loop_time = time()
                    last_clicked = menu
                    print("menu tab")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            #go to friends tab
            if clicked == False and (last_clicked == None or last_clicked == menu or (last_clicked == friends_tab and (time() - loop_time) >= 5)):
                rectangles = friends_tab.find(screenshot, 0.75)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), friends_tab, 0.75])
                    t.start()
                    loop_time = time()
                    last_clicked = friends_tab
                    while (time() - loop_time) <= 6:
                        screenshot = wincap.get_screenshot()
                        cv.imshow('Matches', screenshot)
                        if cv.waitKey(1) == ord('q'):
                            cv.destroyAllWindows()
                            break
                    print("friends tab")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            #send the coins
            if clicked == False and (last_clicked == None or last_clicked == friends_tab or (last_clicked == send_coin and (time() - loop_time) >= 5)):
                rectangles = send_coin.find(screenshot, 0.9)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), send_coin, 0.9])
                    t.start()
                    loop_time = time()
                    last_clicked = send_coin
                    print("send the coin")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            #sent the coin
            if clicked == False and (last_clicked == None or last_clicked == friends_tab or (last_clicked == sendnt_coin and (time() - loop_time) >= 5)):
                rectangles = sendnt_coin.find(screenshot, 0.85)
                if rectangles.size != 0:
                    print("sent the coin already")
                    t = threading.Thread(target=press_once, args=['esc',])
                    t.start()
                    while (time() - loop_time) <= 10:
                        screenshot = wincap.get_screenshot()
                        cv.imshow('Matches', screenshot)
                        if cv.waitKey(1) == ord('q'):
                            cv.destroyAllWindows()
                            break
                    break
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break

def do_pvp():
    if True:
        green_ok = Vision('Screenshots/green_ok.jpg')
        green_chonk_ok = Vision('Screenshots/green_chonk_ok.jpg')
        shopup = Vision('Screenshots/shopup.jpg')
        battle_menu = Vision('Screenshots/battle_menu.jpg')
        elite = Vision('Screenshots/pvp/elite.jpg')
        normal = Vision('Screenshots/pvp/normal.jpg')
        pvp_tab = Vision('Screenshots/pvp/pvp_tab.jpg')
        normal_pvp = Vision('Screenshots/pvp/normal_pvp.jpg')
        pvp_menu = Vision('Screenshots/pvp/pvp_menu.jpg')
        search = Vision('Screenshots/pvp/search.jpg')
        again = Vision('Screenshots/pvp/again.jpg')
        blue_ok = Vision('Screenshots/blue_ok.jpg')
        chonk_ok = Vision('Screenshots/chonk_ok.jpg')
        view_results = Vision('Screenshots/pvp/view_results.jpg')
        join_all = Vision('Screenshots/pvp/join_all.jpg')
    global screenshot
    last_clicked = None
    loop_time = time()
    done_pvp = 0
    q = True
    thread_time = 0
    done_with_pvp = None
    clicked = False
    while True:
        while True:
            screenshot = wincap.get_screenshot()
            cv.imshow('Matches', screenshot)
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                q = False
                break
            if (time() - loop_time) >= (thread_time + 2):
                # check for green ok
                if clicked == False and (last_clicked == None or last_clicked == elite or last_clicked == pvp_tab or last_clicked == shopup or last_clicked == join_all or (last_clicked == green_ok and (time() - loop_time) >= 5)):
                    rectangles = green_ok.find(screenshot, 0.7)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), green_ok, 0.7])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = green_ok
                        print("k")
                    rectangles = green_chonk_ok.find(screenshot, 0.7)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), green_chonk_ok, 0.7])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = green_ok
                        print("k")
                # check for pop up shop
                if clicked == False and (last_clicked == None or last_clicked == green_ok or (last_clicked == shopup and (time() - loop_time) >= 5)):
                    rectangles = shopup.find(screenshot, 0.8)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), shopup, 0.8])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = shopup
                        print("pop up shop wow!!")
                # go to battle menu
                if clicked == False and (last_clicked == None or last_clicked == shopup or (last_clicked == green_ok and (time() - loop_time >= 30)) or (last_clicked == battle_menu and (time() - loop_time) >= 20)):
                    rectangles = battle_menu.find(screenshot, 0.65)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 3), battle_menu, 0.65])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = battle_menu
                        print("clicking battle menu")
                # go to pvp_tab
                if clicked == False and (last_clicked == None or last_clicked == battle_menu or (last_clicked == pvp_tab and (time() - loop_time) >= 20)):
                    rectangles = pvp_tab.find(screenshot, 0.8)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 3), pvp_tab, 0.8])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = pvp_tab
                        print("pvp tab")
                # monday claiming pvp
                if clicked == False and (last_clicked == None or last_clicked == green_ok or last_clicked == pvp_tab or (last_clicked == view_results and (time() - loop_time) >= 20)):
                    rectangles = view_results.find(screenshot, 0.8)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), view_results, 0.8])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = view_results
                        print("view results")
                if clicked == False and (last_clicked == None or last_clicked == green_ok or last_clicked == view_results or last_clicked == pvp_tab or (last_clicked == join_all and (time() - loop_time) >= 20)):
                    rectangles = join_all.find(screenshot, 0.8)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), join_all, 0.8])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = join_all
                        print("join all")
                # press esc when we are in elite pvp menu
                if clicked == False and (last_clicked == None or last_clicked == green_ok or last_clicked == pvp_tab or (last_clicked == elite and (time() - loop_time) >= 20)):
                    rectangles = elite.find(screenshot, 0.85)
                    if rectangles.size != 0:
                        t = threading.Thread(target=press_once, args=['esc',])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = elite
                        print("left elite pvp menu")
                        break

                clicked = False
        clicked = False
        if q == False:
            break
        # going to normal pvp
        while True:
            screenshot = wincap.get_screenshot()
            cv.imshow('Matches', screenshot)
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                q = False
                break
            if (time() - loop_time) >= (thread_time + 1):
                # check for green ok
                if clicked == False and (last_clicked == None or last_clicked == elite or last_clicked == pvp_tab or last_clicked == shopup or (last_clicked == green_ok and (time() - loop_time) >= 5)):
                    rectangles = green_ok.find(screenshot, 0.7)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), green_ok, 0.7])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = green_ok
                        print("k")
                    rectangles = green_chonk_ok.find(screenshot, 0.7)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), green_chonk_ok, 0.7])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = green_ok
                        print("k")
                # check for pop up shop
                if clicked == False and (last_clicked == None or last_clicked == green_ok or (last_clicked == shopup and (time() - loop_time) >= 5)):
                    rectangles = shopup.find(screenshot, 0.8)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), shopup, 0.8])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = shopup
                        print("pop up shop wow!!")
                #entering pvp menu
                if clicked == False and (last_clicked == None or last_clicked == elite or (last_clicked == pvp_menu and (time() - loop_time) >= 20)):
                    rectangles = pvp_menu.find(screenshot, 0.8)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), pvp_menu, 0.8])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = pvp_menu
                        print("pvp menu")
                #going to normal pvp
                if clicked == False and (last_clicked == None or last_clicked == pvp_menu or (last_clicked == normal_pvp and (time() - loop_time) >= 20)):
                    rectangles = normal_pvp.find(screenshot, 0.8)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), normal_pvp, 0.8])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = normal_pvp
                        print("entering normal")
                #going to normal pvp
                if clicked == False and (last_clicked == None or last_clicked == normal_pvp or (last_clicked == normal and (time() - loop_time) >= 20)):
                    rectangles = normal.find(screenshot, 0.7)
                    if rectangles.size != 0:
                        loop_time = time()
                        last_clicked = normal
                        print("we're indeed in normal pvp")
                #searching for a match
                if clicked == False and (last_clicked == None or last_clicked == normal or (last_clicked == search and (time() - loop_time) >= 20)):
                    rectangles = search.find(screenshot, 0.8)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), search, 0.8])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = search
                        print("searching for a match")
                        break
                clicked = False
        clicked = False
        if q == False:
            break
        #in pvp
        while True:
            screenshot = wincap.get_screenshot()
            cv.imshow('Matches', screenshot)
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                q = False
                break
            if (time() - loop_time) >= (thread_time + 2):
                #if it's sunday and we did less than 3 pvp do it again
                if clicked == False and (datetime.date.today().weekday() == 6) and (last_clicked == None or last_clicked == search or last_clicked == again or last_clicked == blue_ok) and (done_pvp < 2):
                    rectangles = again.find(screenshot, 0.65)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), again, 0.65])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = again
                        print("again")
                        done_pvp += 1
                #are we done with pvp today?
                if clicked == False and ((datetime.date.today().weekday() != 6 and (last_clicked == None or last_clicked == search or last_clicked == again or last_clicked == blue_ok)) or done_pvp >= 2):
                    rectangles = again.find(screenshot, 0.65)
                    if rectangles.size != 0:
                        break
                # check for blue ok
                if clicked == False:
                    rectangles = blue_ok.find(screenshot, 0.85)
                    if clicked == False and rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click,args=[(thread_time := 1.5), blue_ok, 0.65])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = blue_ok
                        print("k but blue")
                    rectangles = chonk_ok.find(screenshot, 0.85)
                    if clicked == False and rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click,args=[(thread_time := 1.5), chonk_ok, 0.65])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = blue_ok
                        print("k but blue")
                clicked = False
        clicked = False
        if q == False:
            break
        #make sure we left pvp
        while True:
            q = False
            screenshot = wincap.get_screenshot()
            rectangles = battle_menu.find(screenshot, 0.65)
            output_im = battle_menu.draw_rectangles(screenshot, rectangles)
            cv.imshow('Matches', output_im)
            if clicked == False and (rectangles.size == 0 and (time() - loop_time) >= 5):
                t = threading.Thread(target=press_once, args=['esc',])
                t.start()
                clicked = True
                loop_time = time()
                print("esc")
            if clicked == False and (rectangles.size != 0 and (time() - loop_time) >= 5):
                break
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                q = False
                break
            clicked = False
        break


def patrol():
    if True:
        battle_menu = Vision('Screenshots/battle_menu.jpg')
        reward = Vision('Screenshots/reward.jpg')
        shopup = Vision('Screenshots/shopup.jpg')
        green_ok = Vision('Screenshots/green_ok.jpg')
        green_chonk_ok = Vision('Screenshots/green_chonk_ok.jpg')
        complete = Vision('Screenshots/patrol/complete.jpg')
        dispatched = Vision('Screenshots/patrol/dispatched.jpg')
        gold = Vision('Screenshots/patrol/gold.jpg')
        patrol_all = Vision('Screenshots/patrol/patrol_all.jpg')
        patrol_tab = Vision('Screenshots/patrol/patrol_tab.jpg')
        receive = Vision('Screenshots/patrol/receive.jpg')
        select_reward = Vision('Screenshots/patrol/select_reward.jpg')
        set_all = Vision('Screenshots/patrol/set_all.jpg')
        setnt_all = Vision('Screenshots/patrol/setnt_all.jpg')
        header = Vision('Screenshots/patrol/patrol_header.jpg')
        completent = Vision('Screenshots/patrol/nothing to complete.jpg')
    global screenshot
    last_clicked = None
    q = True
    loop_time = time()
    thread_time = 0
    clicked = False
    while q == True:
        #entering patrol tab
        while True:
            screenshot = wincap.get_screenshot()
            cv.imshow('Matches', screenshot)
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                q = True
                break
            if (time() - loop_time) >= (thread_time + 2):
                # check for green ok
                if clicked == False and (last_clicked == None or last_clicked == shopup or last_clicked == battle_menu or (last_clicked == green_ok and (time() - loop_time) >= 7)):
                    rectangles = green_ok.find(screenshot, 0.7)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 3), green_ok, 0.7])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = green_ok
                        print("k")
                    rectangles = green_chonk_ok.find(screenshot, 0.7)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 3), green_chonk_ok, 0.7])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = green_ok
                        print("k")
                    if cv.waitKey(1) == ord('q'):
                        cv.destroyAllWindows()
                        q = False
                        break
                # check for pop up shop
                if clicked == False and (last_clicked == None or last_clicked == battle_menu or last_clicked == green_ok or (last_clicked == shopup and (time() - loop_time) >= 5)):
                    rectangles = shopup.find(screenshot, 0.8)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 3), shopup, 0.8])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = shopup
                        print("pop up shop wow!!")
                    if cv.waitKey(1) == ord('q'):
                        cv.destroyAllWindows()
                        q = False
                        break
                # check for battle menu
                if clicked == False and (last_clicked == None or last_clicked == shopup or last_clicked == green_ok or (last_clicked == battle_menu and (time() - loop_time) >= 20)):
                    rectangles = battle_menu.find(screenshot, 0.65)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 3), battle_menu, 0.65])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = battle_menu
                        print("clicking battle menu")
                    if cv.waitKey(1) == ord('q'):
                        cv.destroyAllWindows()
                        q = False
                        break
                #patrol tab
                if clicked == False and (last_clicked == None or last_clicked == battle_menu or (last_clicked == patrol_tab and (time() - loop_time) >= 5)):
                    rectangles = patrol_tab.find(screenshot, 0.8)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), patrol_tab, 0.8])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = patrol_tab
                        print("entering patrol tab")
                    if cv.waitKey(1) == ord('q'):
                        cv.destroyAllWindows()
                        q = False
                        break
                if clicked == False and (last_clicked == None or last_clicked == patrol_tab):
                    rectangles = header.find(screenshot, 0.8)
                    if rectangles.size != 0:
                        loop_time = time()
                        last_clicked = patrol_tab
                        print("we're in the patrol tab")
                        break
                #times up
                if (time() - loop_time) >= 30:
                    last_clicked = None
                    loop_time = time()
                clicked = False
        #claiming patrols
        clicked = False
        if q == False:
            break
        while True:
            screenshot = wincap.get_screenshot()
            cv.imshow('Matches', screenshot)
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                q = True
                break
            if (time() - loop_time) >= (thread_time + 2):
                #is there patrol to claim
                if clicked == False and (last_clicked == patrol_tab or (last_clicked == complete and (time() - loop_time) >= 30)):
                    rectangles = complete.find(screenshot, 0.95)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), complete, 0.9])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = complete
                        print("claim all patrols")
                    rectangles = completent.find(screenshot, 0.97)
                    if rectangles.size != 0:
                        print("there was no patrol to claim")
                        loop_time = time()
                        last_clicked = complete
                        break
                    if cv.waitKey(1) == ord('q'):
                        cv.destroyAllWindows()
                        q = False
                        break
                #rewards button
                if clicked == False and (last_clicked == None or last_clicked == complete or (last_clicked == reward and (time() - loop_time) >= 5)):
                    rectangles = reward.find(screenshot, 0.85)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), reward, 0.85])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = reward
                        print("saw rewards")
                        break
                    if cv.waitKey(1) == ord('q'):
                        cv.destroyAllWindows()
                        q = False
                        break
                #times up
                if (time() - loop_time) >= 30:
                    last_clicked = None
                    loop_time = time()
                clicked = False
        clicked = False
        if q == False:
            break
        #setting patrols
        while True:
            screenshot = wincap.get_screenshot()
            cv.imshow('Matches', screenshot)
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                q = True
                break
            if (time() - loop_time) >= (thread_time + 2):
                #start next patrols
                if clicked == False and (last_clicked == None or last_clicked == reward or last_clicked == patrol_tab or last_clicked == complete or (last_clicked == set_all and (time() - loop_time) >= 30)):
                    rectangles = set_all.find(screenshot, 0.97)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), set_all, 0.9])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = set_all
                        print("set all")
                    rectangles = setnt_all.find(screenshot, 0.97)
                    if rectangles.size != 0:
                        loop_time = time()
                        last_clicked = set_all
                        print("nothing to set")
                        break
                    if cv.waitKey(1) == ord('q'):
                        cv.destroyAllWindows()
                        q = False
                        break
                #patrol all
                if clicked == False and (last_clicked == None or last_clicked == set_all or last_clicked == patrol_tab or (last_clicked == patrol_all and (time() - loop_time) >= 20)):
                    rectangles = patrol_all.find(screenshot, 0.8)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), patrol_all, 0.8])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = patrol_all
                        print("sent patrols")
                    if cv.waitKey(1) == ord('q'):
                        cv.destroyAllWindows()
                        q = False
                        break
                #patrols have been dispatched
                if clicked == False and (last_clicked == None or last_clicked == patrol_all or (last_clicked == dispatched and (time() - loop_time) >= 5)):
                    rectangles = dispatched.find(screenshot, 0.75)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), dispatched, 0.68])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = dispatched
                        print("yep sent patrols")
                        break
                    if cv.waitKey(1) == ord('q'):
                        cv.destroyAllWindows()
                        q = False
                        break
                clicked = False
        clicked = False
        if q == False:
            break
        #claim the patrol gold
        while True:
            screenshot = wincap.get_screenshot()
            cv.imshow('Matches', screenshot)
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                q = True
                break
            if (time() - loop_time) >= (thread_time + 2):
                #select reward menu
                if clicked == False and (last_clicked == None or last_clicked == dispatched or last_clicked == set_all or (last_clicked == select_reward and (time() - loop_time) >= 5)):
                    rectangles = select_reward.find(screenshot, 0.95)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 2), select_reward, 0.9])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = select_reward
                        print("select reward")
                    if rectangles.size == 0:
                        print("no reward selection yet")
                        last_clicked = reward
                    if cv.waitKey(1) == ord('q'):
                        cv.destroyAllWindows()
                        q = False
                        break
                #select gold
                if clicked == False and (last_clicked == None or last_clicked == select_reward or (last_clicked == receive and (time() - loop_time) >= 10) or (last_clicked == gold and (time() - loop_time) >= 5)):
                    rectangles = gold.find(screenshot, 0.85)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), gold, 0.85])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = gold
                        print("pick gold")
                    if cv.waitKey(1) == ord('q'):
                        cv.destroyAllWindows()
                        q = False
                        break
                #receive the gold
                if clicked == False and (last_clicked == None or last_clicked == gold or (last_clicked == receive and (time() - loop_time) >= 20)):
                    rectangles = receive.find(screenshot, 0.8)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), receive, 0.8])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = receive
                        print("took gold")
                    if cv.waitKey(1) == ord('q'):
                        cv.destroyAllWindows()
                        q = False
                        break
                #press rewards
                if clicked == False and (last_clicked == None or last_clicked == receive or (last_clicked == reward and (time() - loop_time) >= 5)):
                    rectangles = reward.find(screenshot, 0.75)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), reward, 0.75])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = reward
                        print("reward")
                    if cv.waitKey(1) == ord('q'):
                        cv.destroyAllWindows()
                        q = False
                        break
                if clicked == False and (last_clicked == reward):
                    print("done with patrol tab")
                    t = threading.Thread(target=double_press, args=['esc',])
                    t.start()
                    clicked = True
                    loop_time = time()
                    while (time() - loop_time) <= 10:
                        screenshot = wincap.get_screenshot()
                        cv.imshow('Matches', screenshot)
                        if cv.waitKey(1) == ord('q'):
                            cv.destroyAllWindows()
                            break
                    q = False
                    break
                clicked = False
        if q == False:
            break

def claim_mail():
    if True:
        inbox = Vision('Screenshots/mail/inbox.jpg')
        coin_mail = Vision('Screenshots/mail/friend_coin_inbox.jpg')
        claim_all = Vision('Screenshots/mail/claim all.jpg')
        reward = Vision('Screenshots/reward.jpg')
        claimnt_allnt = Vision('Screenshots/mail/claimnt_allnt.jpg')
        k = Vision('Screenshots/pvp/another_green.jpg')
    loop_time = time()
    last_clicked = None
    clicked = False
    global screenshot
    thread_time = 0
    in_coin_mail = False
    while True:
        sleep(0.05)
        screenshot = wincap.get_screenshot()
        cv.imshow('Matches', screenshot)
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break
        if (time() - loop_time) >= (thread_time + 2):
            #enter the inbox
            if clicked == False and last_clicked == None:
                rectangles = inbox.find(screenshot, 0.7)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), inbox, 0.8])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = inbox
                    print("in mail inbox")
            #claim all?
            if clicked == False and (last_clicked == None or last_clicked == inbox or last_clicked == coin_mail):
                rectangles = claim_all.find(screenshot, 0.9)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), claim_all, 0.9])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = claim_all
                    print("gimme gimme")
            #or nothing to claim?
            if clicked == False and (last_clicked == None or last_clicked == coin_mail or (last_clicked == reward and (time() - loop_time) >= 5)):
                rectangles = claimnt_allnt.find(screenshot, 0.9)
                if rectangles.size != 0:
                    clicked = True
                    loop_time = time()
                    print("I has nothing")
                    last_clicked = claimnt_allnt
                    if in_coin_mail == True:
                        t.join()
                        press_once('esc')
                        print("left mail")
                        break
            #friend coin tab
            if clicked == False and (last_clicked == None or (last_clicked == reward and (time() - loop_time) >= 5) or (last_clicked == inbox and (time() - loop_time) >= 5)):
                rectangles = coin_mail.find(screenshot, 0.8)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), coin_mail, 0.75])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = coin_mail
                    print("going to coin inbox")
                    in_coin_mail = True
            #reward
            if clicked == False and (last_clicked == None or last_clicked == claim_all or (last_clicked == reward and (time() - loop_time) >= 3)):
                rectangles = reward.find(screenshot, 0.7)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), reward, 0.7])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = reward
                    print("yay free shit")
                    if in_coin_mail == True:
                        t.join()
                        press_once('esc')
                        print("left mail")
                        break
            if clicked == False:
                rectangles = k.find(screenshot, 0.85)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), k, 0.7])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = k
                    print("k")
            if clicked == True:
                clicked = False
            #time out
            if (time() - loop_time) >= 10:
                loop_time = time()
                last_clicked = None

def log_in_rewards():
    if True:
        tavern = Vision('Screenshots/Tavern.jpg')
        brown_ok = Vision('Screenshots/log in rewards/orange_ok.jpg')
        k = Vision('Screenshots/pvp/another_green.jpg')
    global screenshot
    loop_time = time()
    found_tavern = False
    last_clicked = None
    thread_time = 0
    print("hello")
    while True:
        sleep(0.05)
        screenshot = wincap.get_screenshot()
        cv.imshow('Matches', screenshot)
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break
        if (time() - loop_time) >= (thread_time + 0.5):
            #check if we're in the tavern
            if ((time() - loop_time) <= 120) and found_tavern == False:
                rectangles = tavern.find(screenshot, 0.8)
                if rectangles.size != 0:
                    found_tavern = True
                    loop_time = time()
                    if last_clicked == brown_ok:
                        break
                    print("found the tavern, looking for rewards")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            #once we find the tavern we look for the brown ok
            if ((time() - loop_time) <= 30) and found_tavern == True:
                rectangles = brown_ok.find(screenshot, 0.85)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 3), brown_ok, 0.85])
                    t.start()
                    loop_time = time()
                    print("k")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            #also make sure to look for the green ok we get regarding daily missions
            if ((time() - loop_time) <= 30) and found_tavern == True:
                rectangles = k.find(screenshot, 0.9)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 3), k, 0.8])
                    t.start()
                    loop_time = time()
                    print("k")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            if (time() - loop_time) >= 45:
                found_tavern = True
            if (time() - loop_time) >= 90:
                break

def do_free_stages():
    if True:
        battle_menu = Vision('Screenshots/battle_menu.jpg')
        green_ok = Vision('Screenshots/green_ok.jpg')
        green_chonk_ok = Vision('Screenshots/green_chonk_ok.jpg')
        blue_ok = Vision('Screenshots/blue_ok.jpg')
        chonk_ok = Vision('Screenshots/chonk_ok.jpg')
        shopup = Vision('Screenshots/shopup.jpg')
        free_stages = Vision('Screenshots/free_stages/free_stages.jpg')
        ring = Vision('Screenshots/free_stages/ring.jpg')
        stage = Vision('Screenshots/free_stages/stage.jpg')
        ticket = Vision('Screenshots/free_stages/auto_clear.jpg')
        clear = Vision('Screenshots/free_stages/skip.jpg')
        total_CC = Vision('Screenshots/free_stages/total_CC.jpg')
    last_clicked = None
    clicked = False
    global screenshot
    loop_time = time()
    thread_time = 0
    while True:
        screenshot = wincap.get_screenshot()
        cv.imshow('Matches', screenshot)
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break
        if (time() - loop_time) >= thread_time:
            #check for green ok
            if clicked == False and (last_clicked == None or last_clicked == shopup or last_clicked == battle_menu or (last_clicked == green_ok and (time() - loop_time) >= 5)):
                rectangles = green_ok.find(screenshot, 0.7)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), green_ok, 0.7])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = green_ok
                    print("k")
                rectangles = green_chonk_ok.find(screenshot, 0.7)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), green_chonk_ok, 0.7])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = green_ok
                    print("k")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            #check for pop up shop
            if clicked == False and (last_clicked == None or last_clicked == battle_menu or last_clicked == green_ok or (last_clicked == shopup and (time() - loop_time) >= 5)):
                rectangles = shopup.find(screenshot, 0.8)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), shopup, 0.8])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = shopup
                    print("pop up shop wow!!")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            #check for battle menu
            if clicked == False and (last_clicked == None or last_clicked == green_ok or (last_clicked == battle_menu and (time() - loop_time) >= 20)):
                rectangles = battle_menu.find(screenshot, 0.65)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), battle_menu, 0.65])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = battle_menu
                    print("clicking battle menu")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            #check for free stage menu
            if clicked == False and (last_clicked == None or last_clicked == battle_menu or (last_clicked == free_stages and (time() - loop_time) >= 15)):
                rectangles = free_stages.find(screenshot, 0.75)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), free_stages, 0.75])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = free_stages
                    print("free stages")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            #check for ring for now
            if clicked == False and (last_clicked == None or last_clicked == free_stages or (last_clicked == ring and (time() - loop_time) >= 10)):
                rectangles = ring.find(screenshot, 0.65)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), ring, 0.65])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = ring
                    print("picked equipment")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            #check for the stage
            if clicked == False and (last_clicked == None or last_clicked == ring or last_clicked == green_ok or (last_clicked == stage and (time() - loop_time) >= 5)):
                rectangles = stage.find(screenshot, 0.9)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 2), stage, 0.9])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = stage
                    print("picked free stage")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            #check for skip tickets
            if clicked == False and (last_clicked == None or last_clicked == stage or last_clicked == green_ok or (last_clicked == ticket and (time() - loop_time) >= 10)):
                rectangles = ticket.find(screenshot, 0.75)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), ticket, 0.73])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = ticket
                    print("skip")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            #check for skip
            if clicked == False and (last_clicked == None or last_clicked == ticket or (last_clicked == clear and (time() - loop_time) >= 20)):
                rectangles = clear.find(screenshot, 0.65)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), clear, 0.65])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = clear
                    print("skipped")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            #check for blue ok
            if clicked == False and (last_clicked == None or last_clicked == clear or (last_clicked == blue_ok and (time() - loop_time) >= 10)):
                rectangles = blue_ok.find(screenshot, 0.7)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), blue_ok, 0.7])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = blue_ok
                    print("k but blue")
                rectangles = chonk_ok.find(screenshot, 0.7)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), chonk_ok, 0.7])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = blue_ok
                    print("k but blue")
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            #check for allied CC
            if clicked == False and (last_clicked == None or last_clicked == blue_ok):
                rectangles = total_CC.find(screenshot, 0.8)
                if rectangles.size != 0:
                    t = threading.Thread(target=double_press, args=['esc',])
                    t.start()
                    clicked = True
                    loop_time = time()
                    print("exit")
                    break
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            if (time() - loop_time) >= 60:
                loop_time = time()
                last_clicked = None
            clicked = False
    while (time() - loop_time) <= 10:
        screenshot = wincap.get_screenshot()
        cv.imshow('Matches', screenshot)
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break
    print("done with free stage")

def eq():
    if True:
        k = Vision('Screenshots/pvp/another_green.jpg')
        shopup = Vision('Screenshots/shopup.jpg')
        menu = Vision('Screenshots/menu.jpg')
        inv = Vision('Screenshots/equipment/inv.jpg')
        gear = Vision('Screenshots/equipment/armor.jpg')
        sort = Vision('Screenshots/equipment/sort by.jpg')
        sort_enhance = Vision('Screenshots/equipment/enhance.jpg')
        sort_ascending = Vision('Screenshots/equipment/ascending.jpg')
        apply = Vision('Screenshots/equipment/apply.jpg')
        y_enhance = Vision('Screenshots/equipment/enhance but yellow.jpg')
        anvils = Vision('Screenshots/equipment/anvil.jpg')
        enhance_tier = Vision('Screenshots/equipment/enhance tier.jpg')
        enhance_level = Vision('Screenshots/equipment/enhance level.jpg')
        con_enhance =Vision('Screenshots/equipment/big boi enhance.jpg')
    q = False
    last_clicked = None
    clicked = False
    global screenshot
    loop_time = time()
    thread_time = 0
    while True:
        screenshot = wincap.get_screenshot()
        cv.imshow('Matches', screenshot)
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break
        if (time() - loop_time) >= thread_time + 1.5:
            #go to menu
            if clicked == False and (last_clicked == None or last_clicked == shopup or (last_clicked == menu and (time() - loop_time) >= 5)):
                rectangles = menu.find(screenshot, 0.85)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), menu, 0.85])
                    t.start()
                    clicked = True
                    loop_time = time()
                    print("went to the menu")
                    last_clicked = menu
            #inventory
            if clicked == False and (last_clicked == None or last_clicked == menu or (last_clicked == inv and (time() - loop_time) >= 5)):
                rectangles = inv.find(screenshot, 0.85)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), inv, 0.85])
                    t.start()
                    clicked = True
                    loop_time = time()
                    print("went to the inv")
                    last_clicked = inv
            #go to equipment inv tab
            if clicked == False and (last_clicked == None or last_clicked == inv or (last_clicked == gear and (time() - loop_time) >= 5)):
                rectangles = gear.find(screenshot, 0.8)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), gear, 0.8])
                    t.start()
                    clicked = True
                    loop_time = time()
                    print("we're in eq tab")
                    last_clicked = gear
            #sort menu
            if clicked == False and (last_clicked == None or last_clicked == gear or (last_clicked == sort and (time() - loop_time) >= 5)):
                rectangles = sort.find(screenshot, 0.85)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), sort, 0.85])
                    t.start()
                    clicked = True
                    loop_time = time()
                    print("sorting shit")
                    last_clicked = sort
            #sort by enhance
            if clicked == False and (last_clicked == None or last_clicked == sort or (last_clicked == sort_enhance and (time() - loop_time) >= 5)):
                rectangles = sort_enhance.find(screenshot, 0.85)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), sort_enhance, 0.85])
                    t.start()
                    clicked = True
                    loop_time = time()
                    print("sort by enhance")
                    last_clicked = sort_enhance
            #sort by ascending
            if clicked == False and (last_clicked == None or last_clicked == sort_enhance or (last_clicked == sort_ascending and (time() - loop_time) >= 5)):
                rectangles = sort_ascending.find(screenshot, 0.85)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), sort_ascending, 0.85])
                    t.start()
                    clicked = True
                    loop_time = time()
                    print("ascending order")
                    last_clicked = sort_ascending
            #apply sorting filters
            if clicked == False and (last_clicked == None or last_clicked == sort_ascending or (last_clicked == apply and (time() - loop_time) >= 5)):
                rectangles = apply.find(screenshot, 0.8)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), apply, 0.8])
                    t.start()
                    clicked = True
                    loop_time = time()
                    print("applying filters")
                    last_clicked = apply
            #press top left piece (72 pixels right 380 pixels down from top left corner)
            if clicked == False and (last_clicked == None or last_clicked == apply) and q == False:
                (x, y) = wincap.get_game_position()
                win32api.SetCursorPos(((x + 72), (y + 380)))
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
                sleep(0.02)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
                sleep(0.05)
                q = True
                thread_time = 2
                clicked = True
                print("selecting equipment")
            #press yellow enhance
            if clicked == False and (last_clicked == None or (last_clicked == apply and q == True) or (last_clicked == y_enhance and (time() - loop_time) >= 5)):
                rectangles = y_enhance.find(screenshot, 0.8)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), y_enhance, 0.8])
                    t.start()
                    clicked = True
                    loop_time = time()
                    print("enhance equipment")
                    last_clicked = y_enhance
                else:
                    q = False
            #press on anvil icon
            if clicked == False and (last_clicked == None or last_clicked == y_enhance or (last_clicked == anvils and (time() - loop_time) >= 5)):
                rectangles = anvils.find(screenshot, 0.85)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), anvils, 0.85])
                    t.start()
                    clicked = True
                    loop_time = time()
                    print("consectuve enhancements")
                    last_clicked = anvils
            #select awakening tier (2)
            if clicked == False and (last_clicked == None or last_clicked == anvils or (last_clicked == enhance_tier and (time() - loop_time) >= 5)):
                rectangles = enhance_tier.find(screenshot, 0.8)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), enhance_tier, 0.8])
                    t.start()
                    clicked = True
                    loop_time = time()
                    print("selecting awakening tier")
                    last_clicked = enhance_tier
            #select enhance tier (0)
            if clicked == False and (last_clicked == None or last_clicked == enhance_tier or (last_clicked == enhance_level and (time() - loop_time) >= 5)):
                rectangles = enhance_level.find(screenshot, 0.85)
                if rectangles.size != 0:
                    click_sec_im(rectangles, enhance_level)
                    thread_time = 0.5
                    clicked = True
                    loop_time = time()
                    print("selecting enhance tier")
                    last_clicked = enhance_level
            #consecutive enhance
            if clicked == False and (last_clicked == None or last_clicked == enhance_level or (last_clicked == con_enhance and (time() - loop_time) >= 5)):
                rectangles = con_enhance.find(screenshot, 0.85)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), con_enhance, 0.85])
                    t.start()
                    clicked = True
                    loop_time = time()
                    print("actually enhancing the gear")
                    last_clicked = con_enhance
            #k into single esc
            if clicked == False and (last_clicked == None or last_clicked == con_enhance or  last_clicked == shopup or (last_clicked == k and (time() - loop_time) >= 5)):
                rectangles = k.find(screenshot, 0.9)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), k, 0.9])
                    t.start()
                    clicked = True
                    loop_time = time()
                    print("k")
                    if last_clicked == con_enhance:
                        double_press('esc')
                        print("we are done, goodbye foreva")
                        break
                    last_clicked = k
            if clicked == True:
                clicked = False

def do_demons(demon_amount = 3):
    if True:
        battle_menu = Vision('Screenshots/battle_menu.jpg')
        accept_raid = Vision('Screenshots/demons/accept.jpg')
        bunny = Vision('Screenshots/demons/bunny.jpg')
        fattie = Vision('Screenshots/demons/fattie.jpg')
        slanderman = Vision('Screenshots/demons/slanderman.jpg')
        bell = Vision('Screenshots/demons/bell.jpg')
        auto = Vision('Screenshots/auto.jpg')
        demons = Vision('Screenshots/demons/demons.jpg')
        green_ok = Vision('Screenshots/green_ok.jpg')
        hell = Vision('Screenshots/demons/hell.jpg')
        hard = Vision('Screenshots/demons/hard.jpg')
        demon_ok = Vision('Screenshots/demons/demon_ok.jpg')
        prep = Vision('Screenshots/demons/prep.jpg')
        dead = Vision('Screenshots/pvp/another_green.jpg')
        spamming = fattie
        diff = hell
    global screenshot
    last_clicked = None
    loop_time = time()
    z = 0
    clicked = False
    death_count = 0
    thread_time = 0
    timer = time()
    while True:
        if z >= demon_amount:
            t.join()
            break
        sleep(0.05)
        screenshot = wincap.get_screenshot()
        output_im = screenshot
        cv.imshow('Matches', output_im)
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break
        if (time() - loop_time) >= (thread_time + 1):
            #do we need to search for demon ok
            if clicked == False and (last_clicked == None or last_clicked == prep or last_clicked == auto or last_clicked == green_ok or (last_clicked == demon_ok and (time() - loop_time) >= 10)):
                rectangles = demon_ok.find(screenshot, 0.65)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 5), demon_ok, 0.65])
                    t.start()
                    clicked = True
                    loop_time = time()
                    if last_clicked != demon_ok:
                        z += 1
                    last_clicked = demon_ok
                    print(f"done with {z} demons")
            # pressing normal ok if people are being little shits
            if clicked == False and (last_clicked == None or (time() - loop_time) >= 5 or last_clicked == dead):
                rectangles = green_ok.find(screenshot, 0.7)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), green_ok, 0.7])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = green_ok
                    print("k")
            #do we need to search for battle menu
            if clicked == False and (last_clicked == None or last_clicked == demon_ok or last_clicked == green_ok or (last_clicked == battle_menu and (time() - loop_time) >= 15) or last_clicked == dead):
                rectangles = battle_menu.find(screenshot, 0.65)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 3), battle_menu, 0.65])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = battle_menu
                    print("clicking battle menu")
            #do we need to search for demons tab
            if clicked == False and (last_clicked == None or last_clicked == battle_menu):
                rectangles = demons.find(screenshot, 0.65)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 3), demons, 0.65])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = demons
                    print("clicking demons menu")
            #do we need to search for the demon, change according to demon you want to spam
            if clicked == False and (last_clicked == None or last_clicked == demons or last_clicked == green_ok or (last_clicked == spamming and (time() - loop_time) >= 20) or (last_clicked == accept_raid and (time() - loop_time) >= 30) or (last_clicked == diff and (time() - loop_time) >= 120)):
                rectangles = spamming.find(screenshot, 0.65)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), spamming, 0.65])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = spamming
                    print("picking demon")
            #do we need to pick difficulty
            if clicked == False and (last_clicked == None or last_clicked == spamming or last_clicked == green_ok):
                rectangles = diff.find(screenshot, 0.65)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 0.2), diff, 0.6])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = diff
                    print("picking diff")
            #do we need to search for accept raid
            if clicked == False and last_clicked == diff:
                rectangles = accept_raid.find(screenshot, 0.85)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 8), accept_raid, 0.65])
                    t.start()
                    clicked = True
                    last_clicked = accept_raid
                    loop_time = time()
                    print("accepting raid")
            #do we need to search for prep
            if clicked == False and (last_clicked == None or last_clicked == green_ok or last_clicked == accept_raid or (last_clicked == prep and (time() - loop_time) >= 2)):
                rectangles = prep.find(screenshot, 0.65)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 0.001), prep, 0.65])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = prep
                    print("ready")
            #autoing the demon
            if clicked == False and (last_clicked == None or last_clicked == prep):
                rectangles = auto.find(screenshot, 0.75)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 10), auto, 0.75])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = auto
                    print("autoing")
            if clicked == False and (last_clicked == None or last_clicked == auto or last_clicked == green_ok):
                rectangles = dead.find(screenshot, 0.95)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 5), dead, 0.95])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = dead
                    death_count += 1
                    print(f"we died {death_count} times")
            if clicked == True:
                clicked = False
        # print(time()-loop_time)
        if ((time() - loop_time) >= 150 and (last_clicked != auto)) or ((time() - loop_time) >= 420 and (last_clicked == auto)):
            loop_time = time()
            last_clicked = None
            print("time")
    print("done")

def coin_shopping():
    if True:
        tavern = Vision('Screenshots/Tavern.jpg')
        k = Vision('Screenshots/pvp/another_green.jpg')
        shopup = Vision('Screenshots/shopup.jpg')
        friend_coins = Vision('Screenshots/coin_shop/coins.jpg')
        exchange = Vision('Screenshots/coin_shop/exchange.jpg')
        free_treasure = Vision('Screenshots/coin_shop/free.jpg')
        max = Vision('Screenshots/coin_shop/max_exchange.jpg')
        out_of_coin = Vision('Screenshots/coin_shop/out_of_coin.jpg')
        pots = Vision('Screenshots/coin_shop/pots.jpg')
        coin_shop = Vision('Screenshots/coin_shop/shop.jpg')
        swap_tab = Vision('Screenshots/coin_shop/shop_tab.jpg')
        shops_menu = Vision('Screenshots/coin_shop/shops.jpg')
        header = Vision('Screenshots/coin_shop/header.jpg')
        treasure = Vision('Screenshots/coin_shop/treassure.jpg')
        reward = Vision('Screenshots/reward.jpg')
        bat_card = Vision('Screenshots/coin_shop/card.jpg')
    loop_time = time()
    last_clicked = None
    clicked = False
    global screenshot
    thread_time = 0
    q = True
    while True:
        sleep(0.05)
        screenshot = wincap.get_screenshot()
        cv.imshow('Matches', screenshot)
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break
        if (time() - loop_time) >= (thread_time + 1):
            #going to tavern
            if clicked == False and (last_clicked == None or (last_clicked == tavern and (time() - loop_time) >= 10)):
                rectangles = tavern.find(screenshot, 0.8)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), tavern, 0.75])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = tavern
                    print("tavern")
            #k
            if clicked == False and (last_clicked == None or last_clicked == shops_menu or last_clicked == shopup or (last_clicked == k and (time() - loop_time) >= 5)):
                rectangles = k.find(screenshot, 0.9)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), k, 0.85])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = k
                    print("k")
            # check for pop up shop
            if clicked == False and (last_clicked == None or last_clicked == k or (last_clicked == shopup and (time() - loop_time) >= 5)):
                rectangles = shopup.find(screenshot, 0.8)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), shopup, 0.8])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = shopup
                    print("pop up shop wow!!")
            #go to shop tab
            if clicked == False and (last_clicked == None or last_clicked == tavern or last_clicked == shopup or last_clicked == k or (last_clicked == shops_menu and (time() - loop_time) >= 10)):
                rectangles = shops_menu.find(screenshot, 0.7)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), shops_menu, 0.7])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = shops_menu
                    print("shops menu")
            #go to coin shop
            if clicked == False and (last_clicked == None or last_clicked == shops_menu or (last_clicked == coin_shop and (time() - loop_time) >= 10)):
                rectangles = coin_shop.find(screenshot, 0.8)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), coin_shop, 0.8])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = coin_shop
                    print("entering coin shop")
            #swap tab
            if clicked == False and (last_clicked == None or last_clicked == coin_shop or (last_clicked == swap_tab and (time() - loop_time) >= 10)):
                rectangles = swap_tab.find(screenshot, 0.8)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1.5), swap_tab, 0.8])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = swap_tab
                    print("swapping tab")
            #scroll down until finding treasure and then pots
            if clicked == False and (last_clicked == None or last_clicked == shops_menu or last_clicked == free_treasure or last_clicked == swap_tab or last_clicked == reward or (last_clicked == header and (time() - loop_time) >= 7)):
                rectangles = header.find(screenshot, 0.8)
                if rectangles.size != 0:
                    t = threading.Thread(target=scroll_shop, args=[1, ])
                    t.start()
                    thread_time = 1
                    clicked = True
                    loop_time = time()
                    last_clicked = header
                    print("scrolling")
            #claim the treassure if it's there
            if clicked == False and (last_clicked == None or last_clicked == header or (last_clicked == free_treasure and (time() - loop_time) >= 10)):
                rectangles = treasure.find(screenshot, 0.75)
                if rectangles.size != 0:
                    rectangles = free_treasure.find(screenshot, 0.8)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 1), free_treasure, 0.8])
                        t.start()
                        print("got free treasure")
                    else:
                        print("treasure was already obtained previously")
                    clicked = True
                    loop_time = time()
                    last_clicked = free_treasure
            #click the reward button if we got treassure or bought the pots
            if clicked == False and (last_clicked == None or last_clicked == free_treasure or last_clicked == exchange or last_clicked == reward):
                rectangles = reward.find(screenshot, 0.8)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 0.5), reward, 0.8])
                    t.start()
                    clicked = True
                    loop_time = time()
                    if q == False:
                        t.join()
                        double_press('esc')
                        break
                    if q == True:
                        last_clicked = reward
                    print("claimed reward")
            #get them pots
            if clicked == False and (last_clicked == None or last_clicked == header or last_clicked == reward or (last_clicked == pots and (time() - loop_time) >= 4)):
                rectangles = bat_card.find(screenshot, 0.75)
                if rectangles.size != 0:
                    rectangles = pots.find(screenshot, 0.75)
                    if rectangles.size != 0:
                        t = threading.Thread(target=sleep_and_click, args=[(thread_time := 0.5), pots, 0.75])
                        t.start()
                        clicked = True
                        loop_time = time()
                        last_clicked = pots
                        print("pots?")
            #buy max pots
            if clicked == False and (last_clicked == None or last_clicked == pots or (last_clicked == max and (time() - loop_time) >= 6)):
                rectangles = max.find(screenshot, 0.75)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 0.5), max, 0.75])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = max
                    print("give all them pots")
            #give coins
            if clicked == False and (last_clicked == None or last_clicked == max or (last_clicked == friend_coins and (time() - loop_time) >= 10)):
                rectangles = friend_coins.find(screenshot, 0.75)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 0.5), friend_coins, 0.75])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = friend_coins
                    print("yeet the coin")
            #check if we ran out of coin
            if clicked == False and (last_clicked == None or last_clicked == friend_coins or (last_clicked == out_of_coin and (time() - loop_time) >= 10)):
                rectangles = out_of_coin.find(screenshot, 0.75)
                if rectangles.size != 0:
                    t = threading.Thread(target=double_press(), args=['esc', ])
                    t.start()
                    clicked = True
                    thread_time = 2
                    loop_time = time()
                    last_clicked = out_of_coin
                    print("we out of coin chief")
            if clicked == False and last_clicked == out_of_coin:
                rectangles = tavern.find(screenshot, 0.75)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 0.5), tavern, 0.75])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = tavern
                    print("back to tavern")
                    break
            #exchange
            if clicked == False and (last_clicked == None or last_clicked == friend_coins or (last_clicked == exchange and (time() - loop_time) >= 10)):
                rectangles = exchange.find(screenshot, 0.75)
                if rectangles.size != 0:
                    t = threading.Thread(target=sleep_and_click, args=[(thread_time := 0.5), exchange, 0.75])
                    t.start()
                    clicked = True
                    loop_time = time()
                    last_clicked = exchange
                    q = False
                    print("gib za pots")
            clicked = False




