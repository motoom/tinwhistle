
import sys
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter, A4, landscape, portrait
from reportlab.lib.units import cm, mm, inch, pica
import os
import codecs

# TODO: ook halfgesloten holes?
# C natural can be played by half-holing the first hole—this can be simpler, especially when playing the octave.
holes = {
    # Eerste octaaf
    "d": "******",
    "e": "*****o",
    "f#": "****oo",
    "g": "***ooo",
    "a": "**oooo",
    "b": "*ooooo",
    "c": "o**ooo",
    "c#": "oooooo",
    # Tweede octaaf
    "D": "o*****",
    "E": "*****o",
    "F#": "****oo",
    "G": "***ooo",
    "A": "**oooo",
    "B": "*ooooo",
    "C": "o***oo",
    "C#": "oooooo",
    # Derde octaaf
    # "D": "o*****",
}

pagesize = landscape(A4)
horizontal_margin = 16
top_margin = 16

printw = pagesize[0] - horizontal_margin * 2

y = pagesize[1] - top_margin
leftx = x = horizontal_margin
scale = 0.8 # Normaliter 0.8 # Om te verkleinen

# Omvang van de omhullende rectangle van de gaten
flutew = 14
fluteh = 95
holer = 6  # finger hole radius

# Witte ruimte tussen frasen (horizontale groepen van vingerzettingen)
interfrase = 20

# Witte ruimte tussen de noten/vingerzettingen/fluiten
internote = 5

# Text font and sizes
# fontname = "Comic Sans MS"  # Nog eens uitzoeken, moet waarschijnlijk handmatig geladen worden
fontname = "Helvetica"
titlesize = 24
subtitlesize = 12
nootsize = 14


# fn = "simple.txt"
# fn = "coppertinboys.txt"
fn = "grönnens-laid.txt"
if len(sys.argv) > 1:
    fn = sys.argv[1]

pdffn = fn.replace(".txt", ".pdf")
pdf = Canvas(pdffn, pagesize=pagesize)

lines = [line.strip() for line in open(fn).readlines() if line.strip()]
title = lines.pop(0)

pdf.setFont(fontname, titlesize * scale)
y -= titlesize * scale
pdf.drawString(x, y, title)

def drawflute(x, y, note):
    r = (x, y, flutew * scale, fluteh * scale)
    if 0:
        # Show omhullende rect
        pdf.setLineWidth(0.2)
        pdf.rect(*r)

    # De rondjes
    pdf.setLineWidth(1.5 * scale)
    rx = x + (flutew *scale) / 2
    ry = y + fluteh * scale - holer * scale
    for i in range(6):
        pdf.circle(rx, ry, holer * scale, fill=holes[note][i] == "*")
        ry -= holer * scale * 2 + 3 * scale
        if i == 2:
            ry -= 8 * scale

    # De nootnaam
    pdf.setFont(fontname, nootsize * scale)
    y -= (nootsize * 1.5) *scale
    pdf.drawCentredString(x + flutew * scale / 2, y, note)
    if note[0] in "ABCDEFG":
        y += (nootsize * 0.8) *scale
        pdf.drawCentredString(x + flutew * scale / 2, y, "+")


for line in lines:
    if "-" in line: # Regel met vingerzettingen
        print("\nZetting", line)
        y -= fluteh * scale
        frases = [frase.strip() for frase in line.split("-")]
        for frase in frases:
            if not frase:
                continue
            print("  Frase", frase)
            notes = [note.strip() for note in frase.split(" ") if note]
            print("  Notes", notes)
            for note in notes:
                print("    Note", note)
                drawflute(x, y, note)
                x += (flutew + internote) * scale
            x += interfrase * scale # lege ruimte tussen frases
        x = leftx
        y -= 56 * scale # 56 = ruimte boven de fluitafbeelding, wat witruimte voor lyrics
    else:
        # Tussentitel ('Verse', 'Chorus' etc)
        pdf.setFont(fontname, subtitlesize * scale)
        y -= (subtitlesize * 1.5) *scale
        x = leftx
        pdf.drawString(x, y, line)
        y -= 22 * scale
        print("\nDeel", line)

# print(title)
# print(lines)

pdf.showPage()
pdf.save()
os.system(f'open "{pdffn}"')
