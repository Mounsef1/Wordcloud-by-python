
import os






class frequencies :
    
    ponctuation =['!','’','"',"'",'#','$','%','&','(',')','*','+',',','.','/',':',';','<','=','>','?','[',']','^','_','{','}','|',']','\n','\t']

    def __init__(self, text):
        self.stopwords=open("stopwords_fr.txt",encoding="utf-8").read().split()
        self.stopwords+=open("stopwords_eng.txt",encoding="utf-8").read().split()
        self.text=text
    def add_stopwords(self,word):
        self.stopwords.append(word)
    def remove_stopwords(self,word):
        self.stopwords.remove(word)
    def generate(self):
        data=self.text
        data=' '+data.lower()

   
        for l in self.ponctuation:
            data=data.replace(l,' ')

        for l in self.stopwords:
            data=data.replace(' '+l+' ',' ')
    
        data=data.split()

        for l in data:
            if len(l)==1:
                data.remove(l)
        liste=[]
        for w in data :
            t=0
            for v in liste :
                if w==v[0] :
                    t=1
                    v[1]=v[1]+1
            if t==0 :
                liste.append([w,1])
                
        t=0
        while t==0 :
            t=1
            for i in range(0,len(liste)):
                if  i+1<len(liste) and liste[i][1]<liste[i+1][1] :
                    liste[i], liste[i+1] = liste[i+1], liste[i]
                    t=0
        d=dict()
        for l in liste:
            d[l[0]] = int(l[1])
        return d








