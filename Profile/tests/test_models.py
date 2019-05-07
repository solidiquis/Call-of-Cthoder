from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from CallofCthoder.settings import STATIC_DIR, MEDIA_ROOT
from Profile.models import AboutMe, Projects, Resume, ContactInformation

class AboutMeTestCase(TestCase):
    """
    Unit-test for AboutMe model.
    """

    def setUp(self):
        """
        Instantiates a temporary AboutMe object. A mock of the image field is
        made using an instance of the SimpleUploadFile class.
        """
        with open(STATIC_DIR + '/test_files/test_image.png', 'rb') as image:
            test_image = image.read()

        profile_pic = SimpleUploadedFile(
            name='test_image.png',
            content=test_image,
            content_type='image/png',
            )

        test_object = AboutMe.objects.create(
            description='test description',
            profile_picture=profile_pic,
            )

    def test_AboutMe(self):
        """
        Checks validity of all object fields as well as whether the object is an
        instance of the proper class.
        """
        about_me = AboutMe.objects.get(description='test description')
        self.assertIsInstance(about_me, AboutMe)
        self.assertEqual(about_me.description, 'test description')
        self.assertIsNotNone(about_me.profile_picture)

class ProjectsTestCase(TestCase):
    """
    Unit-test for Projects model.
    """
    def setUp(self):
        """
        Instantiates a Projects object. A mock of the image field is made using
        an instance of the SimpleUploadFile class.
        """
        with open(STATIC_DIR + '/test_files/test_image.png', 'rb') as image:
            test_image = image.read()

        project_pic = SimpleUploadedFile(
            name='test_image.png',
            content=test_image,
            content_type='image/png',
            )

        Projects.objects.create(
            title='test title',
            summary='test summary',
            project_picture=project_pic,
            )

    def test_Projects(self):
        """
        Checks validity of all object fields as well as whether the object is an
        instance of the proper class.
        """
        project = Projects.objects.get(title='test title')
        self.assertIsInstance(project, Projects)
        self.assertEqual(project.title, 'test title')
        self.assertEqual(project.summary, 'test summary')
        self.assertIsNotNone(project.project_picture)

class ResumeTestCase(TestCase):
    """
    Unit-test for Resume model.
    """
    def setUp(self):
        """
        Instantiates a Resume object. A mock of the file field is made using
        an instance of the SimpleUploadFile class.
        """
        with open(STATIC_DIR + '/test_files/sample.pdf', 'rb') as pdf:
            sample_pdf = pdf.read()

        pdf = SimpleUploadedFile(
            name='sample.pdf',
            content=sample_pdf,
            content_type='pdf',
            )

        Resume.objects.create(resume_pdf=pdf)

    def test_Resume(self):
        """
        Checks validity of all object fields as well as whether the object is an
        instance of the proper class.
        """
        resume = Resume.objects.all().first()
        self.assertIsInstance(resume, Resume)
        self.assertIsNotNone(resume.resume_pdf)

class ContactInformationTestCase(TestCase):
    """
    Unit-test for ContactInformation model.
    """
    def setUp(self):
        ContactInformation.objects.create(
            email='test@gmail.com',
            github='https://github.com/',
            linkedin='https://www.linkedin.com/',
            )

    def test_ContactInformation(self):
        """
        Checks validity of all object fields as well as whether the object is an
        instance of the proper class.
        """
        contact_info = ContactInformation.objects.get(email='test@gmail.com')
        self.assertIsInstance(contact_info, ContactInformation)
        self.assertEqual(contact_info.email, 'test@gmail.com')
        self.assertEqual(contact_info.github, 'https://github.com/')
        self.assertEqual(contact_info.linkedin, 'https://www.linkedin.com/')
