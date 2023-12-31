from django.contrib import admin
from .models import Publisher
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field

class PublisherResource(resources.ModelResource):
    date = Field()
    class Meta:
        model = Publisher
        fields = ('id','name','country','created_at','date')
        export_order = ('id','name','country','created_at','date')

    def dehydrate_date(self,obj):
        return obj.created_at.strftime("%d/%m/%y")

class PublisherAdmin(ExportActionMixin,   admin.ModelAdmin):
    resource_class=PublisherResource


admin.site.register(Publisher,PublisherAdmin)