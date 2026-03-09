


from django.shortcuts import render

def home(request):
    if request.method == "POST":
        text = request.POST.get('text', '')
        uploaded_file = request.FILES.get('file', None)

        if uploaded_file and uploaded_file.name.endswith('.txt'):
            text = uploaded_file.read().decode('utf-8')

        words = text.split()
        word_count = len(words)
        char_count = len(text)

        return render(request, 'counter/result.html', {
            'text': text,
            'word_count': word_count,
            'char_count': char_count
        })

    return render(request, 'counter/home.html')
