from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

from App.form import ContactForm
from App.models import *
from emotionre.new import classi


def plantiart(request):
    results = Topic.objects.all()  # .distinct()
    user = User.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            es = form.save(commit=False)
            dic_sent = classi(es.comment.lower())
            cad = ""
            _Ps = 0
            _Ns = 0
            _NEUs = 0
            for sent in dic_sent:
                cad = cad + sent + '(' + dic_sent[sent] + ')'

            es.comment = cad
            es.save()
            return render(request, 'index.html',
                          {"results": results, "coments": user, 'form': ContactForm(initial={'sender': 'anonymous'})})
    else:
        form = ContactForm(initial={'sender': 'anonymous'})
    return render(request, 'index.html',
                  {"results": results, "coments": user, 'form': form})


def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(title__icontains=query) | Q(authors__first_name__icontains=query) | Q(
                authors__last_name__icontains=query))
        results = User.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("search.html", {"results": results, "query": query, 'busqueda': "s"})


def querys(request):
    form = ContactForm(initial={'sender': 'anonymous'})
    query = request.GET.get('query', '')
    if query:
        qset = (Q(topic__icontains=query) | Q(creator__icontains=query))  # | Q(authors__last_name__icontains=query))
        result = Topic.objects.filter(qset)  # .distinct()
    else:
        result = []
    return render_to_response("index.html", {"results": result, "form": form, 'query': 'd', 'busqueda': "s"})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            post = form.save()
            # post.save()

        return HttpResponseRedirect('http://127.0.0.1:8000')
    else:
        form = ContactForm(initial={'sender': 'user@yourdomine'})

    return render(request, 'contact.html', {'form': form})


def searchtopic(request):
    return render_to_response()
