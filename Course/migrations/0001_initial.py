# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Course'
        db.create_table(u'Course_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('equipment', self.gf('django.db.models.fields.TextField')()),
            ('contact_phone_number', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('price_clarification', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'Course', ['Course'])

        # Adding model 'Price'
        db.create_table(u'Course_price', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Course.Course'])),
        ))
        db.send_create_signal(u'Course', ['Price'])

        # Adding model 'Slot'
        db.create_table(u'Course_slot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('weekday_from', self.gf('django.db.models.fields.IntegerField')()),
            ('weekday_to', self.gf('django.db.models.fields.IntegerField')()),
            ('from_hour', self.gf('django.db.models.fields.TimeField')()),
            ('to_hour', self.gf('django.db.models.fields.TimeField')()),
            ('level', self.gf('django.db.models.fields.IntegerField')()),
            ('children_accepted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('adult_accepted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'Course', ['Slot'])

        # Adding model 'Place'
        db.create_table(u'Course_place', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('adress', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')(blank=True, null=True, geography=True)),
        ))
        db.send_create_signal(u'Course', ['Place'])

        # Adding model 'Note'
        db.create_table(u'Course_note', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'Course', ['Note'])


    def backwards(self, orm):
        # Deleting model 'Course'
        db.delete_table(u'Course_course')

        # Deleting model 'Price'
        db.delete_table(u'Course_price')

        # Deleting model 'Slot'
        db.delete_table(u'Course_slot')

        # Deleting model 'Place'
        db.delete_table(u'Course_place')

        # Deleting model 'Note'
        db.delete_table(u'Course_note')


    models = {
        u'Course.course': {
            'Meta': {'object_name': 'Course'},
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'contact_phone_number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'equipment': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price_clarification': ('django.db.models.fields.TextField', [], {})
        },
        u'Course.note': {
            'Meta': {'object_name': 'Note'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'Course.place': {
            'Meta': {'object_name': 'Place'},
            'adress': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'blank': 'True', 'null': 'True', 'geography': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        u'Course.price': {
            'Meta': {'object_name': 'Price'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['Course.Course']"}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {})
        },
        u'Course.slot': {
            'Meta': {'object_name': 'Slot'},
            'adult_accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'children_accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'from_hour': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {}),
            'to_hour': ('django.db.models.fields.TimeField', [], {}),
            'weekday_from': ('django.db.models.fields.IntegerField', [], {}),
            'weekday_to': ('django.db.models.fields.IntegerField', [], {})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['Course']