from typing import Any

from django.contrib.auth.decorators import login_required
from django.db.models import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .models import Cook, Dish, DishType

from .forms import (CookCreationForm,
                    DishForm,
                    CookSearchForm,
                    DishSearchForm,
                    DishTypeSearchForm)


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "kitchen_service/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_cooks"] = Cook.objects.count()
        context["num_dishes"] = Dish.objects.count()
        context["num_dish_types"] = DishType.objects.count()

        num_visits = self.request.session.get("num_visits", 0) + 1
        self.request.session["num_visits"] = num_visits
        context["num_visits"] = num_visits

        return context


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    paginate_by = 5

    def get_context_data(
        self, *, object_list=..., **kwargs
    ):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishTypeSearchForm(
            initial={"name": name},
        )
        return context

    def get_queryset(self):
        queryset = DishType.objects.all()
        form = DishTypeSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen_service:dish_type-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen_service:dish_type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "kitchen_service/dish_type_confirm_delete.html"
    success_url = reverse_lazy("kitchen_service:dish_type-list")


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    paginate_by = 5

    def get_context_data(
        self, *, object_list=..., **kwargs
    ) -> dict[str, Any]:
        context = super(DishListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishSearchForm(
            initial={"name": name},
        )
        return context

    def get_queryset(self):
        queryset = Dish.objects.select_related("dish_type")
        form = DishSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen_service:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen_service:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen_service:dish-list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    paginate_by = 5

    def get_context_data(
        self, *, object_list=..., **kwargs
    ):
        context = super(CookListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = CookSearchForm(
            initial={"username": username},
        )
        return context

    def get_queryset(self) -> QuerySet:
        queryset = Cook.objects.get_queryset()
        form = CookSearchForm(self.request.GET)
        if form.is_valid():
            return (queryset.
                    filter(username__icontains=form.cleaned_data["username"]))
        return queryset


class CookDetailView(LoginRequiredMixin,
                     generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("cooks__dish_type")


class CookCreateView(LoginRequiredMixin,
                     generic.CreateView):
    model = Cook
    form_class = CookCreationForm


class CookDeleteView(LoginRequiredMixin,
                     generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen_service:cook-list")


class ToggleAssignToDishView(LoginRequiredMixin, View):
    def post(self, request, pk):
        dish = get_object_or_404(Dish, id=pk)
        cook = request.user

        if cook in dish.cooks.all():
            dish.cooks.remove(cook)
        else:
            dish.cooks.add(cook)

        return HttpResponseRedirect(reverse(
            "kitchen_service:dish-detail", args=[pk]))
