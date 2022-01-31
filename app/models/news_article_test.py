import unittest # module for testing
from models import news_article

class TestNewsArticles(unittest.TestCase):
    '''
    TestNewsArticles for testing class news_articles
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        # id, title ,poster, url_link, description, published_date, content
        self.new_article = news_article.News_Article(
        '123', 
        'BBc News',
        "https://www.independent.co.uk/news/world/americas/miss-usa-2019-cheslie-kryst-death-b2003891.html",
        "A woman who jumped to her death from a New York City high rise apartment building has been identified as former Miss USA Cheslie Kryst.\r\nThe 2019 pageant winner who had a ninth floor apartment in Man… [+2506 chars]",
         "2022-01-31T05:07:00Z",
        "With a calm that belied their underdog status, the Bengals intercepted Patrick Mahomes and completed a field-goal drive in overtime to end Kansas City’s streak of Super Bowl appearances.")

if __name__ == "__main__":
    unittest.main()