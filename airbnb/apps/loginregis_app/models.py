from __future__ import unicode_literals
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.db import models
import re
from django import forms
from django.utils.translation import ugettext_lazy as _
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')
NUMBER_REGEX = re.compile(r'^(\+\d{1,3}[- ]?)?\d{10}$')
ZIPCODE_REGEX = re.compile(r'^\d{5}(?:[-\s]\d{4})?$')

# Create your models here.
class UserManager(models.Manager):
    def login_validator(self,postData):
        errors = []
        if len(self.filter(username=postData['username'])) > 0:
            user = self.filter(username=postData['username'])[0]
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                 errors.append ("Invalid password")
        else: 
            errors.append ("No such user")

        if errors:
            return errors

        return user

    def register_valid(self, postData):
        errors = []
         # -----------------------------------
        if len(postData['username']) < 3:
            errors.append("username fields must be at least 3 characters")
        # -----------------------------------
        if len(postData['first_name']) < 3 or len(postData['last_name']) < 3:
            errors.append("name fields must be at least 3 characters")
        #  -----------------------------------
        if len(postData['password']) < 4:
            errors.append("password must be at least 4 characters")
        #  -----------------------------------           
        if len(postData['address']) < 3:
            errors.append("invalid address")
        #  ----------------------------------- 
        if len(postData['city']) < 1:
            errors.append("invalid city")
        #  ----------------------------------- 
        if len(postData['state']) < 1:
            errors.append("invalid state")
        #  ----------------------------------- 
        if len(postData['zipcode']) < 1:
            errors.append("invalid state")
        #  -----------------------------------
        if len(postData['country']) < 1:
            errors.append("invalid country")
        #  -----------------------------------           
        if not re.match(NAME_REGEX, postData['first_name']) or not re.match(NAME_REGEX, postData['last_name']):
            errors.append('name fields must be letter characters only')
        #  -----------------------------------
        if not re.match(EMAIL_REGEX, postData['email']):
            errors.append("invalid email")
        #  -----------------------------------
        if not re.match(NUMBER_REGEX, postData['phone_number']):
            errors.append("invalid phone number")
        #  -----------------------------------
        if not re.match(ZIPCODE_REGEX, postData['zipcode']):
            errors.append("invalid zipcode")
        #  -----------------------------------
        if len(User.objects.filter(email=postData['email'])) > 0:
            errors.append("email already in use")
        #  -----------------------------------
        if postData['password'] != postData['confirm_password']:
            errors.append("passwords do not match")
        #  -----------------------------------
        if postData['password'] != postData['confirm_password']:
            errors.append("passwords do not match")


        if not errors:
            # hash password
            hashed = bcrypt.hashpw((postData['password'].encode()), bcrypt.gensalt(5))

            new_user = self.create(
                username=postData['username'],
                first_name=postData['first_name'],
                last_name=postData['last_name'],
                phone_number=postData['phone_number'],
                address=postData['address'],
                city=postData['city'],
                state=postData['state'],
                zipcode=postData['zipcode'],
                country=postData['country'],
                bday=postData['bday'],
                email=postData['email'],
                bio=postData['bio'],
                school=postData['school'],
                work=postData['work'],
                password=hashed,
            )
            return new_user

        return errors

