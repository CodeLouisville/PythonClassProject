from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import CustomerFeedback

def customer_feedback_list(request):
    reviews = CustomerFeedback.objects.all()
    return render(request, 'reviews/reviews_list.html', {'reviews': reviews})

def customer_feedback_detail(request, pk):
    review = get_object_or_404(CustomerFeedback, pk=pk)
    return render(request, 'reviews/reviews_detail.html', {'review': review})

class CustomerFeedbackListView(ListView):
    context_object_name = 'reviews'
    model = CustomerFeedback

class CustomerFeedbackDetailView(DetailView):
    model = CustomerFeedback