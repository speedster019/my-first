# write a file
fw=open('codox.docx', 'w')
fw.write('codox is the book of druids used for studying magic\n')
fw.write('sword of shannara is the the most powerful sword in the four lands\n')
fw.close()

# reading a file
fr=open('codox.docx', 'r')
am=fr.read()
print(am)
fr.close()