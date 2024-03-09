
# Operace na seznamech - časová složitost

## Třídění 

1. **Úkol:** Napište funkci, která vytvoří seznam s náhodným obsahem požadované délky. 
 (Hint: využijte funkce `range`, `shuffle` z modulu `random`).

```python
def create_random_list(n):
    ...
```

2. **Společně**: Jak setřídit jednoduše seznam. Navrhneme jednoduchý algoritmus, který vždy
najde nejmenší prvek a dá jej na začátek seznamu. 

3. **Úkol**: Zkuste si navržený algoritmus na jednoduché třídění naprogramovat, napište funkci, která
vrátí setříděnou kopii seznamu.

```python
def select_sort(input_list):
    ...
```       

4. **Společně**: Napíšeme si společně funkci, která vytváří seznamy různých délek a měří
čas provedení funkce dané parametrem. Vrací slovník dvojic délka seznamu a čas.

5. **Společně**: Pomocí této funkce změříme čas provedení naší třídící funkce `select_sort`.
 Napíšeme si pomocnou funkci `plot`, která časy zobrazí (`matplotlib.plot`). 

6. **Diskuze**: Jaká je časová složitost naší funkce `select_sort`. 

7. **Úkol**: Zjistěte, zda funkce `sorted` funguje rychleji. 

8. **Společně**: Upravme funkci `plot`, aby brala jako paremeter seznam a vykreslila více průběhů času do jednoho obrázku (srovnání `select_sort` a `sorted`).

## Vsuvka - lambda funkce

9. **Společně**: Co jsou to lambda funkce a jak se používají.

## Základní operace na seznamech

10. **Společně**: Kolik času stojí zjištění délky seznamu (`len`), diskuze různých seznamových operací.

11. **Úkol**: Vyzkoušejte, kolik času stojí další operace - získání i-tého prvku, přidání prvku na konec seznamu, operátor `in`, metody `insert`, `index`, smazání prvku `del`.

12. **Společně**: Diskuze konstatní vs. lineární čas, které operace patří kam. Vytvoření obrázku pomocí `plot`.


## Hledání v setříděném seznamu 

13. **Úkol**: Z `http://dumps.wikimedia.org/enwiki/latest/enwiki-latest-all-titles-in-ns0.gz` si stáhněte soubor `enwiki-latest-all-titles-in-ns0.gz`. Otevřeme jej pomocí modulu `gzip`.

```python
import gzip

with gzip.open("enwiki-latest-all-titles-in-ns0.gz", "rt") as f:
    for line in f:
        ...   
```

Načtěte řádky souboru do seznamu a zjistěte kolik jich je.

14. **Úkol**: Vymyslete si vlastní titulek, např. Prague, Vltava, PyLadies, PyBoys. Zjistěte, zda je titulek obsažen v seznamu a změřte, kolik času toto zjištění zabere (jen zjištění, bez načtení seznamu).

15. **Diskuze**: Jak hledat rychleji? Můžeme nějak využít informace, že je seznam setříděný? Společný návrh algoritmu. 

16. **Úkol**: Naprogramujte navržené hledání v seznamu, zjisti čas, který zabere. Je rychlejší než použit `in`?

