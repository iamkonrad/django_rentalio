from django.contrib import admin

from .choices import STATUS_CHOICES
from .models import Rental
from import_export import resources
from import_export.admin import ExportActionMixin
from import_export.fields import Field

class RentalResource(resources.ModelResource):
    book=Field()
    book_id=Field()
    ISBN=Field()
    status=Field()
    is_closed=Field()
    customer=Field()

    class Meta:
        model=Rental
        fields=('id','book','book_id','ISBN','customer','status','is_closed','rent_start_date','rent_end_date','return_date')

    def dehydrate_book(self,obj):
        return obj.book.title.title

    def dehydrate_book_id(self,obj):
        return obj.book.id

    def dehydrate_isbn(self,obj):
        return obj.book.title.isbn

    def dehydrate_status(self,obj):
        statuses = dict(STATUS_CHOICES)
        return statuses[obj.status]

    def dehydrate_is_closed(self,obj):
        return True if obj.is_closed == 1 else False

    def dehydrate_customer(self,obj):
        return obj.customer.username

class RentalAdmin(ExportActionMixin, admin.ModelAdmin):
    resource_class = RentalResource

admin.site.register(Rental)
