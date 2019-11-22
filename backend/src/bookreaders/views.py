import csv

from django.core.serializers.python import Serializer
from django.http import StreamingHttpResponse

from bookreaders.models import Reader

class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


def some_streaming_csv_view(request):
    """A view that streams a large CSV file."""
    # Generate a sequence of rows. The range is based on the maximum number of
    # rows that can be handled by a single sheet in most spreadsheet
    # applications.
    rows = (
        [
            f"{reader.id};"
            f"{reader.first_name};"
            f"{reader.last_name};"
            f"{[book for book in reader.books.values('title', 'author')]}"
        ] for reader in Reader.objects.all()
    )
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    response = StreamingHttpResponse((writer.writerow(row) for row in rows),
                                     content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    return response
