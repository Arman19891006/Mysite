from django.contrib import admin
from blog.models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'empty'
    list_filter = ('status',)
    #ordering = ('created_date',)
    search_fields = ['title','content']
    list_display =('title','counted_view','status','published_date','created_date')
admin.site.register(Post,PostAdmin)