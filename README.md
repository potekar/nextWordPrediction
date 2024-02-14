README

Aplikacija za Predikciju Sledeće Rijeci

1. Opis:
   Ovaj Python skript implementira aplikaciju za predikciju sledeće reči (NWP) koristeći unapred obučen T5. Aplikacija korisnicima pruža sugestije za sledeću reijč na osnovu teksta koji korisnik unese. Koristi grafički korisnički interfejs (GUI) koji je izgrađen pomoću customtkinter modula.

2. Zahtevi:
   - Python 3.x
   - customtkinter modul (Proverite da li je instaliran ili je uključen u direktorijum projekta)
   - transformers modul 
   - Unapred obučen T5 model i tokenizator (model_one u ovom slučaju)

3. Korišćenje:
   - Proverite da su svi potrebni biblioteke instalirane.
   - Pokrenite skriptu.
   - Počnite da kucate u polje za unos teksta koje je dostupno u GUI-ju.
   - Aplikacija će neprekidno predviđati sledeće reč(i) na osnovu unetog teksta.
   - Kliknite na bilo koju od predloženih reči da biste ih dodali u uneti tekst.
   - Nastavite da kucate i birate prijedloge po želji.

4. Fajlovi:
   - main.py: Glavna Python skripta koja sadrži kod aplikacije za predikciju sledeće reči.
   - customtkinter.py: Custom modul koji pruža prilagođen izgled i funkcionalnost za tkinter GUI-je.
   - model_one (direktorijum): Sadrži unapred obučen T5 model i tokenizator koji se koriste za predikciju sledeće reči.

5. Detalji Implementacije:
   - Skripta uvozi potrebne module uključujući customtkinter za GUI, i T5ForConditionalGeneration i T5Tokenizer iz transformers biblioteke za NWP funkcionalnost.
   - Funkcija run_model generiše predikcije za sledeće reči na osnovu unetog teksta koristeći učitani T5 model.
   - GUI je kreiran koristeći customtkinter sa poljem za unos korisničkog teksta i dugmadima za prikaz sugestija za predikciju.
   - Predviđanja se dinamički ažuriraju dok korisnik kucka.
   - Skripta se izvršava u kontinuiranoj petlji kako bi se održavalo ažuriranje predviđanja i GUI-ja.
   - Po zatvaranju prozora GUI-ja, skripta se isključuje bez problema.

6. Napomene:
   - Preporučuje se pokretanje skripte u okruženju sa podrškom za GPU za brže zaključivanje, posebno sa većim modelima.

7. Zasluge:
   - Ova skripta se zasniva na Hugging Face Transformers biblioteci za NLP zadatke i customtkinter modulu za prilagođavanje GUI-ja.
