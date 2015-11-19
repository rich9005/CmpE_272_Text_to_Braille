import itertools
def slicefile(filename, start, end):
    lines = open(filename)
    return itertools.islice(lines, start, end)
i=0
#while 1:
#   lines= file.read("Huckleberry.txt")
#   if not lines:
#     break
#   for line in slicefile("Huckleberry.txt",i,i+5):
#      print line
#out = open("meh1.txt","w");
for line in slicefile("Huckleberry.txt",i,i+5):
 i=i+5
 print line
