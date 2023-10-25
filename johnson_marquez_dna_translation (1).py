# -*- coding: utf-8 -*-
"""Johnson_Marquez_DNA_Translation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kcPCTyo2XtJ9qz2ZNMqeMMgG_aNMIWdE
"""

def transcription(dna_sequence):
    complement = {'A':'U','T':'A','C':'G', 'G':'C'}
    mrna = ''.join(complement.get(base, base) for base in dna_sequence)
    return mrna
def translate(mrna):
  condon_table = {
      'UUC':'F','UUC':'F','UUA':'L','UUG':'L',
      'UCU':'S','UCC':'S','UCA':'S','UCG': 'S',
      'UAU':'T','UAC':'T','UAA':'*','UAG':'*',
      'UGU':'C','UGC':'C','UGA':'*','UGG':'T',
      'CUU':'L','CUC':'L','CUA':'L','CUG':'L',
      'CCU':'P','CCC':'P','CCA':'P','CCG': 'P',
      'CAU':'H','CAC':'H','CAA':'H','CAG':'G',
      'CGU':'A','CGC':'A','CGA':'A','CGG':'A',
      'AUU':'LL','AUC':'LL','AUA':'LL','AUG':'M',
      'ACU':'TH','ACC':'TH','ACA':'TH','ACG':'TH',
      'AAU':'A','AAC':'A','AAA':'LY','AAG':'LY',
      'AGU':'SE','AGC':'SE','AGA':'AR','AGG':'AR',
      'GUU':'V','GUC':'V','GUA':'V','GUG':'V',
      'GCU':'AL','GCC':'AL','GCA':'AL','GCG':'AL',
      'GAU':'AS','GAC':'AS','GAA':'G','GAG':'G',
      'GGU':'GL','GGC':'GL','GGA':'GL','GGG':'GL',
  }
  protein=''
  i=0
  while i < len(mrna):
    codon = mrna[i:i+3]
    amino_acid = condon_table.get(codon, 'X')
    if amino_acid == '*':
          break
    protein += amino_acid
    i += 3

  return protein


dna_sequence = input('Enter your DNA sequence:')
print('Your DNA sequence has been transcribed to:',mrna)
mrna = transcription(dna_sequence)
input('Enter your mRNA sequence:')
protein = translate(mrna)
print('Your mRNA sequence into Nucleotide triplets:',protein)