from django.shortcuts import render, get_object_or_404, redirect
from .models import WorkingClass, Word, Voice, FullData
from .forms import AddWordForm, AddVoiceForm, AddFullDataForm

def home_page(request):
    working_classes = WorkingClass.objects.all()
    return render(request, "./home.html", {'working_classes': working_classes})


def full_data_page(request, slug):
    working_class = get_object_or_404(WorkingClass, slug=slug)
    full_data = FullData.objects.all()
    context = {
        'working_class': working_class,
        'full_data': full_data
    }
    return render(request, "./full-data.html", context)

def full_data_detail_page(request, slug, pk):
    working_class = get_object_or_404(WorkingClass, slug=slug)
    full_data = get_object_or_404(FullData, pk=pk)
    context = {
        'working_class': working_class,
        'full_data': full_data
    }
    return render(request, "./full-data-detail.html", context)

def add_word_page(request):
    if request.method == "POST":
        form = AddWordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_page")
    else:
        form = AddWordForm()

    return render(request, "./add-word.html", {'form': form})

def add_voice_page(request):
    if request.method == "POST":
        form = AddVoiceForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect("home_page")
    else:
        form = AddVoiceForm()

    return render(request, "./add-voice.html", {'form': form})

def add_full_data_page(request):
    if request.method == "POST":
        form = AddFullDataForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect("home_page")
    else:
        form = AddFullDataForm()

    return render(request, "./add-full.html", {'form': form})