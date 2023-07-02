from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import ExercisesCatalogForm, ProgramForm
from .models import User, ExercisesCatalog, Program, Plan


def index(request):
    currentUser = request.user.id
    exercises = ExercisesCatalog.objects.all()
    availablePrograms = Program.objects.filter(user=currentUser)
    plans = Plan.objects.all()
    if request.method == "POST":
        queryCategory = request.POST["category"]
        filteredExercises = ExercisesCatalog.objects.filter(
            category=queryCategory)
        return render(request, "base/index.html", {
            "programs": availablePrograms,
            "exercises": filteredExercises,
            "form": ExercisesCatalogForm(),
            "formProgram": ProgramForm(),
            "plans": plans
        })
    else:
        return render(request, "base/index.html", {
            "programs": availablePrograms,
            "exercises": exercises,
            "form": ExercisesCatalogForm(),
            "formProgram": ProgramForm(),
            "plans": plans
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "base/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "base/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "base/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "base/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "base/register.html")


def search_exercise(request):
    currentUser = request.user.id
    availablePrograms = Program.objects.filter(user=currentUser)
    plans = Plan.objects.all()
    if request.method == "POST":
        # filter database with partial matches on the title
        searchQuery = request.POST.get('q')
        queryMatch = ExercisesCatalog.objects.filter(
            exerciseName__icontains=searchQuery)
        return render(request, "base/index.html", {
            "exercises": queryMatch,
            "form": ExercisesCatalogForm(),
            "programs": availablePrograms,
            "formProgram": ProgramForm(),
            "plans": plans
        })
    else:
        return render(request, "base/index.html")


def add_program(request):
    if request.method == "POST":
        form = ProgramForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['user'])
            f = Program(
                user=form.cleaned_data['user'], programName=form.cleaned_data['programName'])
            f.save()
            print('New Program Added!')
        else:
            print(form.errors)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "base/index.html")


def add_exercise(request):
    if request.method == "POST":
        programId = request.POST['programId']
        exerciseId = request.POST['exerciseId']
        program = Program.objects.get(id=programId)
        exercise = ExercisesCatalog.objects.get(id=exerciseId)
        try:
            f = Plan(program=program, exercise=exercise)
            f.save()
            return HttpResponseRedirect(reverse("index"))
        except:
            return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "base/index.html")


def programs_view(request):
    currentUser = request.user.id
    programs = Program.objects.filter(user=currentUser)
    return render(request, "base/myPrograms.html", {
        "programs": programs,
    })


def program_page(request, pk):
    if request.user.is_authenticated:
        currentProgram = Program.objects.get(id=pk)
        form = ProgramForm(instance=currentProgram)
        programPlan = Plan.objects.filter(program=currentProgram)
        print(programPlan)
        exercises = ExercisesCatalog.objects.all()
        return render(request, "base/programPage.html", {
            "program": currentProgram,
            "plan": programPlan,
            "exercises": exercises,
            "form": form
        })
    else:
        return render(request, "base/index.html")


def edit_program(request):
    if request.method == "POST":
        programId = request.POST['id']
        program = Program.objects.get(id=programId)
        program.programName = request.POST['programName']
        program.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_program(request):
    if request.method == "POST":
        programId = request.POST['id']
        program = Program.objects.get(id=programId)
        program.delete()
    return HttpResponseRedirect(reverse("index"))


def delete_exercise(request):
    if request.method == "POST":
        programId = request.POST['programId']
        exerciseId = request.POST['exerciseId']
        program = Program.objects.get(id=programId)
        exercise = ExercisesCatalog.objects.get(id=exerciseId)
        plan = Plan.objects.get(program=program, exercise=exercise)
        plan.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