class User(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    bday = models.DateField()
    email = models.EmailField()
    bio = models.TextField(max_length=500)
    school = models.CharField(max_length=30, blank=True)
    work = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __repr__(self):
        return "<User object: {} {} {} {} {} {}>".format(self.id, self.email, self.password, self.image, self.created_at, self.updated_at)

LANGUAGE_CHOICES = (
    ('ab', 'Abkhaz'),
    ('ady', 'Adyghe'),
    ('af', 'Afrikaans'),
    ('ak', 'Akan'),
    ('sq', 'Albanian'),
    ('ase', 'American Sign Language'),
    ('am', 'Amharic'),
    ('grc', 'Ancient Greek'),
    ('ar', 'Arabic'),
    ('an', 'Aragonese'),
    ('arc', 'Aramaic'),
    ('hy', 'Armenian'),
    ('ay', 'Aymara'),
    ('ban', 'Balinese'),
    ('eu', 'Basque'),
    ('bew', 'Betawi'),
    ('sh', 'Bosnian'),
    ('br', 'Breton'),
    ('bg', 'Bulgarian'),
    ('yue', 'Cantonese'),
    ('ca', 'Catalan'),
    ('chr', 'Cherokee'),
    ('clc', 'Chickasaw'),
    ('zh', 'Chinese'),
    ('cop', 'Coptic'),
    ('kw', 'Cornish'),
    ('co', 'Corsican'),
    ('crh', 'Crimean Tatar'),
    ('sh', 'Croatian'),
    ('cs', 'Czech'),
    ('da', 'Danish'),
    ('dwr', 'Dawro'),
    ('nl', 'Dutch'),
    ('en', 'English'),
    ('eo', 'Esperanto'),
    ('et', 'Estonian'),
    ('ee', 'Ewe'),
    ('hif', 'Fiji Hindi'),
    ('fil', 'Filipino'),
    ('fi', 'Finnish'),
    ('fr', 'French'),
    ('gl', 'Galician'),
    ('ka', 'Georgian'),
    ('de', 'German'),
    ('el', 'Greek, Modern'),
    ('kl', 'Greenlandic'),
    ('ht', 'Haitian Creole'),
    ('haw', 'Hawaiian'),
    ('he', 'Hebrew'),
    ('hi', 'Hindi'),
    ('hu', 'Hungarian'),
    ('isc', 'Icelandic'),
    ('id', 'Indonesian'),
    ('ia', 'Interlingua'),
    ('iu', 'Inuktitut'),
    ('ga', 'Irish'),
    ('it', 'Italian'),
    ('ja', 'Japanese'),
    ('jv', 'Javanese'),
    ('kbd', 'Kabardian'),
    ('kls', 'Kalasha'),
    ('kn', 'Kannada'),
    ('csb', 'Kashubian'),
    ('km', 'Khmer'),
    ('rw', 'Kinyarwanda'),
    ('ko', 'Korean'),
    ('ku', 'Kurdish'),
    ('lld', 'Ladin'),
    ('ltg', 'Latgalian'),
    ('la', 'Latin'),
    ('ln', 'Lingala'),
    ('liv', 'Livonian'),
    ('jbo', 'Lojban'),
    ('dsb', 'Lower Sorbian'),
    ('mk', 'Macedonian'),
    ('ms', 'Malay'),
    ('ml', 'Malayalam'),
    ('cmn', 'Mandarin'),
    ('gv', 'Manx'),
    ('mi', 'Maori'),
    ('mfe', 'Mauritian Creole'),
    ('gml', 'Middle Low German'),
    ('nan', 'Min Nan'),
    ('mn', 'Mongolian'),
    ('no', 'Norwegian'),
    ('xcl', 'Old Armenian'),
    ('ang', 'Old English'),
    ('fro', 'Old French'),
    ('kaw', 'Old Javanese'),
    ('non', 'Old Norse'),
    ('prg', 'Old Prussian'),
    ('ory', 'Oriya'),
    ('pag', 'Pangasinan'),
    ('pap', 'Papiamentu'),
    ('ps', 'Pashto'),
    ('fa', 'Persian'),
    ('pjt', 'Pitjantjatjara'),
    ('pl', 'Polish'),
    ('pt', 'Portuguese'),
    ('qya', 'Quenya'),
    ('rap', 'Rapa Nui'),
    ('ro', 'Romanian'),
    ('ru', 'Russian'),
    ('sa', 'Sanskrit'),
    ('sco', 'Scots'),
    ('gd', 'Scottish Gaelic'),
    ('sh', 'Serbian'),
    ('sh', 'Serbo-Croatian'),
    ('si', 'Sinhalese'),
    ('sk', 'Slovak'),
    ('sl', 'Slovene'),
    ('es', 'Spanish'),
    ('sw', 'Swahili'),
    ('sv', 'Swedish'),
    ('tl', 'Tagalog'),
    ('tg', 'Tajik'),
    ('ta', 'Tamil'),
    ('roa-tar', 'Tarantino'),
    ('te', 'Telugu'),
    ('th', 'Thai'),
    ('tpi', 'Tok Pisin'),
    ('tr', 'Turkish'),
    ('ak', 'Twi'),
    ('uk', 'Ukrainian'),
    ('hsb', 'Upper Sorbian'),
    ('ur', 'Urdu'),
    ('uz', 'Uzbek'),
    ('vec', 'Venetian'),
    ('vi', 'Vietnamese'),
    ('wym', 'Vilamovian'),
    ('vo', 'Volapuk'),
    ('vro', 'Voro'),
    ('cy', 'Welsh'),
    ('xh', 'Xhosa'),
    ('yi', 'Yiddish'),
    ('zza', 'Zazaki'),
)

class Language(models.Model):
    choices = LANGUAGE_CHOICES
    language = models.CharField(
        max_length=30,
        choices=LANGUAGE_CHOICES,
        default='en',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "<User object: {}>".format(self.language)
    
class Place(models.Model):
    host = models.ForeignKey(User, related_name="host_places")
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    description = models.TextField()
    neighborhood = models.TextField()
    check_in_time = models.CharField(max_length=15)
    check_out_time = models.CharField(max_length=15)
    is_smoking_allowed = models.BooleanField(default=False)
    house_rules = models.TextField()
    is_amenities_free_parking = models.BooleanField(default=False)
    is_family_amenities_baby_monitor = models.BooleanField(default=False)
    is_familty_amenities_bathtub = models.BooleanField(default=False)
    is_familty_amenities_changing_table = models.BooleanField(default=False)
    is_familty_amenities_crib = models.BooleanField(default=False)
    is_familty_amenities_fireguards = models.BooleanField(default=False)
    is_familty_amenities_high_chair = models.BooleanField(default=False)
    is_familty_amenities_game_console = models.BooleanField(default=False)
    is_familty_amenities_stair_gates = models.BooleanField(default=False)
    is_amenities_pool = models.BooleanField(default=False)
    is_amenities_pets_allowed = models.BooleanField(default=False)
    is_amenities_breakfast = models.BooleanField(default=False)
    is_amenities_gym = models.BooleanField(default=False)
    is_amenities_hot_tub = models.BooleanField(default=False)
    is_amenities_washer = models.BooleanField(default=False)
    is_amenities_dryer = models.BooleanField(default=False)
    is_amenities_internet = models.BooleanField(default=False)
    is_amenities_wheelchair = models.BooleanField(default=False)
    is_amenities_elevator = models.BooleanField(default=False)
    is_amenities_fireplace = models.BooleanField(default=False)
    is_amenities_air_conditioning = models.BooleanField(default=False)
    is_amenities_cable_tv = models.BooleanField(default=False)
    is_amenities_iron = models.BooleanField(default=False)
    is_amenities_linen_essentials = models.BooleanField(default=False)
    is_amenities_kitchen = models.BooleanField(default=False)
    is_amenities_tv = models.BooleanField(default=False)
    is_amenities_hair_dryer = models.BooleanField(default=False)
    is_amenities_heating = models.BooleanField(default=False)
    cancellation_policy = models.CharField(max_length=255)
    price_night = models.DecimalField(max_digits=6, decimal_places=2)
    price_cleaning = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    price_servicefee = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    price_tax = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    price_amenitites = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review_Place(models.Model):
    review_place = models.ForeignKey(Place, related_name="place_reviews")
    reviewer = models.ForeignKey(User, related_name="place_reviews_from_user")
    CLEANLINESS_CHOICES = (
        ("very_clean", 'My grandmother would be proud!'),
        ("clean", 'My roommate would tolerate it!'),
        ("moderately_clean", 'It reminds me of the Dojo kitchen!'),
        ("dirty", 'My unclogged toilet is cleaner than this!'),
    )
    cleanliness = models.CharField(
        max_length=30,
        choices=CLEANLINESS_CHOICES,
    )
    RATING_CHOICES = (
        ('1','1 STAR'),
        ('2','2 STARS'),
        ('3','3 STARS'),
        ('4','4 STARS'),

    )
    rating = models.IntegerField(
        choices=RATING_CHOICES,
    )
    is_location_accuracy = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review_User(models.Model):
    user_being_reviewed = models.ForeignKey(User, related_name="user_review")
    reviewer = models.ForeignKey(User, related_name="user_reviews_from_user")
    comment = models.CharField(max_length=255)
    is_recommend = models.BooleanField()
    is_host = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Booking(models.Model):
    place = models.ForeignKey(Place, related_name="place_bookings")
    guest = models.ForeignKey(User, related_name="guest_bookings")
    is_cancel = models.BooleanField(default=False)
    check_in = models.DateField()
    check_out = models.DateField()
    date_paid = models.DateTimeField(auto_now_add=True)
    price_night = models.DecimalField(max_digits=6, decimal_places=2)
    price_cleaning = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    price_servicefee = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    price_tax = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    price_amenitites = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Conversation(models.Model):
    host = models.ForeignKey(User, related_name="host_conversations")
    guest = models.ForeignKey(User, related_name="guest_conversations")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    conversation = models.ForeignKey(User, related_name="messages")
    author = models.ForeignKey(User, related_name="user_messages")
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Picture(models.Model):
    place = models.ForeignKey(Place, related_name="place_pictures", blank=True)
    user = models.ForeignKey(User, related_name="user_pictures", blank=True)
    caption = models.CharField(max_length=30)
    link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    photo = models.FileField(upload_to='photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class MyModel(models.Model):
    upload = models.FileField(upload_to=user_directory_path)