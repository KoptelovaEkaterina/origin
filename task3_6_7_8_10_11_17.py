from collections.abc import Sequence
import random

class AbstractSequence(Sequence):

    def __init__(self, alphabet, name, data):
        self._alphabet = alphabet
        self._data = data
        self._name = name

    @property
    def alphabet(self):
        return self._alphabet
    
    @alphabet.setter
    def alphabet(self, value):
        self._alphabet = value

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value

    def __len__(self):
        return  len(self._data)

    def __getitem__(self, key):
        return self._data[key]
    
    def __str__(self):
        return self._data
    
    def __repr__(self):
        return self._data

    def statistics(self):
        d = {}
        for alpha in self:
            d[alpha] = d.get(alpha, 0) + 1
        return d
    
    def parts(self):
        while True:
            yield random.choice(self._alphabet)
            
    def parts_fix(self, l):
        gen = self.parts()
        while True:
            yield ''.join([next(gen) for i in range(l)])

    def parts_not_fix(self, min_len, max_len):
        gen = self.parts()
        while True:
            r = random.randint(min_len, max_len)
            yield ''.join([next(gen) for i in range(r)])
            
    def seq_map(self, f):
        return ''.join(map(f, list(self._data)))

    def seq_map_modified(self, f):
        return (''.join(map(f, list(self._data[1:]), list(self._data))))

class DNA(AbstractSequence):
    
    def __init__(self, data):
        super().__init__("ACGT", "DNA", data)

    nucleotid_to_mass = {"A": 313.21, "C": 289.18, "G": 329.21, "T": 304.2}
    complement = {"A": "U", "G": "C", "U": "A", "C": "G"}
    to_rna = {"A": "U", "G": "C", "T": "A", "C": "G"}
    
    def mass(self):
        masses = [DNA.nucleotid_to_mass[alpha] for alpha in self]
        return sum(masses) - 61.96

    def complemented(self):
        return DNA("".join(reversed([DNA.complement[alpha] for alpha in self])))

    def transcription(self):
        return RNA("".join(reversed([DNA.to_rna[alpha] for alpha in self])))


class RNA(AbstractSequence):
    
    def __init__(self, data):
        super().__init__("ACGU", "RNA", data)
        
    def read():
        with open("triplet_to_protein.txt") as f:
            d = {}
            for line in f:
                alpha, *triplets = line.split()
                for triplet in triplets:
                    d[triplet] = alpha
            return d
        
    RNA_to_code = read()

    nucleotid_to_mass = {"A": 329.21, "C": 305.18, "G": 345.21, "U": 306.17}
    complement = {"A": "U", "G": "C", "U": "A", "C": "G"}

    def mass(self):
        masses = [RNA.nucleotid_to_mass[alpha] for alpha in self]
        return sum(masses) + 159.0

    def complemented(self):
        return RNA("".join(reversed([RNA.complement[alpha] for alpha in self])))

    def translation(self):
        protein = []
        for i in range(len(self)//3-1):
            protein.append(RNA.RNA_to_code[self[3*i:3*(i+1)]])
        return Protein(''.join(protein))
        
class Protein(AbstractSequence):
    def __init__(self, data):
        super().__init__("ACDEFGHIKLMNPQRSTVWY", "Protein", data)
        
    def read():
        with open("mass_protein.txt") as f:
            d = {}
            for line in f:
                alpha, mass = line.split()
                d[alpha] = float(mass)
            return d
        
    code_ta_mass = read()
        
    def mass(self):
        masses = [Protein.code_to_mass[alpha] for alpha in self]
        return sum(masses)

def read_fasta(filename):
    with open(filename) as f:
        name, sequence = None, ""
        for line in f:
            if line.startswith(">"):
                line = line[-1]
                ident, *inf = line[1:-1].split()
                if name is not None and sequence != "":
                    if ident == "DNA":
                        yield DNA(name)
                    elif ident == "RNA":
                        yield DNA(name)
                    elif ident == "Protein":
                        yield Protein(name)
                name = line[1:]
                sequence = ""
            else:
                sequence += line
        if name is not None and sequence != "":
            if ident == "DNA":
                yield DNA(name)
            elif ident == "RNA":
                yield DNA(name)
            elif ident == "Protein":
                yield Protein(name)