class News_Article:
    '''
    News_Article class to define News_Article Objects
    '''
    def __init__(self, id, poster, url_link, description, published_date, content):
        self.id = id
        self.poster = poster
        self.url_link = url_link
        self.description = description
        self.published_date = published_date
        self.content = content
