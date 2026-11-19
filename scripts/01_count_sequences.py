from Bio import Entrez

Entrez.email = "nazimdev10022001@gmail.com"

queries = {
    "Anura COI, any country": 'Anura[Organism] AND (COI[Gene] OR COX1[Gene] OR "cytochrome c oxidase subunit I"[Title])',
    "Anura COI, Bangladesh": 'Anura[Organism] AND Bangladesh[All Fields] AND (COI[Gene] OR COX1[Gene] OR "cytochrome c oxidase subunit I"[Title])',
    "Anura 16S, Bangladesh": 'Anura[Organism] AND Bangladesh[All Fields] AND 16S[All Fields]',
}

for label, q in queries.items():
    handle = Entrez.esearch(db='nucleotide',term=q,retmax=0)
    result =  Entrez.read(handle)
    handle.close()
    print(label,":",result["Count"], "sequences")
