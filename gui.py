import customtkinter

class GUI:
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('blue')

    global root,usertext,pOne,pTwo,pThree
    
    root=customtkinter.CTk()
    root.title('NWP')
    root.geometry('1024x480')
    usertext=customtkinter.StringVar(root)
    pOne=customtkinter.StringVar()
    pTwo=customtkinter.StringVar()
    pThree=customtkinter.StringVar()
    
    def __init__(self) -> None:
        print("loading gui")
        def setEntry(predictVlaue,entryField):
            '''
            funkcija setEntry(predictValue) koristi se za dodavanje predloženih riječi na kraj unijetog 
            teksta u polju za unos teksta u GUI-ju. Pored toga, funkcija pomoću icursor funkcije postavlja 
            kursor na kraj unijetog teksta kako bi korisnik mogao da nastavi unos nakon dodavanja predložene reči.
            '''
            usertext.set(usertext.get()+' '+ predictVlaue)
            entryField.icursor(len(usertext.get()))
            return
        
        #formiranje GUI elemenata
        frame=customtkinter.CTkFrame(master=root)
        frame.pack(pady=20,padx=60,fill='both',expand=True)

        label=customtkinter.CTkLabel(master=frame,text='Next Word Prediction',font=("Roboto",34))
        label.pack(pady=50)

        entry=customtkinter.CTkEntry(master=frame,placeholder_text="Start typing...",width=600,font=('Roboto',18),textvariable=usertext)
        entry.pack(pady=5)

        predictionOne=customtkinter.CTkButton(master=frame,textvariable=pOne,font=('Roboto',18),command=lambda:setEntry(predictVlaue=pOne.get(),entryField=entry))
        predictionOne.pack(side='left',padx=(100,5))

        predictionTwo=customtkinter.CTkButton(master=frame,textvariable=pTwo,font=('Roboto',18),command=lambda:setEntry(predictVlaue=pTwo.get(),entryField=entry))
        predictionTwo.pack(side='left',padx=(150,5))

        predictionThree=customtkinter.CTkButton(master=frame,textvariable=pThree,font=('Roboto',18),command=lambda:setEntry(predictVlaue=pThree.get(),entryField=entry))
        predictionThree.pack(side='left',padx=(150,5))
        
        
    def updateData(self,data):
        pOne.set(data[0])
        pTwo.set(data[1])
        pThree.set(data[2])
        root.update()
        
    def getData(self):
        return str(usertext.get())
    
    def checkState(self):
        try:
            if( 'normal'!=root.state()):
                print('gui closed, exiting')
                exit(0) #provjeava se da li je prozor otvoren, ako nije program se gasi
        except:
            exit()

    