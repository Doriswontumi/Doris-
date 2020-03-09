
def verbing(s):
  length = len(s)
  if length > 2:
    if s[-3:] == 'ing':
      s += 'ly'
    else:
      s += 'ing'
  return s



def not_bad(s):
  notV = s.find('not')
  badV = s.find('bad')
  if (badV > notV):
    return s[:notV] + 'good' + s[(badV+3):]
  return s



def front_back(a, b):
  aV = len(a)//2+(len(a)%2)
  bV = len(b)//2+(len(b)%2)
  return a[:aV]+b[:bV]+a[aV:]+b[bV:]



def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
  print ('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print ('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print ('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
