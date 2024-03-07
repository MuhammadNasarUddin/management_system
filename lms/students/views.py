from django.shortcuts import render, redirect
from django.contrib import messages,auth
from .models import CustomUser, Interviews, Faceless, Graphic, Posting
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'index.html')

def signup(request):
    message = None  # Initialize a variable to store the message

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        gender = request.POST['gender']
        occupation = request.POST['occupation']
        school = request.POST['school']
        fb_link = request.POST['fb_link']

        # Check if passwords match
        if pass1 != pass2:
            message = 'Passwords do not match'
            return render(request, 'signup.html', {'message': message})

        try:
            # Create a new CustomUser instance
            new_user = CustomUser.objects.create_user(
                username=username,
                password=pass1,
                first_name=fname,
                last_name=lname,
                email=email,
                gender=gender,
                occupation=occupation,
                school=school,
                fb_link=fb_link,
            )

            # Save the user
            new_user.save()

            message = 'Account created successfully. You can now login.'
            return redirect('signin')  # Replace 'login' with the URL or view name for the login page
        except Exception as e:
            message = f'Error creating account: {e}'

    return render(request, 'signup.html', {'message': message})




from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login



def signin(request):
    msg = None  # Initialize msg variable
    msg_type = None  # Initialize msg_type variable

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            msg = 'Login successful.'
            msg_type = 'success'
            return redirect('index')  # Replace 'dashboard' with the URL or view name for the dashboard page
        else:
            msg = 'Invalid username or password.'
            msg_type = 'danger'

    return render(request, 'signin.html', {'msg': msg, 'msg_type': msg_type})









def logout(request):
    messages.success(request, '')  # Clear any messages in the session
    auth.logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('signin')  # Replace 'signin' with the URL or view name for the login page




@login_required
def interview(request):
    if request.method == "POST":
        user = request.user
        guest_name = request.POST['guest_name']
        interview_no = request.POST['interview_no']
        topic = request.POST['topic']
        language = request.POST['language']
        city = request.POST['city']
        country = request.POST['country']
        url = request.POST['url']

        try:
            new_interview = Interviews(
                user=user,
                guest_name=guest_name,
                interview_no=interview_no,
                topic=topic,
                language=language,
                city=city,
                country=country,
                url=url
            )

            new_interview.save()
            messages.success(request, 'Interview added successfully.')
            return redirect('Profile')  # Replace 'interviews' with the URL or view name for the interviews page
        except Exception as e:
            messages.error(request, f'Error adding interview: {e}')
    return render(request, 'index.html')


@login_required
def user_interviews(request):
    user = request.user
    interviews = Interviews.objects.filter(user=user)
    return render(request, 'user_interviews.html', {'interviews': interviews})



@login_required
def faceless(request):
    if request.method == "POST":
        user = request.user
        title = request.POST['title']
        faceless_no = request.POST['faceless_no']
        url = request.POST['url']

        try:
            new_faceless = Faceless(
                user=user,
                title=title,
                faceless_no=faceless_no,
                url=url
            )

            new_faceless.save()
            messages.success(request, 'Faceless added successfully.')
            return redirect('Profile')  # Replace 'faceless' with the URL or view name for the faceless page
        except Exception as e:
            messages.error(request, f'Error adding faceless: {e}')
    return render(request, 'index.html')


@login_required
def user_faceless(request):
    user = request.user
    faceless = Faceless.objects.filter(user=user)
    return render(request, 'user_faceless.html', {'faceless': faceless})



@login_required
def posting(request):
    if request.method == "POST":
        user = request.user
        title = request.POST['title']
        posting_no = request.POST['posting_no']
        url = request.POST['url']

        try:
            new_posting = Posting(
                user=user,
                title=title,
                posting_no=posting_no,
                url=url
            )

            new_posting.save()
            messages.success(request, 'Posting added successfully.')
            return redirect('Profile')  # Replace 'posting' with the URL or view name for the posting page
        except Exception as e:
            messages.error(request, f'Error adding posting: {e}')

    return render(request, 'index.html')

@login_required
def user_posting(request):
    user = request.user
    posting = Posting.objects.filter(user=user)
    return render(request, 'user_posting.html', {'posting': posting})           



@login_required
def graphic(request):
    if request.method == "POST":
        user = request.user
        title = request.POST['title']
        graphic_no = request.POST['graphic_no']
        url = request.POST['url']

        try:
            new_graphic = Graphic(
                user=user,
                title=title,
                graphic_no=graphic_no,
                url=url
            )

            new_graphic.save()
            messages.success(request, 'Graphic added successfully.')
            return redirect('Profile')  # Replace 'graphic' with the URL or view name for the graphic page
        except Exception as e:
            messages.error(request, f'Error adding graphic: {e}')
    return render(request, 'index.html')         

@login_required
def user_graphic(request):
    user = request.user
    graphic = Graphic.objects.filter(user=user)
    return render(request, 'user_graphic.html', {'graphic': graphic})            



@login_required
def profile(request):
    user = request.user
    total_interview = Interviews.objects.filter(user=user).count()
    total_faceless = Faceless.objects.filter(user=user).count()
    total_posting = Posting.objects.filter(user=user).count()
    total_graphic = Graphic.objects.filter(user=user).count()
    ct = {
        'user': user,
        'total_interview': total_interview,
        'total_faceless': total_faceless,
        'total_posting': total_posting,
        'total_graphic': total_graphic
    }
    return render(request, 'Profile.html', ct)