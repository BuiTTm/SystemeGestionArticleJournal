def handle_soumission_article_file_upload(f, filename):
    with open('static/uploads/' + filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
