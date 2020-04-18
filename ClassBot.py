from pil import ImageGrab,ImageOps
import os
import time
from numpy import *
from ClassConfig import  *
import win32api,win32con
import keyboard
class Mybot():
    def __init__(self):
        self.grab = ImageGrab
        self.mainpath = os.path.dirname(__file__)
        self.pathphoto = os.path.join(self.mainpath,"photo")
        self.box = ()
        self.FoodOnhand = {
            'ไข่ปลา':10,
            'ข้าว':10,
            'สาหร่าย':10
        }
        self.SushiType ={
            1770:"gunkan",
            1843:"onigiri",
            2100:"cailroll"
        }
        ###blank table###
        self.Blank_1 = 5514
        self.Blank_2 = 4792
        self.Blank_3 = 9335
        self.Blank_4 = 9254
        self.Blank_5 = 4948
        self.Blank_6 = 7038
    def Grab_img(self):
        self.box =(450,378,1086,850)
        img = self.grab.grab()
        return img
    def MouseClick(self,cord):
        win32api.SetCursorPos((cord[0],cord[1]))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.5)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        time.sleep(0.3)
    def StarGame(self):
        #play menu 456 707
        self.MouseClick((449,536))
        #skip
        self.MouseClick((732,786))
        #continue
        self.MouseClick((456,707))    
    def MakeFood(self,food):
        if food == "onigiri":
            self.MouseClick(Cord.กดข้าว)
            self.MouseClick(Cord.กดข้าว)
            self.MouseClick(Cord.กดสาหร่าย)
            self.MouseClick(Cord.กดส่งอาหาร)
            self.FoodOnhand['ข้าว'] -=2
            self.FoodOnhand['สาหร่าย'] -=1
        if food == "cailroll":
            self.MouseClick(Cord.กดข้าว)
            self.MouseClick(Cord.กดสาหร่าย)
            self.MouseClick(Cord.กดไข่ปลา)
            self.MouseClick(Cord.กดส่งอาหาร)
            self.FoodOnhand['ข้าว'] -=1
            self.FoodOnhand['สาหร่าย'] -=1
            self.FoodOnhand['ไข่ปลา'] -=1
        if food == "gunkan":
            self.MouseClick(Cord.กดข้าว)  
            self.MouseClick(Cord.กดสาหร่าย)  
            self.MouseClick(Cord.กดไข่ปลา)
            self.MouseClick(Cord.กดไข่ปลา)
            self.MouseClick(Cord.กดส่งอาหาร)
            self.FoodOnhand['ข้าว'] -=1
            self.FoodOnhand['สาหร่าย'] -=1
            self.FoodOnhand['ไข่ปลา'] -=2
    def BuyFood(self,food):
        if food == "สาหร่าย":
            self.MouseClick(Cord.กดโทรศัพ)
            self.MouseClick(Cord.กดเมนูทอปปิ้ง)
            if self.Grab_img().getpixel(Cord.สั้งสาหร่าย) != (33, 30, 11):
                print("กำลังสั่งอาหาร สาหร่าย")
                self.MouseClick(Cord.สั้งสาหร่าย)
                self.MouseClick(Cord.กดสั่งอาหาร)
                self.FoodOnhand['สาหร่าย'] +=10
            else:
                self.MouseClick(Cord.กดวางมือถือ)
                print("ยังไม่พร้อมสั่งอาหาร สาหร่าย")
                self.BuyFood(food)
        if food == "ข้าว":
            self.MouseClick(Cord.กดโทรศัพ)
            self.MouseClick(Cord.กดเมนูข้าว)
            if self.Grab_img().getpixel(Cord.สั่งข้าว) != (118, 83, 85):
                print("กำลังสั่งอาหาร ข้าว")
                self.MouseClick(Cord.สั่งข้าว)
                self.MouseClick(Cord.กดสั่งอาหาร)
                self.FoodOnhand['ข้าว'] +=10
            else:
                print("ยังไม่พร้อมสั่งอาหาร ข้าว")   
                self.MouseClick(Cord.กดวางมือถือ)
                self.BuyFood(food)
        if food == "ไข่ปลา":
            self.MouseClick(Cord.กดโทรศัพ)
            self.MouseClick(Cord.กดเมนูทอปปิ้ง)
            if self.Grab_img().getpixel(Cord.สั่งไข่ปลา) != (127, 61, 0):
                print("กำลังสั่งอาหาร ไข่ปลา")
                self.MouseClick(Cord.สั่งไข่ปลา)
                self.MouseClick(Cord.กดสั่งอาหาร)
                self.FoodOnhand['ไข่ปลา'] +=10
            else:
                print("ยังไม่พร้อมสั่งอาหารไข่ปลา")   
                self.MouseClick(Cord.กดวางมือถือ)
                self.BuyFood(food)
    def CheckFood(self):
        for key,values in self.FoodOnhand.items():
            if key == "ไข่ปลา" or key == "ข้าว" or key =="สาหร่าย":
                if values < 4:
                    self.BuyFood(key)
    def GetSeat1(self):
        box = (177,397,177+63,397+10)
        img = ImageOps.grayscale(self.grab.grab(box))
        sumcolor = array(img.getcolors())
        sumcolor = sumcolor.sum()
        img.save(f"{self.pathphoto}/seat1.jpg")
        self.grab.grab(box).save(f"{self.pathphoto}/seat11.jpg")
     
        return sumcolor
    def GetSeat2(self):
        box = (278,397,278+63,397+10)
        img = ImageOps.grayscale(self.grab.grab(box))
        sumcolor = array(img.getcolors())
        sumcolor = sumcolor.sum()
        img.save(f"{self.pathphoto}/seat2.jpg")
        self.grab.grab(box).save(f"{self.pathphoto}/seat22.jpg")
        
        return sumcolor
    def GetSeat3(self):
        box = (379,397,379+63,397+10)
        img = ImageOps.grayscale(self.grab.grab(box))
        sumcolor = array(img.getcolors())
        sumcolor = sumcolor.sum()
        img.save(f"{self.pathphoto}/seat3.jpg")
        self.grab.grab(box).save(f"{self.pathphoto}/seat33.jpg")
   
        return sumcolor   
    def GetSeat4(self):
        box = (480,397,480+63,397+10)
        img = ImageOps.grayscale(self.grab.grab(box))
        sumcolor = array(img.getcolors())
        sumcolor = sumcolor.sum()
        img.save(f"{self.pathphoto}/seat4.jpg")
        self.grab.grab(box).save(f"{self.pathphoto}/seat44.jpg")
       
        return sumcolor   
    def GetSeat5(self):
        box = (581,397,581+63,397+10)
        img = ImageOps.grayscale(self.grab.grab(box))
        sumcolor = array(img.getcolors())
        sumcolor = sumcolor.sum()
        img.save(f"{self.pathphoto}/seat5.jpg")
        self.grab.grab(box).save(f"{self.pathphoto}/seat55.jpg")
      
        return sumcolor      
    def GetSeat6(self):
        box = (682,397,682+63,397+10)
        img = ImageOps.grayscale(self.grab.grab(box))
        sumcolor = array(img.getcolors())
        sumcolor = sumcolor.sum()
        img.save(f"{self.pathphoto}/seat6.jpg")
        self.grab.grab(box).save(f"{self.pathphoto}/seat66.jpg")
 
        return sumcolor    
    def GetAllseat(self):
        self.GetSeat1()
        self.GetSeat2()
        self.GetSeat3()
        self.GetSeat4()
        self.GetSeat5()
        self.GetSeat6()
    def clearTable(self):
        self.MouseClick((225,536))
        time.sleep(0.2)
        self.MouseClick((325,536))
        time.sleep(0.2)
        self.MouseClick((425,536))
        time.sleep(0.2)
        self.MouseClick((525,536))
        time.sleep(0.2)
        self.MouseClick((625,536))
        time.sleep(0.2)
        self.MouseClick((725,536))
        print("===Clear Table===")
    def ProcessBot(self):
        self.CheckFood()
        print(self.FoodOnhand)
        time.sleep(5)
        if self.GetSeat1() != self.Blank_1:
            if self.GetSeat1() in self.SushiType:
                print(f"Table 1 need {self.SushiType[self.GetSeat1()]}")
                self.MakeFood(self.SushiType[self.GetSeat1()])
        
        if self.GetSeat2() != self.Blank_2:
             if self.GetSeat2() in self.SushiType:
                print(f"Table 2 need {self.SushiType[self.GetSeat2()]}")
                self.MakeFood(self.SushiType[self.GetSeat2()])
                
        if self.GetSeat3() != self.Blank_3:
            if self.GetSeat3() in self.SushiType:
                print(f"Table 3 need {self.SushiType[self.GetSeat3()]}")
                self.MakeFood(self.SushiType[self.GetSeat3()])

        if self.GetSeat4() != self.Blank_4:
            if self.GetSeat4() in self.SushiType:
                print(f"Table 4 need {self.SushiType[self.GetSeat4()]}")
                self.MakeFood(self.SushiType[self.GetSeat4()])

        if self.GetSeat5() != self.Blank_5:
            if self.GetSeat5() in self.SushiType:
                print(f"Table 5 need {self.SushiType[self.GetSeat5()]}")
                self.MakeFood(self.SushiType[self.GetSeat5()])

        if self.GetSeat6() != self.Blank_6:
            if self.GetSeat6() in self.SushiType:
                print(f"Table 6 need {self.SushiType[self.GetSeat6()]}")
                self.MakeFood(self.SushiType[self.GetSeat6()])
        
        self.clearTable()

            
bot = Mybot()
bot.StarGame()
while True:
    if keyboard.is_pressed('q'):
        print("STOP BOT")
        break
    time.sleep(0.3)
    bot.ProcessBot()





