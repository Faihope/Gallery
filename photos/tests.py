from django.test import TestCase
from photos.models import Image,Location,Category
# Create your tests here.

class ImageTestClass(TestCase):
    #setup method
    def setUp(self):
        self.image1=Image(image="image",name='Flower',description="Nice image")

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image1,Image))

    def test_save_images(self):
        self.image1.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)