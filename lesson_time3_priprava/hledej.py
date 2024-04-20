import gzip


wiki_hesla = [] 

# načteme první dva miliony řádek a uložíme do seznamu
# pokud máte počítač s dostatkem paměti, můžete zkusit načíst všechny řádky
with gzip.open("enwiki-latest-all-titles-in-ns0.gz", "rt", encoding="utf-8") as f:
    cislo_radky = 0
    for radek in f:
        wiki_hesla.append(radek.strip())
        cislo_radky += 1
        if cislo_radky >= 2000000:
            break
        
        
print(len(wiki_hesla))

