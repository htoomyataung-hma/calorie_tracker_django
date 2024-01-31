from django.shortcuts import render, redirect
from .models import Food, Consume
from django.shortcuts import get_object_or_404


# Create your views here.

def createfood(request):
    if request.method == "POST":
        food_name = request.POST.get('name')
        food_carbs = request.POST.get('carbs')
        food_protein = request.POST.get('protein')
        food_fats = request.POST.get('fats')
        food_calories = request.POST.get('calories')
        foods_name = Food.objects.create(name='food_name')
        foods_carbs = Food.objects.create(name='food_carbs')
        foods_protein = Food.objects.create(name='food_protein')
        foods_fats = Food.objects.create(name='food_fats')
        foods_calories = Food.objects.create(name='food_calories')
        return render(request, 'myapp/food.html')


def index(request):
    if request.method == "POST":
        food_consumed = request.POST.get('food_consumed')
        # consume = Food.objects.get(name=food_consumed)
        consume = get_object_or_404(Food, name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()
        foods = Food.objects.all()

    else:
        foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user.id)

    return render(request, 'myapp/index.html', {'foods': foods, 'consumed_food': consumed_food})


def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    return render(request, 'myapp/delete.html')
