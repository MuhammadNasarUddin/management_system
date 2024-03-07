
# adminpanel/views.py
from django.shortcuts import render, redirect
import logging
from django.contrib.auth import login, logout , authenticate
from students.models import CustomUser , Interviews , Faceless , Posting , Graphic
logger = logging.getLogger(__name__)

from django.contrib.auth import authenticate, login

def admin_signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)

            # Redirect to a success page, or use reverse() to redirect to a specific URL
            return redirect('dashboard')
        else:
            # Invalid credentials
            error_message = "Invalid username or password. Please try again."
            return render(request, 'adminpanel/admin_signin.html', {'error_message': error_message})

    return render(request, 'adminpanel/admin_signin.html')


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_signin')
    total_interviews = Interviews.objects.all().count()
    total_faceless = Faceless.objects.all().count()
    total_postings = Posting.objects.all().count()
    total_graphics = Graphic.objects.all().count()
    total_users = CustomUser.objects.exclude(username='admin')[:3]
    interviews = Interviews.objects.all()[:3]
    faceless = Faceless.objects.all()[:3]
    postings = Posting.objects.all()[:3]
    graphics = Graphic.objects.all()[:3]
    total_userss = CustomUser.objects.exclude(username='admin').count()
    only_student = CustomUser.objects.filter(occupation='Student').count()
    only_staff = CustomUser.objects.filter(occupation='Staff').count()
    only_facilitator = CustomUser.objects.filter(occupation='Facilitator').count()


    ct = {
        'total_interviews': total_interviews,
        'total_faceless': total_faceless,
        'total_postings': total_postings,
        'total_graphics': total_graphics,
        'total_users': total_users,
        'interviews': interviews,
        'faceless': faceless,
        'postings': postings,
        'graphics': graphics,
        'only_student': only_student,
        'only_staff':only_staff,
        'only_facilitator': only_facilitator,
        'total_userss': total_userss,
    }

    return render(request, 'adminpanel/admin_home.html' , ct)




def admin_logout(request):
    if request.user.is_authenticated:
        # Log the user out
        logout(request)
        return redirect('admin_signin') 
    else:
        return redirect('admin_signin')
    



def admin_allusers(request):

    all_users = CustomUser.objects.exclude(username='admin')
    total_users = CustomUser.objects.exclude(username='admin').count()
    only_student = CustomUser.objects.filter(occupation='Student').count()
    only_staff = CustomUser.objects.filter(occupation='Staff').count()
    only_facilitator = CustomUser.objects.filter(occupation='Facilitator').count()

   
    ct = {
    'all_users': all_users,
    'total_users': total_users,
    'only_student': only_student,
    'only_staff': only_staff,
    'only_facilitator': only_facilitator,
}

    return render(request, 'adminpanel/admin_allusers.html', ct)




from django.shortcuts import get_object_or_404

def all_users_detail(request, id):
    user = get_object_or_404(CustomUser, id=id)
    user_interview = Interviews.objects.filter(user=user).count()
    user_faceless = Faceless.objects.filter(user=user).count()
    user_posting = Posting.objects.filter(user=user).count()
    user_graphic = Graphic.objects.filter(user=user).count()
    user_interview_all = Interviews.objects.filter(user=user)
    user_posting_all = Posting.objects.filter(user=user)
    user_faceless_all = Faceless.objects.filter(user=user)
    user_graphic_all = Graphic.objects.filter(user=user)

    ct = {
        'user': [user],  # Pass user as a list
        'user_interview': user_interview,
        'user_faceless': user_faceless,
        'user_posting': user_posting,
        'user_graphic': user_graphic,
        'user_interview_all': user_interview_all,
        'user_posting_all': user_posting_all,
        'user_faceless_all': user_faceless_all,
        'user_graphic_all': user_graphic_all,
    }
    return render(request, 'adminpanel/all_users_detail.html', ct)


def all_user_delete(request, id):
    user = get_object_or_404(CustomUser, id=id)
    user.delete()
    return redirect('users')

