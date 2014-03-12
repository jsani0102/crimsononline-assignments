import json
from PIL import Image

class Article:
    def __init__(self, headline, content, author, related_image=None):
        self.headline = headline
        self.content = content
        self.author = author
        self.related_image = related_image

    def show(self):
        print self.content
        if (self.related_image):
            image = Image.open(self.related_image)
            image.show()

    def save(self):
        f = open(self.headline + "-" + self.content + "-" self.author + "-" self.related_image, 'w') # verbose for very, very rare collisions
        dict = {'headline': self.headline, 'content': self.content, 'author': self.author, 'related_image': self.related_image}
        f.write(json.dumps(dict))
        f.close()

    @classmethod
    def load(cls, filename):
        try:
            f = open(filename, 'r')
            new_dict = json.loads(f.read())
            return Article(new_dict['headline'], new_dict['content'], new_dict['author'], new_dict['related_image'])
        except IOError:
            print "File does not exist!"     

    '''
    Question 2a
        Properties:
            - headline
            - content
            - creator (author)
        Methods:
            - show (print contents)
            - save (save to text file)

    Question 2b
        Methods:
            - Load article from text file

    Question 2d
        Properties:
            - related_image
        Methods:
            - modify save to save info about related picture (if it exists)
            - modify load to load info about related picture (if it exists)
            - modify show to also show the related picture (if it exist)
    '''

class Picture:
    '''
    Question 2c
        Properties:
            - image_file (path to original image relative to this file)
            - creator (photographer)
         Methods
            - show (show image)
    '''

    def __init__(self, filename, photographer):
        self.image_file = filename
        self.photographer = photographer

    def show(self):
        image = Image.open(self.filename)
        image.show()    
