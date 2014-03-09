import datetime
import re

class Content(object):
    '''
    Required properties:
        - title
        - subtitle
        - creator
        - publication date
    Required methods:
        - show
        - matches_url (question 1d)
    '''
    def __init__(self, title, subtitle, creator):
        self.title = title
        self.subtitle = subtitle
        self.creator = creator
        self.publication_date = datetime.date.today()

    def show(self):
        print "<Title: {0}\nSubtitle: {1}\nCreator: {2}\nPublication Date: {3}>"
        .format(self.title, self.subtitle, self.creator, self.publication_date.__str__())

    def matches_url(self, url):
        pattern = r'http://thecrimson.com/(\w+)/(\d{4})/(\d{1,2})/(\d{1,2})/(\w+)'
        return !(re.search(pattern, url) is None)

    '''
    Question 1e
    '''
    @classmethod
    def from_url(c_lst, url):
        matched_content = []

        for i in range(len(c_lst)):

            split_title = c_lst[i].title.split()
            slug = '-'.join(split_title)

            pattern = r'http://thecrimson.com/(\w+)/{0}/{1}/{2}/{3}/'
            .format(c_list[i].publication_date.year, c_list[i].publication_date.month, c_list[i].publication_date.day, slug)
            if (!(re.search(pattern, url) is None): matched_content.append(c_lst[i])
        
        if (len(matched_content) > 1): 
            print "Error - More than one content object matches the URL!"
        else if:
            print "No content matched"    
        else:
            return matched_content[0]

class Article(Content):
    '''
    Required properties:
        - All properties of Content
        - related_image
    Required methods:
        - All methods of Content
    '''
    def __init__(self, title, subtitle, creator, image):
        super(Content, self).__init__(title, subtitle, creator)
        self.related_image = image

    def show(self):
        print "<Title: {0}\n Subtitle: {1}\nCreator: {2}\nPublication Date: {3}\nRelated Image: {4}>"
        .format(self.title, self.subtitle, self.creator, self.publication_date.__str__(), self.related_image)

class Picture(Content):
    '''
    Required properties:
        - All properties of Content
        - image_file
    Required methods:
        - All methods of Content
    '''
    def __init__(self, title, subtitle, creator, image_file):
        super(Content, self).__init__(title, subtitle, creator)
        self.image_file = image_file

    def show(self):
        print "<Title: {0}\n Subtitle: {1}\nCreator: {2}\nPublication Date: {3}\nImage File: {4}>"
        .format(self.title, self.subtitle, self.creator, self.publication_date.__str__(), self.image_file)

'''
Question 1e
'''
def posted_after(c_lst, dt):
    content_before_dt = []
    for content in c_lst:
        if (content.publication_date < dt): content_before_dt.append(content)
    return content_before_dt    