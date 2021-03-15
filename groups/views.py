from django.shortcuts import render



def group_list(request):

    return render(request, 'groups/group_list.html')
