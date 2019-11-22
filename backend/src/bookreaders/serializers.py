from rest_framework import serializers

from bookreaders.models import Reader, Book


class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'title', 'author',
        )


class ReaderSerializer(serializers.ModelSerializer):

    books = BooksSerializer(many=True, read_only=True)

    class Meta:
        model = Reader
        fields = (
            'id', 'first_name', 'last_name',
            'created_at', 'modified_at',
            'books'
        )
