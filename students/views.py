from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CourseEnrollForm
from django.views.generic.list import ListView
from courses.models import Course
from django.views.generic.detail import DetailView


class StudentRegistrationView(CreateView):
    template_name = 'students/student/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('student_course_list')

    def form_valid(self, form):
        result = super().form_valid(form)

        cd = form.cleaned_data
        user = authenticate(username=cd['username'],
                            password=cd['password1'])
        login(self.request, user)
        return result


class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm

    def form_valid(self, form):
        self.course = form.cleaned_data['course']

        self.course.students.add(self.request.user)
        return super().form_valid(form)

    # Method returns the URL that the user will be redirected
    # to if the form was successfully submitted.
    def get_success_url(self):
        return reverse_lazy('student_course_detail',
                            args=[self.course.id])


# displaying the courses that students are enrolled on.
class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/course/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])


class StudentCourseDetailView(DetailView):
    model = Course
    template_name = 'students/course/detail.html'

    # Limit the base QuerySet to courses on which the student is enrolled.
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(students__in=[self.request.user])

    # Set a course module in the context if the module_id URL parameter is given.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get course object.
        course = self.get_object()
        if 'module_id' in self.kwargs:
            # Get current module.
            context['module'] = course.modules.get(
                id=self.kwargs['module_id'])
        else:
            # Get first module.
            context['module'] = course.modules.all()[0]
        return context
