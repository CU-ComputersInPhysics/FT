# Fourierova transformace

- Naprogramujte diskrétní Fourierovu transformaci pro zadaný signál (pole) se zadanou vzorkovací frekvencí.
- Zanalyzujte a vykreslete výkonové spektrum všechny signály ze souboru [signals.py](signals.py). K tomu budete potřebovat knihovny [sounddevice](https://python-sounddevice.readthedocs.io) a [soundfile](https://pypi.org/project/soundfile/), které nainstalujete z příkazové řádky příkazem
```python -m pip install sounddevice soundfile``` (Windows)
```pip install sounddevice soundfile``` (Linux, Mac)
Signály obsahují
    - superpozici tří harmonických signálů o frekvencích 440 Hz, 550 Hz a 660 Hz,
    - hlásky a, e, i, o, u,
    - "chirp sound" vzniklý při převedení gravitačních vln ze splynutí dvou černých děr na zvuk.
Poslední uvedený signál analyzujte v plovoucím okně délky $N_W=2000$ bodů. Pro každé okno určete výkonové spektrum a následně ho vykreslete do konturového grafu (spektrogamu), ve kterém na ose $x$ bude čas, na ose $y$ frekvence a barvou bude znázorněn výkon.