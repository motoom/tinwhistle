# Tinwhistle

Genereer PDF-vingerzettingsdiagrammen voor de D-whistle (tinfluit).

## Installatie

```bash
pip install reportlab
```

## Gebruik

```bash
python tabs.py [invoerbestand.txt]
```

De gegenereerde PDF wordt automatisch geopend.

## Invoerformaat

```
Titel van het liedje
Ondertitel (optioneel)

[Sectienaam]
d e f# g - a b c# D - E F# G A
```

- Eerste regel: titel
- Noten gescheiden door spaties
- Koppelteken `-` scheidt frasen
- Tekst zonder `-` wordt als tussentitel weergegeven

## Ondersteunde noten

| Octaaf | Noten |
|--------|-------|
| Eerste (laag) | d, e, f#, g, a, a#, b, c, c# |
| Tweede (hoog) | D, E, F#, G, A, A#, B, C, C# |

## Voorbeeld

Invoer (`simple.txt`):
```
Titel
Subtitel
d -
e - f g
Tweede subtitel
E - F
D - g
```

Dit genereert een PDF met vingerzettingsdiagrammen waar `*` een gesloten gat is en `o` een open gat.

## Licentie

MIT License - Michiel Overtoom, 2025
