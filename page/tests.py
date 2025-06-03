from django.test import SimpleTestCase
from django.urls import reverse
from django.test import TestCase
from .models import Authors

class AboutPaperTest(SimpleTestCase):
    
    def setUp(self):
        self.get_url = reverse('papers')
        
    
    
    def test_url_exists_at_correct_location(self):
        res = self.client.get(self.get_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'papers.html')
        
class AboutProjectTest(SimpleTestCase):
    
    def setUp(self):
       self.get_url = reverse('projects')
       
       
    def test_url_exists_at_correct_location(self):
        res =   self.client.get(self.get_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'projects.html')

class AboutTeamTest(SimpleTestCase):
    def setUp(self):
        self.get_url = reverse('team')
    
    def test_url_exists_at_correct_location(self):
        res = self.client.get(self.get_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res,'team.html')
        

 # test database
     
class AuthorsListTest(TestCase):
    
    def test_list(self):
        url = reverse('authors')
        res = self.client.get(url)
        self.assertTemplateUsed(res,'authors.html')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context.get('list_authors').count(),0)
        
        
        p = Authors.objects.create(
             first_name="John",
             last_name="Doe",
             bio="A test author."
        )
            
        res = self.client.get(reverse('authors'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.context.get('list_authors').count(),1)
        self.assertEqual(res.context.get('list_authors').first(), p)