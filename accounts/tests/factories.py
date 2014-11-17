from accounts.models import User
import factory


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = 'john'
    username = "jesusanaya"
    email = "jesus.anaya@test.com"
    photo = factory.django.ImageField(color='blue', filename='image.png')
    biography = "Ola ke ase"
    google_plus = "http://plus.google.com/test"
