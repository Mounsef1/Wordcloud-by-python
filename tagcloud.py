
from PIL import Image
import random as r
import numpy as np

from scipy.ndimage import gaussian_gradient_magnitude
from frequencies import frequencies
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS

#il faut executer get_frequency avant de generate !!!
#si vous voulez integrer la font_size il faut entrer le max et la min non pas le max seulement!!!!
#pour definir l'object il faut obligatoirement entrer comme parametre le text string et l'image (non pas le chemin)
#toutes configutation ou modification des mots (le texte, les stopwords, ajouter ou enlever) doit etre avant get_frequencies
#toutes configutation ou modification des parametre du cloud (couleur ,image ,police,resolution,taille) doit etre avant generate
#download doit etre apres generate

class one_wordcloud :
    
    def __init__(self,text,image=None,max_font_size=None,min_font_size=None,resolution=1,bgc="black",color=None,contour_width=0):
        self.image=image
        self.text=text
        self.bgc=bgc
        self.data=frequencies(text)
        self.max_font_size=max_font_size
        self.min_font_size=min_font_size
        self.resolution=resolution
        self.color=color
        self.contour_width=contour_width
    
    def add_stopwords(self,word):
        self.data.add_stopwords(word)
    def remove_stopwords(self,word):
        self.data.remove_stopwords(word)
    def get_frequencies(self):
        self.frequency=self.data.generate()
        return self.frequency
    def download(self,d=""):
        self.wc.to_file(d+".jpg");
    def generate(self):
        
        
        self.image = np.array(self.image)
        self.image = self.image[::self.resolution, ::self.resolution] #resolution et taille
        self.image_mask = self.image.copy()

        self.image_mask[self.image_mask.sum(axis=2) == 0] = 255 #white background
        edges = np.mean([gaussian_gradient_magnitude(self.image[:, :, i] / 255., 2) for i in range(3)], axis=0)
        self.image_mask[edges > .10] = 255

        if self.max_font_size!=None and self.min_font_size!=None :
            self.wc = WordCloud( mask=self.image_mask, background_color=self.bgc,
                        max_font_size=self.max_font_size ,
                        min_font_size=self.min_font_size ,
                        random_state=r.seed(), relative_scaling=0,contour_width=self.contour_width)
        else :
            self.wc = WordCloud( mask=self.image_mask, background_color=self.bgc,random_state=r.seed(), relative_scaling=0,contour_width=self.contour_width)

       
        self.wc.generate_from_frequencies(self.frequency)
        if self.color=="S" :
            self.wc.recolor(color_func=ImageColorGenerator(self.image))
        elif self.color!=None :
            self.wc.recolor(color_func=self.color)
        return self.wc
        

#d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
#one=one_wordcloud(Image.open(os.path.join(d, "ggg.jpg")),open(os.path.join(d, 'text2.txt'),encoding="utf-8").read());
#one.resolution=3

#one.bgc="black"
#one.get_frequencies()

#def color_funct(word, font_size, position, orientation, random_state=None,**kwargs):
 #   return "hsl(0, %d%%, 50%%)" % r.randint(50, 100)
#one.color="S"

#plt.figure(figsize=(20, 20))
#plt.imshow(one.generate(), interpolation="bilinear")
#one.download("peeeeeererrrrerere")

#plt.show()


