from shlex import join

from Bio import Entrez


Entrez.email = "nazimdev10022001@gmail.com"

query = "Anura[Organism] AND Bangladesh[All Fields] AND 16s[All Fields]"

# 1. Get all ids for all matching sequences
handle = Entrez.esearch(term=query,db='nucleotide',retmax=300)
ids = Entrez.read(handle)["IdList"]
handle.close()
print("Ids Found: ", len(ids))

# 2. Get short summary for each one
handle = Entrez.esummary(db="nucleotide",id=",".join(ids))
records = Entrez.read(handle)
handle.close()

species = {}
lengths = []

for r in records:
    name = " ".join(r["Title"].split()[:2]) 
    species[name]=species.get(name,0)+1
    lengths.append(int(r["Length"]))


print("Species names found:", len(species))
print("Sequence length: min", min(lengths), "| max", max(lengths))
print()
print("Sequences per species:")

for name,n in sorted(species.items() ,key=lambda t: -t[1]):
    print(" ",n,name)

print()
print("First 5 titles")

for r in records[:5]:
    print(" ", r["Title"])

