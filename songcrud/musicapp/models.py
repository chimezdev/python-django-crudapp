from django.db import models
import uuid



# Create your models here.
class Artiste(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=25, null=True)
    last_name = models.CharField(max_length=25, null=True)
    age = models.IntegerField(null=True)
    
    def __str__(self):
        return self.first_name #displays the table name instead of object(1) as name
    
class Song(models.Model):
    VOTE = (                # creates a selectable dropdown list to any attribute its inferred to in form 'choice="..."'
        ('Likes', 'likes'),
        ('Unlike', 'unlike'),
    )
    artiste_id = models.ForeignKey(Artiste, null=True, on_delete=models.SET_NULL)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=30, null=True)
    release_date = models.DateTimeField(auto_now_add=True, null=True)
    likes = models.IntegerField(null=True)
    vote = models.CharField(max_length=10, null=True, choices=VOTE)
    
    def __str__(self):
        return self.title
    
class Lyric(models.Model):
    song_id = models.ForeignKey(Song, null=True, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    content = models.TextField(max_length=2000, null=True)
    
    def __str__(self):
        return self.content
    
    
# i used this line of code to clear and delete all tables
# def delete_everything(self):
#     Reporter.objects.all().delete()

# def drop_table(self):
#     cursor = connection.cursor()
#     table_name = self.model._meta.db_table
#     sql = "DROP TABLE %s;" % ()
#     cursor.execute(sql)