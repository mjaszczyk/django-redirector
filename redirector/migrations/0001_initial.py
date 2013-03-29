# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Rule'
        db.create_table('redirector_rule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('redirection_type', self.gf('django.db.models.fields.SmallIntegerField')(default=301)),
            ('pattern', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('target_url', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('target_url_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('target_view', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('target_params', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
        ))
        db.send_create_signal('redirector', ['Rule'])


    def backwards(self, orm):
        
        # Deleting model 'Rule'
        db.delete_table('redirector_rule')


    models = {
        'redirector.rule': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Rule'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'pattern': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'redirection_type': ('django.db.models.fields.SmallIntegerField', [], {'default': '301'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'target_params': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'target_url': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'target_url_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'target_view': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['redirector']
