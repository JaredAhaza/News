from django.test import TestCase
from .models import Editor,tags,Article

# Create your tests here.
class EditorTestClass(TestCase):

    def setUp(self):
        self.jared = Editor(first_name = 'Jared', last_name = 'Ahaza', email='jared@moringaschool.com')
    
#testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.jared,Editor))

#testing saving method
    def test_save_method(self):
        self.jared.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class ArticleTestClass(TestCase):

    def setUp(self):
        #Creating a new editor and saving it
        self.jared=Editor(first_name = 'Jared',last_name = 'Ahaza',email = 'jared@moringaschool.com')
        self.jared.save_editor

        #creating new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()


        self.new_article(titla = 'Test Article',post = 'This is a random test post',editor = self.jared)
        self.new_article.save()


    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all.delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)