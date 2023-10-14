# Zahřívací hodina

1. Malá násobilka
   - naprogramuj hru, která bude zkoušet hráče z malé násobilky
   - příklady se budou generovat náhodně
   - příklady se budou opakovat, dokud hráč nezadá konec
   - hra bude imunní vůči chybnému vstupu
   - na konci se vypíše statistika - kolik příkladů bylo správně a kolik chybně


2. Malá násobilka rozšíření I
   - přidej měření času reakce hráče
   - na konci se vypíše průměrný čas odpovědi (započítej jen správné odpovědi)


3. Malá násobilka rozšíření II
   - hráč na začátku zadá své jméno
   - na konci se přidá řádek do souboru `jmeno_hrace.txt` s počtem správně a chybně a časem
   - přidej začátek programu menu, kdy se hráč rozhodne, jestli hrát hru nebo zobrazit statistiku


## Co je nového:
  - ukážeme si použití `time.time()`

  - __name__ a "__main__"

 - ukážeme si použití `map`

 - můžeme si ukázat matplotlib, jednoduché grafy


## Postup hodiny ... 

1.  Na rozehřátí:

-   Napiš funkci, která bere jako argument otázku a vrací True/False dle toho, zda uživatel zadal ANO nebo NE.
    (jaké odpovědi budou brány jako ano a jaké jako ne si můžeš rozhodnout sama, otázka by se měla opakovat, dokud uživatel nezadá validní odpověď)

-   Napiš funkci, která generuje tří čísla, první dvě jsou náhodná od nuly do deseti, třetí je násobkem prvních dvou.

2. Naprogramuj hru Malá násobilka (viz 1. Malá násobilka)

  - Na ošetření chybného vstupu využij výjimku. Jakou výjimku vrací `int()` pokud argument nelze převést na celé číslo?


3. Vyhledejte si dokumentaci knihovny `time`, zjistěte co vrací `time()`. Přidejte do programu měření času.

4. Přidej ukládání statistik do souboru s jménem hráče.

5. Přidej do programu menu s možností buď hrát hru nebo zobrazit statistiku.

     - jakou výjimku dostaneme při pokusu o čtení neexistujícího souboru?

     - jak převést řetězec čísel oddělených např. čárkou na seznam čísel (ukážeme si `map`)

## Rozšíření

 - ukážeme si nějaké jednoduché hrátky s matplotlib
 

 - rozšíříme login o heslo (soubor se jmény uživatelů a zašifrovanými hesly)
