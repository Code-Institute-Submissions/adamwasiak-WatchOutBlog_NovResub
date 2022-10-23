from django.shortcuts import render
from .forms import ContentForm


def content_view(request):
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'content/success.html')
    form = ContentForm()
    context = {'form': form}
    return render(request, 'content/content.html', context)