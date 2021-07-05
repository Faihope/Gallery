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
    def test_delete_images(self):
        self.image1.save_image()
        images_record=Image.objects.all()
        self.image1.delete_image()
        self.assertTrue(len(images_record)==0)

    def test_update_image(self):
        image=Image.objects.first()
        new_image=Image.update_image()
        expected_image=f'{new_image}'
        self.assertTrue(expected_image,'new_image')

    def test_search_category(self):
        category=Image.objects.all()
        search_term='food'
        db_term=search_term
        if db_term !=search_term:
            return('no match')

        else:
            return(search_term)





