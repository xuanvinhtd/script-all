import pyautogui, sys
import argparse
import pathlib
import time

def changevpn(region):
    pyautogui.click(x=1700, y=51)
    pyautogui.PAUSE = 5
    pathFile = str(pathlib.Path(__file__).parent.resolve())
    
    p= None
    tryFind = 0
    isTop = False

    while p is None: 

        for x in range(0, 5):
            t= None
            e= None
            p = pyautogui.locateCenterOnScreen(pathFile + "\\pytool\\" + region, confidence=0.7)
            t = pyautogui.locateCenterOnScreen(pathFile + "\\pytool\\faster.png", confidence=0.7)
            e = pyautogui.locateCenterOnScreen(pathFile + "\\pytool\\taiwain.png", confidence=0.7)

            if t is not None:
                if isTop == False:
                    tryFind += 1               
                isTop = True
                
            if e is not None: 
                if isTop:
                    tryFind += 1
                isTop = False

            if p is not None: break
        if p is not None: break
        if tryFind >= 4: break
          
        if isTop:       
            pyautogui.click(x=1910, y=393, clicks=1, interval=0.25) # click down
        else:
            pyautogui.click(x=1911, y=41, clicks=1, interval=0.25) # click up     
        
        pyautogui.PAUSE = 1
       

    pyautogui.PAUSE = 2
    if p is not None:
        pyautogui.click(p.x, p.y)
        ck = None
        for x in range(0, 5):
            time.sleep(15)
            ck = pyautogui.locateCenterOnScreen(pathFile + "\\pytool\\connected_vpn.png", confidence=0.7)
            if ck is not None:
                break
        if ck is None:
            pyautogui.click(1624, 37)
            for x in range(0, 5):
                time.sleep(10) 
                ck = pyautogui.locateCenterOnScreen(pathFile + "\\pytool\\connected_vpn.png", confidence=0.7)
                if ck is not None:
                    break
        if ck is None:
            return "fail"
        else:
            return "success"
    else:
        return "fail"
    

MyParser = argparse.ArgumentParser(description="Generate, Change vpn")
MyParser.add_argument('-change',required=True,help='Change vpn with region',type=str)
args = MyParser.parse_args()

if args.change !=None:
    rs = changevpn(args.change)
    print(rs)