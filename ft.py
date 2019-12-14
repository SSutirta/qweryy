import os
import io
import fasttext

files = []
file1 = io.open("text.txt", "w", encoding="utf-8")
for r, d, f in os.walk('D:'):
    for file in f:
        file1.write(file+"\n")
		#files.append( file + "\n")
#for f in files:
	#file1.writelines(f)
file1.close()
model = fasttext.train_unsupervised("text.txt", model='skipgram')

model.get_nearest_neighbors('ana', k=100)
print(model['ana'])