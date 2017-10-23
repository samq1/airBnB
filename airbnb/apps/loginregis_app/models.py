from __future__ import unicode_literals
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

# Create your models here.
class UserManager(models.Manager):
    def login_validator(self,postData):
        errors = []
        if len(self.filter(email=postData['email'])) > 0:
            user = self.filter(email=postData['email'])[0]
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
        if len(postData['first_name']) < 2 or len(postData['last_name']) < 2:
            errors.append("name fields must be at least 3 characters")
        #  -----------------------------------
        if len(postData['password']) < 4:
            errors.append("password must be at least 4 characters")
        #  -----------------------------------           
        if not re.match(NAME_REGEX, postData['first_name']) or not re.match(NAME_REGEX, postData['last_name']):
            errors.append('name fields must be letter characters only')
        #  -----------------------------------
        if not re.match(EMAIL_REGEX, postData['email']):
            errors.append("invalid email")
        #  -----------------------------------
        if len(User.objects.filter(email=postData['email'])) > 0:
            errors.append("email already in use")
        #  -----------------------------------
        if postData['password'] != postData['confirm_password']:
            errors.append("passwords do not match")

        if not errors:
            # hash password
            hashed = bcrypt.hashpw((postData['password'].encode()), bcrypt.gensalt(5))

            new_user = self.create(
                first_name=postData['first_name'],
                last_name=postData['last_name'],
                email=postData['email'],
                password=hashed,
                bday=postData['bday']
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
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __repr__(self):
        return "<User object: {} {} {} {} {}>".format(self.id, self.email, self.password, self.created_at, self.updated_at)


class Language(models.Model):
    LANGUAGE_CHOICES = (
        (Abkhaz, 'Abkhaz'),
        (Adyghe, 'Adyghe'),
        (Afrikaans, 'Afrikaans'),
        (Akan, 'Akan'),
        (Albanian, 'Albanian'),
        (American Sign Language, 'American Sign Language'),
        (Amharic, 'Amharic'),
        (Ancient Greek, 'Ancient Greek'),
        (Arabic, 'Arabic'),
        (Aragonese, 'Aragonese'),
        (Aramaic, 'Aramaic'),
        (Armenian, 'Armenian'),
        (Aymara, 'Aymara'),
        (Balinese, 'Balinese'),
        (Basque, 'Basque'),
        (Betawi, 'Betawi'),
        (Bosnian, 'Bosnian'),
        (Breton, 'Breton'),
        (Bulgarian, 'Bulgarian'),
        (Cantonese, 'Cantonese'),
        (Catalan, 'Catalan'),
        (Cherokee, 'Cherokee'),
        (Chickasaw, 'Chickasaw'),
        (Chinese, 'Chinese'),
        (Coptic, 'Coptic'),
        (Cornish, 'Cornish'),
        (Corsican, 'Corsican'),
        (Crimean Tatar, 'Crimean Tatar'),
        (Croatian, 'Croatian'),
        (Czech, 'Czech'),
        (Danish, 'Danish'),
        (Dawro, 'Dawro'),
        (Dutch, 'Dutch'),
        (English, 'English'),
        (Esperanto, 'Esperanto'),
        (Estonian, 'Estonian'),
        (Ewe, 'Ewe'),
        (Fiji Hindi, 'Fiji Hindi'),
        (Filipino, 'Filipino'),
        (Finnish, 'Finnish'),
        (French, 'French'),
        (Galician, 'Galician'),
        (Georgian, 'Georgian'),
        (German, 'German'),
        (Greek, Modern, 'Greek, Modern'),
        (Greenlandic, 'Greenlandic'),
        (Haitian Creole, 'Haitian Creole'),
        (Hawaiian, 'Hawaiian'),
        (Hebrew, 'Hebrew'),
        (Hindi, 'Hindi'),
        (Hungarian, 'Hungarian'),
        (Icelandic, 'Icelandic'),
        (Indonesian, 'Indonesian'),
        (Interlingua, 'Interlingua'),
        (Inuktitut, 'Inuktitut'),
        (Irish, 'Irish'),
        (Italian, 'Italian'),
        (Japanese, 'Japanese'),
        (Javanese, 'Javanese'),
        (Kabardian, 'Kabardian'),
        (Kalasha, 'Kalasha'),
        (Kannada, 'Kannada'),
        (Kashubian, 'Kashubian'),
        (Khmer, 'Khmer'),
        (Kinyarwanda, 'Kinyarwanda'),
        (Korean, 'Korean'),
        (Kurdish/Kurd�, 'Kurdish/Kurd�'),
        (Ladin, 'Ladin'),
        (Latgalian, 'Latgalian'),
        (Latin, 'Latin'),
        (Lingala, 'Lingala'),
        (Livonian, 'Livonian'),
        (Lojban, 'Lojban'),
        (Low German, 'Low German'),
        (Lower Sorbian, 'Lower Sorbian'),
        (Macedonian, 'Macedonian'),
        (Malay, 'Malay'),
        (Malayalam, 'Malayalam'),
        (Mandarin, 'Mandarin'),
        (Manx, 'Manx'),
        (Maori, 'Maori'),
        (Mauritian Creole, 'Mauritian Creole'),
        (Middle Low German, 'Middle Low German'),
        (Min Nan, 'Min Nan'),
        (Mongolian, 'Mongolian'),
        (Norwegian, 'Norwegian'),
        (Old Armenian, 'Old Armenian'),
        (Old English, 'Old English'),
        (Old French, 'Old French'),
        (Old Javanese, 'Old Javanese'),
        (Old Norse, 'Old Norse'),
        (Old Prussian, 'Old Prussian'),
        (Oriya, 'Oriya'),
        (Pangasinan, 'Pangasinan'),
        (Papiamentu, 'Papiamentu'),
        (Pashto, 'Pashto'),
        (Persian, 'Persian'),
        (Pitjantjatjara, 'Pitjantjatjara'),
        (Polish, 'Polish'),
        (Portuguese, 'Portuguese'),
        (Proto-Slavic, 'Proto-Slavic'),
        (Quenya, 'Quenya'),
        (Rapa Nui, 'Rapa Nui'),
        (Romanian, 'Romanian'),
        (Russian, 'Russian'),
        (Sanskrit, 'Sanskrit'),
        (Scots, 'Scots'),
        (Scottish Gaelic, 'Scottish Gaelic'),
        (Serbian, 'Serbian'),
        (Serbo-Croatian, 'Serbo-Croatian'),
        (Sinhalese, 'Sinhalese'),
        (Slovak, 'Slovak'),
        (Slovene, 'Slovene'),
        (Spanish, 'Spanish'),
        (Swahili, 'Swahili'),
        (Swedish, 'Swedish'),
        (Tagalog, 'Tagalog'),
        (Tajik, 'Tajik'),
        (Tamil, 'Tamil'),
        (Tarantino, 'Tarantino'),
        (Telugu, 'Telugu'),
        (Thai, 'Thai'),
        (Tok Pisin, 'Tok Pisin'),
        (Turkish, 'Turkish'),
        (Twi, 'Twi'),
        (Ukrainian, 'Ukrainian'),
        (Upper Sorbian, 'Upper Sorbian'),
        (Urdu, 'Urdu'),
        (Uzbek, 'Uzbek'),
        (Venetian, 'Venetian'),
        (Vietnamese, 'Vietnamese'),
        (Vilamovian, 'Vilamovian'),
        (Volap�k, 'Volap�k'),
        (V�ro, 'V�ro'),
        (Welsh, 'Welsh'),
        (Xhosa, 'Xhosa'),
        (Yiddish, 'Yiddish'),
        (Zazaki, 'Zazaki'),
    )
    language = models.CharField(
        max_length=30,
        choices=LANGUAGE_CHOICES,
        default=English,
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
    is_amenities_free_parking
    is_family_amenities_baby_monitor = models.BooleanField(default=False)
    is_familty_amenities_bathtub = models.BooleanField(default=False)
    is_familty_amenities_changing_table = models.BooleanField(default=False)
    is_familty_amenities_crib = models.BooleanField(default=False)
    is_familty_amenities_fireguards = models.BooleanField(default=False)
    is_familty_amenities_high_chair = models.BooleanField(default=False)
    is_familty_amenities_game_console = models.BooleanField(default=False)
    is_familty_amenities_stair_gates = models.BooleanField(default=False)
    is_amenities_free_parking = models.BooleanField(default=False)
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
    reviewer = models.ForeignKey(User, related_name="reviews_from_user")
    CLEANLIESS_CHOICES = (
        (very_clean, 'My grandmother would be proud!'),
        (clean, 'My roommate would tolerate it!'),
        (moderately_clean, 'It reminds me of the Dojo kitchen!'),
        (dirty, 'My unclogged toilet is cleaner than this!'),
    )
    cleanliness = models.CharField(
        max_length=30,
        choices=CLEANLINESS_CHOICES,
    )
    RATING_CHOICES = (
        (1,'1 STAR'),
        (2,'2 STARS'),
        (3,'3 STARS'),
        (4,'4 STARS'),

    )
    rating = models.IntegerField(
        choices=RATING_CHOICES,
    )
    is_location_accuracy = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review_User(models.Model):
    user_being_reviewed = models.ForeignKey(User, related_name="user_review")
    reviewer = models.ForeignKey(User, related_name="reviews_from_user")
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


    