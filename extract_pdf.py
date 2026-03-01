import sys
try:
    import fitz # PyMuPDF
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pymupdf"])
    import fitz

doc = fitz.open(sys.argv[1])
text = ""
for page in doc:
    text += page.get_text()

with open("extracted.txt", "w", encoding="utf-8") as f:
    f.write(text)
print("done")
