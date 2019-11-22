from django.contrib import admin

from bookreaders.models import Book, Reader


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'author',
        'created_at', 'modified_at'
    )


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name',
        'created_at', 'modified_at'
    )
