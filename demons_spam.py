from windowcapture import WindowCapture
from vision import Vision, click
from time import time, sleep
import cv2 as cv
import numpy as np



def click_im(rectangles, img1):
    (x, y) = img1.get_click_point(rectangles)
    (x, y) = ((x + window_location[0]), (y + window_location[1]))
    click(x, y)

def click_until_found(rectangles, im1, im2, confidence1=0.6, confidence2=0.6, how_long_search = 30):
    loop_time = time()
    while True:
        if clicked := True:
            #search for first image
            (screenshot, window_location) = wincap.get_screenshot()
            rectangles = im1.find(screenshot, confidence1)
            output_im = im1.draw_rectangles(screenshot, rectangles)
            cv.imshow('Matches', output_im)
            if rectangles.size != 0:
                #click command
                (x, y) = im1.get_click_point(rectangles)
                (x, y) = ((x + window_location[0]), (y + window_location[1]))
                click(x, y)
                #check if next image shows up for x amount of frames
                print("looking for next image")
                for i in range(0, how_long_search, 1):
                    (screenshot, window_location) = wincap.get_screenshot()
                    rectangles = im2.find(screenshot, confidence2)
                    output_im = im2.draw_rectangles(screenshot, rectangles)
                    cv.imshow('Matches', output_im)
                    #print(rectangles)
                    #the check itself, if found exit the loop
                    if rectangles.size != 0:
                        print("next im found")
                        clicked = False # variable to confirm next image was found
                        break
                    #print('FPS {}'.format(1 / (time() - loop_time)))
                    loop_time = time()
                    if cv.waitKey(1) == ord('q'):
                        cv.destroyAllWindows()
                        break
            #print('FPS {}'.format(1 / (time() - loop_time)))
            loop_time = time()
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                break
        #exit the functions loop, another break may be needed if used within a loop
        if clicked == False:
            break

def click_when_found(rectangles, check_for_img, click_img, confidence1=0.6, confidence2=0.6):
    loop_time = time()
    while True:
        (screenshot, window_location) = wincap.get_screenshot()
        rectangles = check_for_img.find(screenshot, confidence1)
        output_im = check_for_img.draw_rectangles(screenshot, rectangles)
        cv.imshow('Matches', output_im)
        if rectangles.size != 0:
            rectangles = click_img.find(screenshot, confidence2)
            click_im(rectangles, click_img)
            break

        print('FPS {}'.format(1 / (time() - loop_time)))
        loop_time = time()
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break

def search_and_click(rectangles, img, confidence=0.6):
    while True:
        (screenshot, window_location) = wincap.get_screenshot()
        rectangles = img.find(screenshot, confidence)
        output_im = img.draw_rectangles(screenshot, rectangles)
        cv.imshow('Matches', output_im)
        if rectangles.size != 0:
            click_im(rectangles, img)
            break
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break

#window to capture
wincap =  WindowCapture('BlueStacks')
#load images
if True:
    #images to identify
    battle_menu = Vision('bluestacks_SS\\battle_menu.jpg')
    blue_ok =  Vision('bluestacks_SS\\Blue_ok.jpg')
    green_ok = Vision('bluestacks_SS\\Green_ok.jpg')
    demon_join = Vision('bluestacks_SS\\demons\\demon_join.jpg')
    auto = Vision('bluestacks_SS\\demons\\auto.jpg')
    bunny = Vision('bluestacks_SS\\demons\\bunny.jpg')
    demon_accept = Vision('bluestacks_SS\\demons\\demon_accept.jpg')
    demons = Vision('bluestacks_SS\\demons\\demons.jpg')
    fattie = Vision('bluestacks_SS\\demons\\fattie.jpg')
    prep = Vision('bluestacks_SS\\demons\\prep.jpg')
    skinny = Vision('bluestacks_SS\\demons\\skinny.jpg')
    demon_diff = Vision('bluestacks_SS\\demons\\demon_diff.jpg')
    is_normal_demons = Vision('bluestacks_SS\\demons\\is_normal_demons.jpg')
    bell = Vision('bluestacks_SS\\demons\\bellmoth.jpg')
    demon_ok = Vision('bluestacks_SS\\demons\\demon_ok.jpg')
    tavern = Vision('bluestacks_SS\\tavern.jpg')


