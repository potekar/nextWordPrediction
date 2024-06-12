print("Loading...")
import customtkinter
from transformers import T5ForConditionalGeneration, T5Tokenizer

model_name = "model_one"   #ucitavanje modela
tokenizer = T5Tokenizer.from_pretrained(model_name, legacy=False)       #ucitavanje tokenizera
model = T5ForConditionalGeneration.from_pretrained(model_name)


def run_model(input_string, **generator_args):
    '''
    funkicja run_model uzima za argumente ulazni string tj. recenicu i vraca niz 
    rijeci koje su najvjerovatnije sledece rijeci u tekstu.
    prva 3 elementa u nizu se dodjeljuju StringVar elementima.
    '''

    global pOne
    global pTwo
    global pThree

    input_ids = tokenizer.encode(input_string, return_tensors="pt")
    generator_args = {
        "max_length": 100,
        "num_return_sequences": 3,
        "no_repeat_ngram_size": 3,
        "early_stopping": True,
        "num_beams": 5
    }

    res = model.generate(input_ids, **generator_args)
    pOne.set(str(tokenizer.decode(res[1], skip_special_tokens=True)))
    pTwo.set(str(tokenizer.decode(res[0], skip_special_tokens=True)))
    pThree.set(str(tokenizer.decode(res[2], skip_special_tokens=True)))
    return

def setEntry(predictVlaue):
    '''
    funkcija setEntry(predictValue) koristi se za dodavanje predloženih riječi na kraj unijetog 
    teksta u polju za unos teksta u GUI-ju. Pored toga, funkcija pomoću icursor funkcije postavlja 
    kursor na kraj unijetog teksta kako bi korisnik mogao da nastavi unos nakon dodavanja predložene reči.
    '''
    global usertext
    global entry
    usertext.set(usertext.get()+' '+ predictVlaue)
    entry.icursor(len(usertext.get()))
    return

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

root=customtkinter.CTk()
root.title('NWP')
root.geometry('1024x480')

usertext=customtkinter.StringVar(root)
pOne=customtkinter.StringVar()
pTwo=customtkinter.StringVar()
pThree=customtkinter.StringVar()



if __name__=="__main__": #main funkcija programa
    
    #formiranje GUI elemenata
    frame=customtkinter.CTkFrame(master=root)
    frame.pack(pady=20,padx=60,fill='both',expand=True)

    label=customtkinter.CTkLabel(master=frame,text='Next Word Prediction',font=("Roboto",34))
    label.pack(pady=50)

    entry=customtkinter.CTkEntry(master=frame,placeholder_text="Start typing...",width=600,font=('Roboto',18),textvariable=usertext)
    entry.pack(pady=5)

    predictionOne=customtkinter.CTkButton(master=frame,textvariable=pOne,font=('Roboto',18),command=lambda:setEntry(predictVlaue=pOne.get()))
    predictionOne.pack(side='left',padx=(100,5))

    predictionTwo=customtkinter.CTkButton(master=frame,textvariable=pTwo,font=('Roboto',18),command=lambda:setEntry(predictVlaue=pTwo.get()))
    predictionTwo.pack(side='left',padx=(150,5))

    predictionThree=customtkinter.CTkButton(master=frame,textvariable=pThree,font=('Roboto',18),command=lambda:setEntry(predictVlaue=pThree.get()))
    predictionThree.pack(side='left',padx=(150,5))

    prevtext=''
    
    print("Loaded.")
    while(True):
        '''
        Ovaj dio koda predstavlja beskonačnu petlju koja kontinuirano osluškuje promijene 
        u tekstu koji korisnik unosi u polje za unos teksta u GUI-ju.
        '''
        text=str(usertext.get())
        if text==prevtext:
            pass
        else:
            run_model(text)

        root.update()   #root.update() metda azurira trenuti prikaz GUI elemenata
        prevtext=text
        try:
            if( 'normal'!=root.state()):exit(0) #provjeava se da li je prozor otvoren, ako nije program se gasi
        except:
            exit()



