# Lineární a kvadratická časová složitost

1. **Úkol**: Napište funkci, která dostane na vstupu řetězec a vrátí slovník
četností výskytů jednotlivých písmen.
```python
def count_letters(input_string):
    ... 
```

2. **Diskuze**: Použili jste ve funkci metodu `count`?  Které řešení, se vám víc líbí (s `count` nebo bez)? 

3. **Společně**: Naprogramujeme i druhou variantu (s count/bez count).

4. **Diskuze**: Co je to program a co je to algoritmus? Jaký je algoritmus/ postup v programu na četnost výskytů písmen.

5. **Společně**: Vytvořme krátký program, měřící čas potřebný na zjištění četností písmen v řetězci "Hello, PyLadies!" 

6. **Diskuze**: Jaký je rozdíl v časech dvou variant programu? Vadí nám to? Dnešní počítače pracují rychle, vadí nám pomalejší řešení, když se jedná o sekundy?
Kolikrát musím řetězec projít v první a druhé variantě?

7. **Úkol**: Stáhněte a rozbalte si soubor `bible_part.txt.zip`. Napište program, který zjistí, kolik má soubor řádek a znaků.

8. **Úkol**: Napiště pomocnou funkci, která načte ze souboru `bible_part.txt` požadovaný počet řádek. Načtený text vrátí jako jeden řetězec.

9. **Úkol**: Zjistěte, kolik času je potřeba na zjištění četností písmen na prvním řádku (souboru `bible_part.txt`) - pro obě varianty funkce `count_letters`.

10. **Diskuze**: Kolik času bude potřeba pro celý soubor? (Předpokládejme, že řádky jsou stejně dlouhé - stačí nám odhad.)

11. **Úkol**: Zkuste si několik variant velikosti vstupu (počtu řádků, např. 10, 20, 100 řádek) pro obě varianty? Jak to vypadá s časem?

12. **Společně**: Napíšeme funkci, která pro danou funkci vytvoří pole časů odpovídající vstupům  10 až 100 řádek s krokem 10. Zavoláme ji pro obě varianty funkce (**BACHA**: funkce se dá předávat jako parametr, to je novinka.) a vykreslíme výsledky do grafu (**SIDE EFFECT**: jednoduché použití matplotlib)

13. **Když zbyde čas**: Hrátky se souborem. Např. zjistěte 10 nejčastěji se vyskytujících slov.
