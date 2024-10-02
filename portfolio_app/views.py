from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html', {
        'title': 'About Us',
        'description': 'This portfolio website showcases various projects and skills. It allows users to create, read, update, and delete project entries, providing a comprehensive overview of the developers capabilities.',
        'crud_operations': {
            'Create': 'Users can add new projects to the portfolio.',
            'Read': 'Users can view all projects listed on the website.',
            'Update': 'Users can edit existing project details.',
            'Delete': 'Users can remove projects from the portfolio.'
        }
    })


def contact(request):
    return render(request, "contact.html")


def userportfolio(request):
    return render(request, "userportfolio.html")


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = auth.authenticate(username=username, password=password)

        # Debugging output
        print(f'Username: {username}, Password: {password}, Authenticated User: {user}')

        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        contact = request.POST.get('contact')
        skills = request.POST.get('skills')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,
                                                email=email, password=password)
                user.contact = contact
                user.skills = skills
                user.save()

            return redirect('login')
        else:
            messages.info(request, 'password not matching')
            return redirect(request, 'register')

    return render(request, 'register.html')


def profile(request):
    return render(request, 'profile.html')


from .forms import ProjectForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, UserProfile, Experience, Education, Certification


def listprojects(request):
    userports = UserProfile.objects.all()
    return render(request, "listprojects.html", {"userports": userports})


def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')  # After creation, redirect to the project list
    else:
        form = ProjectForm()

    return render(request, 'create_project.html', {'form': form})


# List all projects
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})


# View a single project
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})


# Update an existing project
def update_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)

    return render(request, 'update_project.html', {'form': form, 'project': project})


# Delete a project
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == "POST":
        project.delete()
        return redirect('project_list')  # Redirect to the list of projects after deletion

    return render(request, 'delete_project.html', {'project': project})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import WorkExperienceForm


@login_required
def work_experience_view(request):
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the work experience page after saving
    else:
        form = WorkExperienceForm()
    return render(request, 'profile.html', {'form': form})


from .forms import EducationForm


@login_required
def education_view(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the education page after saving
    else:
        form = EducationForm()
    return render(request, 'profile.html', {'form': form})


from .forms import CertificationForm


@login_required
def certification_view(request):
    if request.method == 'POST':
        form = CertificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the certification page after saving
    else:
        form = CertificationForm()
    return render(request, 'profile.html', {'form': form})


from .forms import UserProfileForm


@login_required
def user_profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user.profile)  # Assuming User has a related Profile model
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = UserProfileForm(instance=user.profile)
    return render(request, 'profile.html', {'form': form})


from .models import UserProfile


@login_required
def update_profile(request):
    # Get the UserProfile instance for the logged-in user
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Assuming 'profile' is a detail view
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'update_profile.html', {'form': form})

def update_workexperience(request):
    work_experience, created = Experience.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = WorkExperienceForm(request.POST, request.FILES, instance=work_experience)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Assuming 'profile' is a detail view
    else:
        form = WorkExperienceForm(instance=work_experience)

    return render(request, 'update_workexperience.html', {'form': form})

def update_education(request):
    education, created = Education.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = EducationForm(request.POST, request.FILES, instance=education)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Assuming 'profile' is a detail view
    else:
        form = EducationForm(instance=education)

    return render(request, 'update_education.html', {'form': form})

def update_certificate(request):
    certificate, created = Certification.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = CertificationForm(request.POST, request.FILES, instance=certificate)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Assuming 'profile' is a detail view
    else:
        form = CertificationForm(instance=certificate)

    return render(request, 'update_certificate.html', {'form': form})



