from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .forms import *
from office.models import *
from .models import *


class MainView(ListView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        context['projects'] = Project.objects.all()
        context['offers'] = Offer.objects.all()
        context['categories'] = Category.objects.all()

        return context

    def get_queryset(self):
        return Department.objects.all()


class DepartmentListView(ListView):
    model = Department
    template_name = 'department_info.html'
    context_object_name = 'departments'


class HistoryView(ListView):
    model = History
    template_name = 'history_page.html'
    context_object_name = 'history_data'


class MissionView(ListView):
    model = Mission
    template_name = 'mission_page.html'
    context_object_name = 'mission_data'


class WorkerListView(ListView):
    model = Worker
    template_name = 'worker_list.html'
    context_object_name = 'workers'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html' 
    context_object_name = 'project'


class ProjectListView(ListView):
    model = Project
    template_name = 'project_list.html' 


class OfferDetailView(DetailView):
    model = Offer
    context_object_name = 'offer'

    def get_template_names(self):
        offer_type = self.object.type
        return [f'offers/offer_detail_{offer_type}.html']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    

class CategoryDetailView(ListView):
    template_name = 'category_detail.html'
    context_object_name = 'products'
    paginate_by = 24

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        queryset = Product.objects.filter(category=self.category)
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = Category.objects.all()
        context['departments'] = Department.objects.all()
        context['company'] = Company.objects.first()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['departments'] = Department.objects.all()
        context['company'] = Company.objects.first()
        return context
    
