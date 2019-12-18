import os
import io
import fasttext

#files = []
#file1 = io.open(r"C:\Users\AlnthraevaN\Documents\Skripsi\text.txt", "w", encoding="utf-8")
#for r, d, f in os.walk('D:'):
#    for file in f:
#        file1.write(r + '\\' + file + "\n")
		#files.append( file + "\n")
#for f in files:
	#file1.writelines(f)
#file1.close()


model = fasttext.load_model(r"C:\Users\AlnthraevaN\Documents\Skripsi\cc.en.300.bin")

model.get_nearest_neighbors('dog', k=100)
#print(model['ana'])