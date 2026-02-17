from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .models import Cuisine


# ----------------------------
# FUNCTION-BASED VIEW
# ----------------------------

def cuisine_list_fbv(request):
    object_list = Cuisine.published.all()
    paginator = Paginator(object_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "cuisine/list.html",
        {"cuisines": page_obj, "page_obj": page_obj}
    )


# ----------------------------
# CLASS-BASED VIEWS
# ----------------------------

class CuisineListView(ListView):
    queryset = Cuisine.published.all()
    context_object_name = "cuisines"
    paginate_by = 3
    template_name = "cuisine/list.html"


class CuisineDetailView(DetailView):
    model = Cuisine
    context_object_name = "cuisine"
    template_name = "cuisine/detail.html"

    def get_queryset(self):
        return Cuisine.published.all()
