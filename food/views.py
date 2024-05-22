from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Item
from .forms import CreateForm
from django.contrib.auth.decorators import login_required

"""
@login_required
def home(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'home.html', context)
"""


class Home(ListView):
    model = Item
    template_name = 'home.html'
    context_object_name = 'items'


"""
@login_required
def detail(request, id):
    item = Item.objects.get(pk=id)
    context = {
        'item': item
    }
    return render(request, 'detail.html', context)
"""


class Detail(DetailView):
    model = Item
    template_name = 'detail.html'
    context_object_name = 'item'


"""
@login_required
def create(request):
    form = CreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'create.html', {'form': form})
"""


class CreateItem(CreateView):
    model = Item
    fields = ['name', 'description', 'price', 'image']
    template_name = 'create.html'
    success_url = reverse_lazy('food:home')

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


"""
@login_required
def update(request, id):
    item = Item.objects.get(pk=id)
    form = CreateForm(request.POST or None, instance=item)
    context = {
        'form': form,
        'item': item
    }
    if form.is_valid():
        form.save()
        return redirect('food:home')
    return render(request, 'create.html', context)
"""


class Update(UpdateView):
    model = Item
    template_name = 'update.html'
    form_class = CreateForm
    success_url = reverse_lazy('food:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = self.object
        return context


"""
@login_required
def delete(request, id):
    item = Item.objects.get(pk=id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:home')
    return render(request, 'home.html', {'item': item})
"""


class Delete(DeleteView):
    model = Item
    success_url = reverse_lazy('food:home')
