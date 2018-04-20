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
        li=Label(inputFrame, text="Enter username: ")
        self.username=Entry(inputFrame)
        self.opString=StringVar()
        self.opString.set("Output will display here")
        lo=Label(self.outputFrame, textvariable= self.opString)

        #Adding Buttons
        b1=Button(buttonFrame, text="User Details", command=self.cookSoup, width=15)
        b3 = Button(buttonFrame, text="Image Details", command=self.likes_window, width=15)
        b6 = Button(buttonFrame, text="Download Images", command=self.create_window, width=15)
        li.grid(row=0)
        self.username.grid(row=0, column=1)
        b1.grid(row=1, columnspan=2)
        b3.grid(row=2, columnspan=2)
        b6.grid(row=3, columnspan=2)
        lo.grid(row=4, columnspan=2)

    def cookSoup(self):
        
        #Cooking soup
        self.user=self.username.get()
        
        chrome_path = r"C:\webdrivers\chromedriver.exe"
        driver=webdriver.Chrome(chrome_path)
        driver.get("https://www.instagram.com/"+self.user+"/")
        
        self.soup=BeautifulSoup(driver.page_source, 'lxml')
        items=self.soup.find_all('span', class_='_fd86t')

        self.opString.set("No. of followers: "+items[1].text+"\nNo. of following: "+items[2].text+"\nNo. of posts: "+items[0].text)

    def likes(self):
        chrome_path = r"C:\webdrivers\chromedriver.exe"
        driver=webdriver.Chrome(chrome_path)
        
        driver.get(self.giveURL.get())
        soup=BeautifulSoup(driver.page_source, 'lxml')

        likes = soup.find_all('span', class_="_nzn1h")
        
        l4=Label(self.statusFrame, text='No. of likes: '+likes[0].text)
        l4.grid(row=0)

        caption = soup.find_all('li', class_="_ezgzd")
        l5=Label(self.statusFrame, text='Caption: '+caption[0].text)
        l5.grid(row=1)

        div = soup.find_all('span', class_='_ha6c6 _6d44r')
        for a in div.findAll('a'):
            a = a.get('href')
        l6=Label(self.statusFrame, text='Time: '+a[0].text)
        l6.grid(row=2)
            
        
    def likes_window(self):
        #Creating new window
        window=Toplevel(self.root)

        #Widgets for new window
        l2=Label(window, text="Enter URL: ")
        self.giveURL=Entry(window)
        b7=Button(window, text="Get Details", command=self.likes)
        self.statusFrame=Frame(window)

        l2.grid(row=0)
        self.giveURL.grid(row=0, column=1)
        b7.grid(row=1, columnspan=2)
        self.statusFrame.grid(row=2, columnspan=2)
        
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
