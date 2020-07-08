# BEGIN (write your solution here)
def to_rna(items):
    dict_r = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U',
    }
    result = []
    for i in items:
          result.append(i.replace(i, dict_r[i]))
    print (''.join(result))
# END

to_rna('ACGTGGTCTTAA')