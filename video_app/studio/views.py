
from django.contrib.auth import authenticate, login

# We will use django's default UserCreationForm
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect
from django.views import View


from django.shortcuts import render
from django.http import JsonResponse


# from .forms import UploadForm
from .forms import UploadVideo
# from .models import Document
from .models import Video
# Create your views here.
from datetime import datetime




def index(request):
    response = redirect('/login/')
    return response


def upload(request):
    print(Video.objects.all())
    print(request.POST)
    user = request.user
    if not request.user.is_authenticated:
        return JsonResponse({"auth": False})
    print(request.FILES)
    if request.FILES:
        form = UploadVideo(request.POST, request.FILES)

        if form.is_valid():
            video = Video(
                # get title from form.data
                title=form.data["title"],
                # get image from form.files
                videoFile=form.files["videoFile"],
                subtitleFile=form.files["subtitleFile"],
                uploaded_date=datetime.now(),
                uploaded_by=user,
            )
            video.save()

    return JsonResponse({'success': True})


def studio(request):
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        return JsonResponse({"auth": False})
    videos = Video.objects.order_by("uploaded_date")
    # print(videos[0].videoFile)
    return render(request, 'studio/studio.html', {'videos': videos, 'user': request.user})


def dashboard(request):
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        return JsonResponse({"auth": False})
    videos = Video.objects.order_by("uploaded_date")

    videos = Video.objects.all().filter(uploaded_by=request.user)

    print(videos)

    # print(videos[0].videoFile)
    return render(request, 'studio/dashboard.html', {'videos': videos, 'user': request.user})


class SignUpView(View):
    def get(self, request):
        # Render giffy_app/signup.html with
        # UserCreationForm upon page load
        return render(
            request,
            "studio/signup.html",
            {
                "form": UserCreationForm(),
            },
        )

    def post(self, request):
        # Validate form, create user, and login
        # upon sign-up form submission
        form = UserCreationForm(request.POST)

        # If user credentials are valid
        if form.is_valid():
            # create a new user in the database
            form.save()

            # get username and password from form
            username = form.data["username"]
            password = form.data["password1"]

            # authenticate user using credentials
            # submited in the UserCreationForm
            user = authenticate(
                request,
                username=username,
                password=password,
            )

            if user:
                # login user
                login(request, user)

            # redirect user to index page
            return redirect("/")

        # if form is not valid, re-render the template
        # showing the validation error messages
        return render(
            request,
            "studio/signup.html",
            {
                "form": form,
            },
        )
