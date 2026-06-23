def descendentes(a):
  if a[1] == [] :
    return []
  else :
    return [ nm for nm, _ in a[1] ] +\
           [ nm for f in a[1] for nm in descendentes(f) ]

arvore = ()
print(descendentes(arvore))