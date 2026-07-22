from pathlib import Path
p=Path(r'c:/Users/bugra/bugthe/_data/publications.yml')
text=p.read_text(encoding='utf-8')
for i,l in enumerate(text.splitlines(), start=1):
    print(f"{i:03d}: {l}")
