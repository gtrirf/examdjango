from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from .forms import BikeForm, AddReviewForm, ReviewForm
from .models import Bike, Review, Category, PurchaseRequest


class BikeListView(View):
    def get(self, request):
        categories = Category.objects.all()
        bikes = Bike.objects.all().order_by('-id')
        context = {
            'categories': categories,
            'bikes': bikes
        }
        return render(request, 'home.html', context=context)


class BikesByCategoryView(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        bikes = Bike.objects.filter(category=category).order_by('-id')
        categories = Category.objects.all()
        context = {
            'category': category,
            'bikes': bikes,
            'categories': categories
        }
        return render(request, 'bikes_category.html', context=context)


class BikeDetailView(View):
    def get(self, request, pk):
        bike = get_object_or_404(Bike, pk=pk)
        reviews = Review.objects.filter(bike=bike)
        context = {
            'bike': bike,
            'reviews': reviews,
        }
        return render(request, 'bike_detail.html', context=context)


class AddReviewView(LoginRequiredMixin, View):
    def get(self, request, pk):
        bike = get_object_or_404(Bike, pk=pk)
        add_review_form = AddReviewForm()
        context = {
            'bike': bike,
            'add_review_form': add_review_form
        }
        return render(request, 'add_review.html', context=context)

    def post(self, request, pk):
        bike = get_object_or_404(Bike, pk=pk)
        add_review_form = AddReviewForm(request.POST)
        if add_review_form.is_valid():
            review = add_review_form.save(commit=False)
            review.bike = bike
            review.user = request.user
            review.save()
            messages.success(request, 'Review added successfully!')
            return redirect('bikes:bike-detail', pk=pk)
        else:
            messages.error(request, 'Something went wrong. Please check your input.')
            context = {
                'bike': bike,
                'add_review_form': add_review_form
            }
            return render(request, 'add_review.html', context=context)


class DeleteReviewView(LoginRequiredMixin, View):
    def get(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        bike = review.bike
        is_author = review.user == request.user
        return render(request, 'delete_review.html', {'review': review, 'bike':bike, 'is_author': is_author})

    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        if review.user != request.user:
            messages.error(request, "You are not authorized to delete this review.")
            return redirect('bikes:bike-detail', pk=review.bike.id)
        review.delete()
        messages.success(request, 'Review deleted successfully.')
        return redirect('bikes:bike-detail', pk=review.bike.id)


class UpdateReviewView(LoginRequiredMixin, View):
    def get(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        form = AddReviewForm(instance=review)
        context = {
            'form': form,
            'review': review
        }
        return render(request, 'update_review.html', context=context)

    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        form = AddReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review updated successfully.')
            return redirect('bikes:bike-detail', pk=review.bike.id)
        else:
            messages.error(request, 'Error updating review. Please check the form.')
        return render(request, 'update_review.html', {'form': form, 'review': review})


def handle_purchase_request(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        PurchaseRequest.objects.create(name=name, phone=phone)
        return redirect('bikes:home')
    else:
        pass