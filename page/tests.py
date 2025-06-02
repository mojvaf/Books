from django.test import SimpleTestCase
from django.urls import reverse
from django.test import TestCase
from .models import Authors

class AboutPaperTest(SimpleTestCase):
    
    def setUp(self):
        self.get_url = reverse('papers')
        
    
    
    def test_url_exists_at_correct_location(self):
        r = self.client.get('/papers/')
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, 'papers.html')
        
class AboutProjectTest(SimpleTestCase):
    
    def setUp(self):
       self.get_url = reverse('projects')
       
       
    def test_url_exists_at_correct_location(self):
        r =   self.client.get('/projects/')
        self.assertEqual(r.status_code, 200)
        self.assertTemplateUsed(r, 'projects.html')

class AboutTeamTest():
    def setUp(self):
        self.get_url = reverse('team')
    
    def test_url_exists_at_correct_location(self):
        r = self.client.get('/team/')
        self.assertEqual(r.status_code, 200)
        self.assetTemplateUsed(r,'team.html')
        
###################
 # test data base
###################        
class AuthorsListTest(TestCase):
    
    def test_list(self):
        r = self.client.get(reverse( 'authors'))
        self.assertTemplateUsed(r,'authors.html')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.context.get('list_authors').count(),0)
        
        
        p = Authors.objects.create(
             first_name="John",
             last_name="Doe",
             bio="A test author."
        )
            
        r = self.client.get(reverse('authors'))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.context.get('list_authors').count(),1)
        self.assertEqual(r.context.get('list_authors').first(), p)