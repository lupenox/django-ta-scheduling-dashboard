from django.shortcuts import render
from django.views import View

# Create your views here.

class Home(View):
    def get(self, request):
        # Redirects to the login page
        return redirect('/login/')

class dashboardView(View):
    def get(self, request):

    def post(self, request):

class loginView(View):
    def get(self, request):

    def post(self, request):

class dashboardView(View):
    def get(self, request):

    def post(self, request):

class userManageView(View):
    def get(self, request):

    def post(self, request):

class courseManageView(View):
    def get(self, request):

    def post(self, request):

class contactInfoView(View):
    def get(self, request):

    def post(self, request):

class courseAssignmentView(View):
    def get(self, request):

    def post(self, request):