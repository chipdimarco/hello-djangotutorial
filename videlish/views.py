from django.shortcuts import render
from django.views import View

from videlish.models import Recipe

class FeedView(View):
    def get(self, request):
        all_recipes = Recipe.objects.all()
        context = {'recipes': all_recipes}
        return render(request, 'feed.html', context)


    # def post(self, request):
        # Code block for POST request