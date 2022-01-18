from windowcapture import WindowCapture
from vision import Vision, click
from time import time, sleep
import cv2 as cv
import numpy as np



def click_im(rectangles, img1):
    (x, y) = img1.get_click_point(rectangles)
    (x, y) = ((x + window_location[0]), (y + window_location[1]))
    click(x, y)

def click_until_found(rectangles, im1, im2, confidence1=0.6, confidence2=0.6):
    loop_time = time()
    got_points = 0
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
                got_points = 1
                click(x, y)
                #check if next image shows up for x amount of frames
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
            #print('FPS {}'.format(1 / (time() - loop_time)))
            loop_time = time()
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                break
        #exit the functions loop, another break may be needed if used within a loop
        if clicked == False:
            break

def join_demon(rectangles, demon_to_repeat, demon_to_check_against, difficulty, search_for_how_many_frames = 30):
    loop_time = time()
    while True:
        search_and_click(rectangles, demon_to_repeat, 0.85)
        while True:
            if clicked := True:
                #search for first image, dark orb in this case
                (screenshot, window_location) = wincap.get_screenshot()
                rectangles = difficulty.find(screenshot, 0.85)
                output_im = difficulty.draw_rectangles(screenshot, rectangles)
                cv.imshow('Matches', output_im)
                if rectangles.size != 0:
                    #click command
                    (x, y) = difficulty.get_click_point(rectangles)
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
                        rectangles = demon_to_check_against.find(screenshot, 0.9)
                        output_im = demon_join.draw_rectangles(screenshot, rectangles)
                        cv.imshow('Matches', output_im)
                        #if we see the demon timer probably ran out
                        if rectangles.size != 0:
                            #making sure if wasn't an error
                            frames = frames + 1
                            print(f"frame count: {frames}/15")
                            if frames >= 15:
                                print("need to find another invite")
                                (screenshot, window_location) = wincap.get_screenshot()
                                rectangles = demon_to_repeat.find(screenshot, 0.95)
                                output_im = demon_to_repeat.draw_rectangles(screenshot, rectangles)
                                cv.imshow('Matches', output_im)
                                if rectangles.size != 0:
                                    click_im(rectangles, demon_to_repeat)
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
                rectangles = demon_to_check_against.find(screenshot, 0.85)
                output_im = demon_to_check_against.draw_rectangles(screenshot, rectangles)
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
    tavern = Vision('bluestacks_SS\\tavern.jpg')
    green_ok = Vision('bluestacks_SS\\Green_ok.jpg')
    tap_to_proceed = Vision('bluestacks_SS\\tap_to_proceed.jpg')
    demon_join = Vision('bluestacks_SS\\demons\\demon_join.jpg')
    auto = Vision('bluestacks_SS\\demons\\auto.jpg')
    bunny = Vision('bluestacks_SS\\demons\\bunny.jpg')
    demon_accept = Vision('bluestacks_SS\\demons\\demon_accept.jpg')
    demons = Vision('bluestacks_SS\\demons\\demons.jpg')
    fattie = Vision('bluestacks_SS\\demons\\fattie.jpg')
    prep = Vision('bluestacks_SS\\demons\\prep.jpg')
    skinny = Vision('bluestacks_SS\\demons\\skinny.jpg')
    hell_diff = Vision('bluestacks_SS\\demons\\demon_diff.jpg')
    hard_diff = Vision('bluestacks_SS\\demons\\hard.jpg')
    is_normal_demons = Vision('bluestacks_SS\\demons\\is_normal_demons.jpg')
    bell = Vision('bluestacks_SS\\demons\\bellmoth.jpg')
    demon_ok = Vision('bluestacks_SS\\demons\\demon_ok.jpg')


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
            click_until_found(rectangles, battle_menu, demons, 0.65, 0.7)
            print("in battle menu")
            break
    #click demons tab
    if True:
        while True:
            click_until_found(rectangles, demons, battle_menu, 0.7, 0.55)
            print("in battle menu")
            break
    #check if we're doing bellmoths or normal demons, to be done in the future
    if True:
        pass
    #join a demon, and auto it I guess...
    if True:
        while True:
        #pick a demon and join raid
            if True:
                bamboozled = False
                while True:
                    #change bunny to the demon you want to do
                    #only change skinny when doing bell for normal demons keep it as skinny
                    join_demon(rectangles, bunny, skinny, hell_diff, 30)
                    #join the raid
                    while True:
                        search_and_click(rectangles, demon_accept, 0.75)
                        print("joined demon")
                        break
                    for idk in range(0, 100, 1):
                        (screenshot, window_location) = wincap.get_screenshot()
                        rectangles = green_ok.find(screenshot, 0.7)
                        output_im = green_ok.draw_rectangles(screenshot, rectangles)
                        cv.imshow('Matches', output_im)
                        if rectangles.size != 0:
                            bamboozled = True
                            break
                        if cv.waitKey(1) == ord('q'):
                            cv.destroyAllWindows()
                            break
                    if bamboozled == False:
                        break
            #click prep button and wait for them to start the demon
            if bamboozled == False:
                while True:
                    (screenshot, window_location) = wincap.get_screenshot()
                    rectangles = prep.find(screenshot, 0.5)
                    output_im = prep.draw_rectangles(screenshot, rectangles)
                    cv.imshow('Matches', output_im)
                    if rectangles.size != 0:
                        click_im(rectangles, prep)
                        break
                    if cv.waitKey(1) == ord('q'):
                        cv.destroyAllWindows()
                        break
            #auto
            if bamboozled == False:
                while True:
                    (screenshot, window_location) = wincap.get_screenshot()
                    rectangles = auto.find(screenshot, 0.75)
                    output_im = auto.draw_rectangles(screenshot, rectangles)
                    cv.imshow('Matches', output_im)
                    if rectangles.size != 0:
                        click_im(rectangles, auto)
                        print("autoing")
                        break
                    if cv.waitKey(1) == ord('q'):
                        cv.destroyAllWindows()
                        break
                    rectangles = tavern.find(screenshot, 0.85)
                    if rectangles.size != 0:
                        bamboozled = True
                        while True:
                            click_until_found(rectangles, battle_menu, demons, 0.65, 0.7)
                            print("in battle menu")
                            break
                        #click demons tab
                        while True:
                            click_until_found(rectangles, demons, battle_menu, 0.7, 0.55)
                            print("in battle menu")
                            break
                        break
                    if cv.waitKey(1) == ord('q'):
                        cv.destroyAllWindows()
                        break
            if bamboozled == False:
                break
    #press ok until we can see tavern button
    if True:
        click_until_found(rectangles, demon_ok, battle_menu, 0.7, 0.65)

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
    print(f"done {z+1} demons")
    z = z+1
    #print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses

