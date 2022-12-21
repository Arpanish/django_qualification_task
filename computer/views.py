from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.views.generic.edit import FormView
from .models import Computer
from .forms import CreateModel
from django.views.generic.edit import UpdateView



# class based view for lists of computers
class ComputerList(View):
    def get(self, request):
        computer_listing = Computer.objects.all()
        return render(request,'computer/homepage.html',{'Computerlist':computer_listing})


# class based view for creation of computer information 
class ComputerCreate(FormView):
    template_name = 'computer/add_computer.html'
    # template_name = 'computer/homepage.html'
    form_class = CreateModel
    success_url = '/thanks/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# class based view for thank you page
class Thanks(View):
    def get(self, request):
        # computer_listing = Computer.objects.all()
        return render(request,'computer/thankyoupage.html')


# class based view for detailing of computer information
class ComputerDetail(View):
    def get(self, request, id):
        Computerdetail = Computer.objects.get(id=id)
        return render(request, 'computer/computerdetail.html', {'detail':Computerdetail})


#class based delete operation 
class ComputerDelete(View):
    def get(self, request, id):
        Computerdelete = Computer.objects.get(id=id)
        Computerdelete.delete()
        return redirect('/') 


# class based view to update computer information
class ComputerInfoUpdate(View):
    def get(self, request,id):
        update = Computer.objects.get(id=id)
        computerupdate=CreateModel(instance=update)  
        return render(request,'computer/updatecomputer_info.html',{'updatecomputerinfo':computerupdate})

    def post(self,request,id):
        update = Computer.objects.get(pk=id)
        computerupdate = CreateModel(request.POST,instance=update)
        if computerupdate.is_valid():
            computerupdate.save()
            return redirect('/')



   