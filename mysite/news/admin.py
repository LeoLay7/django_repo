from django.contrib import admin

from .models import News, Category
# Register your models here.


class NewsAdmin(admin.ModelAdmin):  # класс, отвечающий за вывод объектов в админке
    list_display = ['id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'photo']  # список того, что нужно вывести
    list_display_links = ['id', 'title']  # какие штуки будут ссылками на информацию об объекте
    search_fields = ['title', 'content']  # по каким полям можно осуществлять поиск в админке
    list_editable = ['is_published']  # что изменяется
    list_filter = ['category', 'is_published']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    search_fields = ['title']


admin.site.register(News, NewsAdmin)  # регистрация модели
admin.site.register(Category, CategoryAdmin)
