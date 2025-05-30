from django.test import SimpleTestCase
from django.urls import reverse

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