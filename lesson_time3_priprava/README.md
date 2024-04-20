
## Hledání v setříděném seznamu 

 **Úkol**: Z `http://dumps.wikimedia.org/enwiki/latest/enwiki-latest-all-titles-in-ns0.gz` si stáhněte soubor `enwiki-latest-all-titles-in-ns0.gz`. Otevřeme jej pomocí modulu `gzip`.

```python
import gzip

with gzip.open("enwiki-latest-all-titles-in-ns0.gz", "rt", encoding="utf-8") as f:
    for line in f:
        ...   
```


