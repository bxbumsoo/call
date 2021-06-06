from django.core.checks import messages
from django.urls import reverse
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import Calloj
from django.http import Http404

# Create your views here.


def callhome(request):
    message = request.GET.get('message')
    callinfo = Calloj.objects.get(mdname='콜 기본정보')
    if message:
        mdmd = Calloj.objects.filter(mdname__icontains=message)
        return render(request, 'home.html', {'callinfo': callinfo, 'mdmd': mdmd})
    return render(request, 'home.html', {'callinfo': callinfo})


def info(request):
    message = request.GET.get('message')
    callinfo = Calloj.objects.get(mdname='콜 기본정보')
    if request.method == 'POST':
        callinfo.mdname = request.POST['mdmd']
        callinfo.mdinfo = request.POST['ifif']
        callinfo.save()
        return render(request, 'home.html', {'callinfo': callinfo})
    if message:
        mdmd = Calloj.objects.filter(mdname__icontains=message)
        return render(request, 'home.html', {'callinfo': callinfo, 'mdmd': mdmd})

    return render(request, 'info.html', {'callinfo': callinfo})


def detail(request, mdname):
    callmd = Calloj.objects.get(mdname=mdname)
    message = request.GET.get('message')
    callinfo = Calloj.objects.get(mdname='콜 기본정보')
    if message:
        mdmd = Calloj.objects.filter(mdname__icontains=message)
        return render(request, 'home.html', {'callinfo': callinfo, 'mdmd': mdmd})
    return render(request, 'detail.html', {'callinfo': callinfo, 'callmd': callmd})


def mdinfo(request, mdname):
    callmd = Calloj.objects.get(mdname=mdname)
    message = request.GET.get('message')
    callinfo = Calloj.objects.get(mdname='콜 기본정보')
    # template_name = 'mdinfo/%s_list.html' % mdname
    if request.method == 'POST':
        callmd.mdname = request.POST['mdmd']
        callmd.mdinfo = request.POST['ifif']
        callmd.save()

        return render(request, 'detail.html', {'callinfo': callinfo, 'callmd': callmd})

    if message:
        mdmd = Calloj.objects.filter(mdname__icontains=message)
        return render(request, 'home.html', {'callinfo': callinfo, 'mdmd': mdmd})

    return render(request, 'mdinfo.html', {'callinfo': callinfo, 'callmd': callmd})


def one(request):
    message = request.GET.get('message')
    callinfo = Calloj.objects.get(mdname='콜 기본정보')
    if message:
        mdmd = Calloj.objects.filter(mdname__icontains=message)
        return render(request, 'home.html', {'callinfo': callinfo, 'mdmd': mdmd})
    return render(request, 'home.html', {'callinfo': callinfo})


def newmd(request):
    message = request.GET.get('message')
    callinfo = Calloj.objects.get(mdname='콜 기본정보')
    newmdn = Calloj()
    if request.method == 'POST':
        for alist in Calloj.objects.filter(mdname=request.POST['mdmd']):
            if request.POST['mdmd'] == alist.mdname:
                return Http404('ddd')
        newmdn.mdname = request.POST['mdmd']
        newmdn.mdinfo = request.POST['ifif']
        newmdn.save()
        new = Calloj.objects.get(mdname=request.POST['mdmd'])
        return render(request, 'home.html', {'callinfo': callinfo, 'new': new})
    if message:
        mdmd = Calloj.objects.filter(mdname__icontains=message)
        return render(request, 'home.html', {'callinfo': callinfo, 'mdmd': mdmd})
    return render(request, 'newmd.html', {'callinfo': callinfo})


def delmd(request, mdname):
    callmd = Calloj.objects.get(mdname=mdname)
    callmd.delete()
    return redirect('/')
