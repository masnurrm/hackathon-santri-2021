import factory
from factory import fuzzy
import factory.django
from .models import CustomUser

diseases = ('Abdominal Aortic Aneurysm', 'Acanthamoeba Infection', 'ACE (Adverse Childhood Experiences)', 'Acinetobacter Infection', 'Acquired Immune Deficiency Syndrome (AIDS)', 'Acute Flaccid Myelitis', 'Adenovirus Infection', 'Adenovirus Vaccination', 'ADHD', 'Adult Vaccinations')

class CustomUserFactory(factory.django.DjangoModelFactory):
    
    class Meta:
        model = CustomUser
    
    nama = factory.Faker('name')
    telepon = factory.Faker('phone_number')
    email = factory.Faker('email')
    alamat = factory.Faker('street_address')
    tanggal_lahir = factory.Faker('date')
    penyakit_bawaan = fuzzy.FuzzyChoice(diseases)
