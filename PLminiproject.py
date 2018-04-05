from tkinter import *
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
from urllib.request import urlretrieve
import os


class mainWindow:

    def __init__(self, root):
        
        self.root=root

        #Creating frames
        inputFrame=Frame(root)
        buttonFrame=Frame(root)
        self.outputFrame=Frame(root)
        
        #Displaying frames
        inputFrame.grid(row=0)
        buttonFrame.grid(row=1)
        self.outputFrame.grid(row=2)

        #Contents
        l1=Label(inputFrame, text="Enter username: ")
        self.username=Entry(inputFrame)
        


        #Adding Buttons
        b1=Button(buttonFrame, text="No. of followers", command=lambda: self.cookSoup(1))
        b2=Button(buttonFrame, text="List of followers", command=self.lifers) #Sandhya will handle
        b3=Button(buttonFrame, text="Analysis of likes", command=self.likes) #Sandhya will handle
        b4=Button(buttonFrame, text="No. of following", command=lambda: self.cookSoup(4))
        b5=Button(buttonFrame, text="No. of posts", command=lambda: self.cookSoup(5))
        b6=Button(buttonFrame, text="Download Images", command=self.create_window)
        l1.grid(row=0)
        self.username.grid(row=0, column=1)
        b1.grid(row=0)
        b2.grid(row=1, column=0)
        b3.grid(row=2, column=0)
        b4.grid(row=0, column=1)
        b5.grid(row=1, column=1)
        b6.grid(row=2, column=1)

    def cookSoup(self, choice):
        
        #Cooking soup
        self.user=self.username.get()
        
        
        chrome_path=r"C:\webdrivers\chromedriver.exe"
        driver=webdriver.Chrome(chrome_path)
        driver.get("https://www.instagram.com/"+self.user+"/")
        
        self.soup=BeautifulSoup(driver.page_source, 'lxml')
        items=self.soup.find_all('span', class_='_fd86t')

        if(choice==1):
            op=Label(self.outputFrame, text="No. of followers: "+items[1].text)
            op.grid(row=0)

        elif(choice==4):
            op=Label(self.outputFrame, text="No. of following: "+items[2].text)
            op.grid(row=0)

        elif(choice==5):
            op=Label(self.outputFrame, text="No. of posts: "+items[0].text)
            op.grid(row=0)
    

    def lifers():
        pass

    def likes():
        pass

    def create_window(self):
        #Creating new window
        window=Toplevel(self.root)

        #Widgets for new window
        l2=Label(window, text="Enter URL: ")
        self.giveURL=Entry(window)
        b7=Button(window, text="Download", command=self.downimg)
        self.statusFrame=Frame(window)

        l2.grid(row=0)
        self.giveURL.grid(row=0, column=1)
        b7.grid(row=1, columnspan=2)
        self.statusFrame.grid(row=2, columnspan=2)

    def downimg(self):
        chrome_path=r"C:\webdrivers\chromedriver.exe"
        driver=webdriver.Chrome(chrome_path)
        
        driver.get(self.giveURL.get())
        soup=BeautifulSoup(driver.page_source, 'lxml')
        
        metaTag = soup.find_all('meta', {'property':'og:image'})
        imgURL = metaTag[0]['content']
        fileName = datetime.datetime.now().strftime("%Y-%m-%d_%H"+"h"+"%M"+"m"+"%S"+"s") + '.jpg'
        urlretrieve(imgURL, fileName)

        l4=Label(self.statusFrame, text="Download completed.")
        l4.grid(row=0)

    

root=Tk()
obj=mainWindow(root)
root.mainloop()
