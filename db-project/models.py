# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Book(models.Model):
    isbn13 = models.CharField(db_column='ISBN13', primary_key=True, max_length=14)  # Field name made lowercase.
    isbn10 = models.CharField(db_column='ISBN10', unique=True, max_length=10)  # Field name made lowercase.
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    years = models.IntegerField()
    num_copies = models.IntegerField()
    price = models.FloatField()
    book_format = models.CharField(max_length=9)
    keyword = models.CharField(max_length=255, blank=True, null=True)
    book_subject = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'


class Customer(models.Model):
    login_name = models.CharField(primary_key=True, max_length=255)
    fullname = models.CharField(max_length=255)
    login_password = models.CharField(max_length=255)
    credit_card = models.CharField(max_length=16)
    address = models.CharField(max_length=255)
    phone_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customer'


class Orders(models.Model):
    login_name = models.ForeignKey(Customer, models.DO_NOTHING, db_column='login_name')
    isbn13 = models.ForeignKey(Book, models.DO_NOTHING, db_column='ISBN13')  # Field name made lowercase.
    num_order = models.IntegerField(blank=True, null=True)
    order_date = models.DateField()
    order_status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'orders'
        unique_together = (('login_name', 'isbn13'),)


class Rate(models.Model):
    rater = models.ForeignKey(Customer, models.DO_NOTHING, db_column='rater')
    rated = models.ForeignKey('Review', models.DO_NOTHING, db_column='rated')
    rating = models.IntegerField()
    isbn13 = models.ForeignKey('Review', models.DO_NOTHING, db_column='ISBN13')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rate'
        unique_together = (('rater', 'rated', 'isbn13'),)


class Review(models.Model):
    login_name = models.ForeignKey(Customer, models.DO_NOTHING, db_column='login_name')
    isbn13 = models.ForeignKey(Book, models.DO_NOTHING, db_column='ISBN13')  # Field name made lowercase.
    review_score = models.IntegerField(blank=True, null=True)
    review_text = models.CharField(max_length=255, blank=True, null=True)
    review_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'
        unique_together = (('login_name', 'isbn13'),)


class Shoppingcart(models.Model):
    login_name = models.ForeignKey(Customer, models.DO_NOTHING, db_column='login_name')
    isbn13 = models.ForeignKey(Book, models.DO_NOTHING, db_column='ISBN13')  # Field name made lowercase.
    num_order = models.IntegerField(blank=True, null=True)
    order_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shoppingcart'
        unique_together = (('login_name', 'isbn13'),)