def all_user_edit(request, id):
    user = get_object_or_404(CustomUser, id=id)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.occupation = request.POST.get('occupation')
        user.school = request.POST.get('school')
        user.save()
        return redirect('users')
    return render(request, 'adminpanel/all_user_edit.html', {'user': user})



def all_interviews(request):
    all_interviews = Interviews.objects.all().order_by
    total_interviews = Interviews.objects.all().count()
    student_interviews = Interviews.objects.filter(user__occupation='Student').count()
    staff_interviews = Interviews.objects.filter(user__occupation='Staff').count()
    facilitator_interviews = Interviews.objects.filter(user__occupation='Facilitator').count()

    ct = {
        'all_interviews': all_interviews,
        'total_interviews': total_interviews,
        'student_interviews': student_interviews,
        'staff_interviews': staff_interviews,
        'facilitator_interviews': facilitator_interviews,
    }
    return render(request, 'adminpanel/all_interviews.html' , ct)



def delete_interview(request, id):
    interview = get_object_or_404(Interviews, id=id)
    interview.delete()
    return redirect('interviews')

# def all_interviews_detail(request, id):
#     interview = get_object_or_404(Interviews, id=id)
#     total_user_interview = Interviews.objects.filter(id=id).count()
#     total_eng_interview = Interviews.objects.filter(id=id, language='English').count()
#     total_urd_interview = Interviews.objects.filter(id=id, language='Urdu').count()

#     ct = {
#         'interview': [interview],
#         'total_user_interview': total_user_interview,
#         'total_eng_interview': total_eng_interview,
#         'total_urd_interview': total_urd_interview,
#     }
#     return render(request, 'adminpanel/all_interviews_detail.html', ct)



def all_faceless(request):
    all_faceless = Faceless.objects.all()
    total_faceless = Faceless.objects.all().count()
    student_faceless = Faceless.objects.filter(user__occupation='Student').count()
    staff_faceless = Faceless.objects.filter(user__occupation='Staff').count()
    facilitator_faceless = Faceless.objects.filter(user__occupation='Facilitator').count()

    ct = {
        'all_faceless': all_faceless,
        'total_faceless': total_faceless,
        'student_faceless': student_faceless,
        'staff_faceless': staff_faceless,
        'facilitator_faceless': facilitator_faceless,
    }
    return render(request, 'adminpanel/all_faceless.html' , ct)

def delete_faceless(request, id):
    faceless = get_object_or_404(Faceless, id=id)
    faceless.delete()
    return redirect('faceless')

def all_posting(request):
    all_posting = Posting.objects.all()
    total_posting = Posting.objects.all().count()
    student_posting = Posting.objects.filter(user__occupation='Student').count()
    staff_posting = Posting.objects.filter(user__occupation='Staff').count()
    facilitator_posting = Posting.objects.filter(user__occupation='Facilitator').count()

    ct={
        'all_posting': all_posting,
        'total_posting': total_posting,
        'student_posting': student_posting,
        'staff_posting': staff_posting,
        'facilitator_posting': facilitator_posting,
    
    }
    return render(request, 'adminpanel/all_posting.html',ct)

def delete_posting(request, id):
    posting = get_object_or_404(Posting, id=id)
    posting.delete()
    return redirect('posting')

def all_graphics(request):
    all_graphics = Graphic.objects.all()
    total_graphics = Graphic.objects.all().count()
    student_graphics = Graphic.objects.filter(user__occupation='Student').count()
    staff_graphics = Graphic.objects.filter(user__occupation='Staff').count()
    facilitator_graphics = Graphic.objects.filter(user__occupation='Facilitator').count()

    ct = {
        'all_graphics': all_graphics,
        'total_graphics': total_graphics,
        'student_graphics': student_graphics,
        'staff_graphics': staff_graphics,
        'facilitator_graphics': facilitator_graphics,
    }
    return render(request, 'adminpanel/all_graphics.html' , ct)




def delete_graphics(request, id):
    graphic = get_object_or_404(Graphic, id=id)
    graphic.delete()
    return redirect('graphics')