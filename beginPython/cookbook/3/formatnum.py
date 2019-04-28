ss = {ord('.'):ord(','),ord(','):ord('.')}

print(1234.567)
print(format(1234.567,','))
print(format(1234.567,',').translate(ss))