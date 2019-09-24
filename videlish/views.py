
from django import forms
from django.shortcuts import render
from django.views import View

from videlish.models import Recipe

class FeedView(View):
    def get(self, request):
        all_recipes = [recipe.get_recipe_card_context() for recipe in Recipe.objects.all()]
        context = {'recipes': all_recipes}
        create_recipe_form = RecipeForm()
        context.update({'create_recipe_form': create_recipe_form})
        return render(request, 'feed.html', context)

    # def post(self, request):
        # Code block for POST request


class CreateRecipe(View):
    def get(self, request):
        form = RecipeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return 'yay'
        

class RecipeForm(forms.Form):
    recipe_name = forms.CharField(label='Name', max_length=100)
    host = forms.ChoiceField(label='Host', choices=[('Youtube', 'Youtube')])
    credit =  forms.CharField(max_length=250)
    hostId =  forms.CharField(max_length=100)