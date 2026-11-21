
from Bio import Entrez


Entrez.email = "nazimdev10022001@gmail.com"

query = "Anura[Organism] AND Bangladesh[All Fields] AND 16s[All Fields]"

handle = Entrez.esearch(db="nucleotide",term=query,retmax=300)
ids = Entrez.read(handle)["IdList"]
handle.close()

handle = Entrez.esummary(db="nucleotide", id=",".join(ids))
records = Entrez.read(handle)
handle.close()

keep = []
for r in records:
    title = r['Title']
    words = title.split()
    genus, epithet = words[0],words[1]
    length = int(r["Length"])

    is_16s = ("16S" in title) or ("large subunit ribosomal RNA" in title)
    good_length = 300 <=length <=2000
    real_species = epithet not in ("sp.", "cf.", "aff.")
    
    if is_16s and good_length and real_species:
        keep.append((genus + " " + epithet, length,r["Caption"]))

species = sorted(set(k[0] for k in keep))
print("Sequences kept:", len(keep), "of", len(records))
print(len(species))
print()
for name in species:
    n = sum(1 for k in keep if k[0] == name)
    print(" ",n,name)

