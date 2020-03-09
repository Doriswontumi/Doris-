import random
import sys


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  
  mimic_dict = {}
  f = open(filename, 'r')
  text = f.read()
  f.close()
  words = text.split()
  prev = ''
  for word in words:
    if not prev in mimic_dict:
      mimic_dict[prev] = [word]
    else:
      mimic_dict[prev].append(word)
  
    prev = word
  return mimic_dict
 

def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""

  for unused_i in range(200):
    print (word)
    nexts = mimic_dict.get(word)          
    if not nexts:
      nexts = mimic_dict['']  
    word = random.choice(nexts)
 


def main():
  if len(sys.argv) != 2:
    print ('usage: ./mimic.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
