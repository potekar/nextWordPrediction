from transformers import T5ForConditionalGeneration, T5Tokenizer


class PredictionModel():
    
    def __init__(self) -> None:
        print("model loading")
        global model_name,tokenizer,model    
        model_name = "model_one"   #ucitavanje modela
        tokenizer = T5Tokenizer.from_pretrained(model_name, legacy=False)       #ucitavanje tokenizera
        model = T5ForConditionalGeneration.from_pretrained(model_name)
        print("model loaded")


    def get_predictions(self,input_string, **generator_args):
        '''
        funkicja run_model uzima za argumente ulazni string tj. recenicu i vraca niz 
        rijeci koje su najvjerovatnije sledece rijeci u tekstu.
        prva 3 elementa u nizu se ubaciju u listu koja se vraca u main funkciju.
        '''
        
        predictions=[]
        
        input_ids = tokenizer.encode(input_string, return_tensors="pt")
        generator_args = {
            "max_length": 100,
            "num_return_sequences": 3,
            "no_repeat_ngram_size": 3,
            "early_stopping": True,
            "num_beams": 5
        }

        res = model.generate(input_ids, **generator_args)
        predictions.append(str(tokenizer.decode(res[0], skip_special_tokens=True)))
        predictions.append(str(tokenizer.decode(res[1], skip_special_tokens=True)))
        predictions.append(str(tokenizer.decode(res[2], skip_special_tokens=True)))
        
        return predictions
    
   