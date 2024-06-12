import gui
import model

if __name__=="__main__": #main funkcija programa 
    
    
    predictionModel=model.PredictionModel()
    interface=gui.GUI()
    
    prevText=''
    dataList=['','','']
    
    while(True):
        '''
        Ovaj dio koda predstavlja beskonačnu petlju koja kontinuirano osluškuje promijene 
        u tekstu koji korisnik unosi u polje za unos teksta u GUI-ju.
        '''
        inputText=interface.getData()
        
        if prevText==inputText:
            pass
        else:
            dataList=predictionModel.get_predictions(inputText)
        
        interface.updateData(dataList)
            
        prevText=inputText
        
        interface.checkState()

        