z = 0
frames = 0
loop_time = time()
while(True):
    #start screen recording
    (screenshot, window_location) = wincap.get_screenshot()
    rectangles = battle_menu.find(screenshot, 0.85)
    output_im = battle_menu.draw_rectangles(screenshot, rectangles)
    cv.imshow('Matches', output_im)
    #click battle menu until we can see the menu
    if True:
        while True:
            click_until_found(rectangles, battle_menu, demons, 0.55, 0.7)
            print("in battle menu")
            break
    #click demons tab
    if True:
        while True:
            (screenshot, window_location) = wincap.get_screenshot()
            rectangles = demons.find(screenshot, 0.85)
            output_im = demons.draw_rectangles(screenshot, rectangles)
            cv.imshow('Matches', output_im)
            if rectangles.size != 0:
                sleep(0.25)
                click_im(rectangles, demons)
                print("went into demons menu")
                break
            #print('FPS {}'.format(1 / (time() - loop_time)))
            loop_time = time()
            # press 'q' with the output window focused to exit.
            # waits 1 ms every loop to process key presses
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                break
    #pick a demon and join raid
    if True:
        while True:
            search_and_click(rectangles, bunny, 0.85)
            while True:
                if clicked := True:
                    #search for first image, dark orb in this case
                    (screenshot, window_location) = wincap.get_screenshot()
                    rectangles = demon_diff.find(screenshot, 0.85)
                    output_im = demon_diff.draw_rectangles(screenshot, rectangles)
                    cv.imshow('Matches', output_im)
                    if rectangles.size != 0:
                        #click command
                        (x, y) = demon_diff.get_click_point(rectangles)
                        (x, y) = ((x + window_location[0]), (y + window_location[1]))
                        click(x, y)
                        print("pressed dark orb")
                        #check if next image shows up for x amount of frames
                        frames = 0
                        for i in range(0, 1750 , 1):
                            (screenshot, window_location) = wincap.get_screenshot()
                            rectangles = demon_join.find(screenshot, 0.98)
                            output_im = demon_join.draw_rectangles(screenshot, rectangles)
                            cv.imshow('Matches', output_im)
                            #the check itself, if found exit the loop
                            if rectangles.size != 0:
                                print("found invite")
                                clicked = False # variable to confirm next image was found
                                break
                            #make sure timer didn't run out or some twat took back invite
                            rectangles = skinny.find(screenshot, 0.9)
                            output_im = demon_join.draw_rectangles(screenshot, rectangles)
                            cv.imshow('Matches', output_im)
                            #if we see the demon timer probably ran out
                            if rectangles.size != 0:
                                #making sure if wasn't an error
                                frames = frames + 1
                                print(frames)
                                if frames >= 15:
                                    print("need to find another invite")
                                    (screenshot, window_location) = wincap.get_screenshot()
                                    rectangles = skinny.find(screenshot, 0.95)
                                    output_im = skinny.draw_rectangles(screenshot, rectangles)
                                    cv.imshow('Matches', output_im)
                                    if rectangles.size != 0:
                                        click_im(rectangles, skinny)
                                        print("picked demon again")
                                        break
                                    #print('FPS {}'.format(1 / (time() - loop_time)))
                                    loop_time = time()
                                    if cv.waitKey(1) == ord('q'):
                                        cv.destroyAllWindows()
                                        break

                            #print('FPS {}'.format(1 / (time() - loop_time)))
                            loop_time = time()
                            if cv.waitKey(1) == ord('q'):
                                cv.destroyAllWindows()
                                break
                        if clicked == False:
                            break
                    #making sure the previous click registered
                    rectangles = skinny.find(screenshot, 0.85)
                    output_im = skinny.draw_rectangles(screenshot, rectangles)
                    cv.imshow('Matches', output_im)
                    #print('FPS {}'.format(1 / (time() - loop_time)))
                    loop_time = time()
                    if cv.waitKey(1) == ord('q'):
                        cv.destroyAllWindows()
                        break
                #exit the functions loop, another break may be needed if used within a loop
                if clicked == False:
                    break
            break
    #join the raid
    if True:
        while True:
            search_and_click(rectangles, demon_accept, 0.75)
            print("joined demon")
            break
    #click prep button and wait for them to start the demon
    if True:
        while True:
            search_and_click(rectangles, prep, 0.5)
            print("ready")
            break
    #auto
    if True:
        while True:
            search_and_click(rectangles, auto, 0.75)
            print("autoing")
            break
    #press ok until we can see tavern button
    if True:
        while True:
            while True:
                (screenshot, window_location) = wincap.get_screenshot()
                rectangles = demon_ok.find(screenshot, 0.6)
                output_im = demon_ok.draw_rectangles(screenshot, rectangles)
                cv.imshow('Matches', output_im)
                if rectangles.size != 0:
                    sleep(0.25)
                    click_im(rectangles, demon_ok)
                    break
                if cv.waitKey(1) == ord('q'):
                    cv.destroyAllWindows()
                    break
            break

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
    print(f"done {z+1} demons")
    #print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
