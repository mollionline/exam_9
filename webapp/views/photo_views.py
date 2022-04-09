from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import DetailView, CreateView, DeleteView, ListView, UpdateView
from webapp.models import Photo, ChoosePhoto
from webapp.forms import PhotoForm


class ListPhotoView(ListView):
    template_name = 'photo/list_photo.html'
    model = Photo
    context_object_name = 'photos'


class DetailPhotoView(DetailView):
    model = Photo
    context_object_name = 'photo'
    template_name = 'photo/detail_photo.html'


class DeletePhotoView(PermissionRequiredMixin, DeleteView):
    model = Photo
    permission_required = ''

    def get(self, request, *args, **kwargs):
        return self.delete(request=request)

    def get_success_url(self):
        return reverse('list_photo')

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user


class CreatePhotoView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'photo/create_photo.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, files=self.request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            user = request.user
            photo.author = user
            photo.save()
            url = reverse('detail_photo', kwargs={'pk': photo.pk})
            return HttpResponseRedirect(url)
        return render(request, self.template_name,
                      context={
                          'form': form
                      })


class UpdatePhotoView(PermissionRequiredMixin, UpdateView):
    model = Photo
    template_name = 'photo/update_photo.html'
    form_class = PhotoForm
    context_object_name = 'photo'
    permission_required = ''
    success_url = '/'

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user


class ChoosePhotoView(CreateView):
    model = ChoosePhoto

    def post(self, request, *args, **kwargs):
        photo_pk = kwargs.get('pk')
        photo = get_object_or_404(Photo, pk=photo_pk)
        if not self.model.objects.filter(photo_id=photo_pk, author_id=self.request.user.pk):
            self.model.objects.create(photo_id=photo_pk, author_id=self.request.user.pk)
            photo.save()
        else:
            photo.save()
            self.model.objects.filter(photo_id=photo_pk, author_id=self.request.user.pk).delete()
        return redirect(request.META.get('HTTP_REFERER'))
