from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Review

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'reviews/review_detail.html', {'review': review})

class ReviewListView(ListView):
    context_object_name = 'reviews'
    model = Review

class ReviewDetailView(DetailView):
    model = Review

class ReviewCreateView(CreateView):
    fields = ('name', 'date_of_visit', 'email', 'title', 'message')
    model = Review

class ReviewUpdateView(UpdateView):
    fields = ('name', 'date_of_visit', 'email', 'title', 'message')
    model = Review

class ReviewDeleteView(DeleteView):
    model = Review
