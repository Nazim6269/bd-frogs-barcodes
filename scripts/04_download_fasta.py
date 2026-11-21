
import time

from Bio import Entrez


Entrez.email = "nazimdev10022001.com"
query = "Anura[Organism] AND Bangladesh[All Fields] AND 16s[All Fields]"

handle = Entrez.esearch(db="nucleotide",term=query,retmax=300)
ids = Entrez.read(handle)["IdList"]
handle.close()

handle =  Entrez.esummary(db="nucleotide",id=",".join(ids))
records = Entrez.read(handle)
handle.close()

# Keep the longest 16S sequence for each species
best ={}
for r in records:
    title= r["Title"]
    words = title.split()
    name = words[0] + " " + words[1]
    length = int(r["Length"])

    is_16s = ("16S" in title) or ("large subunit ribosomal RNA" in title)
    good_length = 300 <=length <=2000
    real_species = words[1] not in ("sp.", "cf.", "aff.")

    if is_16s and good_length and real_species:
        if name not in best or length >= best[name][1]:
            best[name] = (r["Id"], length, r["Caption"])

print("Species with a representative",len(best))

# Download them as FASTA
out = open("data/frog_16s.fasta","w")
for name,(seq_id,length,acc) in sorted(best.items()):
    handle = Entrez.efetch(db='nucleotide',id=seq_id,rettype='fasta',retmod='text')
    fasta = handle.read()
    handle.close()
    lines = fasta.split("\n")
    lines[0] = ">" + name.replace(" " , "_") + "|" + acc
    out.write("\n".join(lines))
    print("Saved",name,length, "bases",acc)
    time.sleep(0.4)
out.close()
print("saved data/frog_16s.fasta")
