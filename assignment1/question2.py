class Article:
    def __init__(self, headline, content, author):
        self.headline = headline
        self.content = content
        self.author = author

    def show(self):
        print self.content

    def save(self):
        f = open(headline + '.py', 'w')
        f.write(content)
        f.close()

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
    pass

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
        self.filename = filename
        self.photographer = photographer

    def show(self):
            
    pass
