from django.shortcuts import render,redirect
from .forms import *
from django.views.generic import CreateView, UpdateView , DeleteView
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.


def homepage(request):
    films_data = Film.objects.all()
    return render(request, 'homepage.html', {'films': films_data})

# Another way of creating a form, call it as a class
# instead doing like below - saves some lines of code
class AddFilm(CreateView,SuccessMessageMixin):
    form_class = AddFilmForm
    template_name = 'add.html'
    success_url = '/films/homepage'
    #TODO: why in the HTML when i try to render 'form.country` and `form.category` it does not show up, but the others it does
    #TODO: How to pass an ID to Modal to delete a film but his own ID

    def form_valid(self, form):
        form.save()
        self.success_message = 'Film has successfully added'
        return redirect(self.success_url)


class UpdateFilm(UpdateView,SuccessMessageMixin):
    form_class = AddFilmForm
    template_name = 'add.html'
    success_url = 'homepage'
    success_message = 'Film has update'

    def form_valid(self, form):
        form.save()
        self.success_message = 'Film has successfully updated'
        return redirect(self.success_url)

    def get_object(self, queryset=None):
        return Film.objects.get(pk=self.kwargs['pk'])


class AddDirector(CreateView,SuccessMessageMixin):
    form_class = AddDirectorForm
    template_name = 'add.html'
    success_url = '/films/homepage'

    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        if first_name != "" and last_name != "":
            form.save()
        self.success_message = 'Director has successfully added'
        return redirect(self.success_url)


class UpdateDirector(UpdateView,SuccessMessageMixin):
    model = Director
    form_class = AddDirectorForm
    template_name = 'add.html'
    success_url = 'homepage'


    def form_valid(self, form):
        form.save()
        self.success_message = 'Director has successfully updated'
        return redirect(self.success_url)

    def get_object(self, queryset=None):
        return Director.objects.get(pk=self.kwargs['pk'])


class DeleteFilmView(DeleteView):
    template_name = 'homepage.html'
    model = Film
    context_object_name = 'film'
    success_url = '/films/homepage'

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.success_url)

class CommentViewForm(CreateView,SuccessMessageMixin):
    form_class = AddCommentForm
    template_name = 'comment.html'
    model = Comments
    success_message = 'Comment has added'
    success_url = '/films/homepage'

    def form_valid(self, form):
        form.save()
        self.success_message = self.success_message
        return redirect(self.success_url)

    def get_object(self, queryset=None):
        return Film.objects.get(pk=self.kwargs['pk'])
        #TODO: here i want to get by the film id the film and display its title on Comment html - need to ask how to do that