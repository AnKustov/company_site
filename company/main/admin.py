from django.contrib import admin
from .models import *
from office.models import *

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phones', 'emails', 'manager')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 
                    'legal_name',
                    'edrpou',
                    'physical_address',
                    'legal_address',
                    'account',
                    'tax_number',
                    'single_tax_payer_certificate',
                    'phones',
                    'emails',
                    'director')
    

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('short_description', )

    def short_description(self, obj):
        max_length = 50 
        return (obj.description[:max_length] + '...') if len(obj.description) > max_length else obj.description
    

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('short_description', )

    def short_description(self, obj):
        max_length = 50 
        return (obj.description[:max_length] + '...') if len(obj.description) > max_length else obj.description


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'second_name', 'department', 'phone_number', 'email' )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'client')


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


class ProductImageInline(admin.TabularInline): 
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('article' ,'name', 'category')
    search_fields = ['name', 'article']
    readonly_fields = ('article',)


admin.site.site_title = "Адмін-панель сайту"
admin.site.site_header = "Адмін-панель сайту"