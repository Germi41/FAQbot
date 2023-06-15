## FAQbot skript v.0.1
Skript for testing FAQbot in Kiwi

### How to run:

Program require one argument `lang` which define which language version you want to test (`cz` or `en`)

```commandline
python3 faqbot.py <lang>
```


-----------------
### Upcoming version:

### FAQbot skript v.0.2
Skript for testing FAQbot in Kiwi

### What:
- Get responses from chatbot API to predefined answers or upload your own txt file with inputs
- Upload responses (and your own inputs) to testing sheet to manually review each input and corresponding reply

### How to run:

1. To run skript only for predefined inputs use following commands:
    ```commandline
    python3 faqbot.py
    ```

2. To run skript only for your own inputs use following commands:
    ```commandline
    python3 faqbot.py <yourfilename.txt>
    ```