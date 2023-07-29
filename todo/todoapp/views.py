from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.

def index(request, id):
	ls = ToDoList.objects.get(id=id)

	if request.method == "POST":
		if request.POST.get("save"):
			for item in ls.item_set.all():
				p = request.POST
				
				if "clicked" == p.get("c"+str(item.id)):
					item.complete = True
				else:
					item.complete = False

				if "text" + str(item.id) in p:
					item.text = p.get("text" + str(item.id))


				item.save()

		elif request.POST.get("add"):
			newItem = request.POST.get("new")
			if newItem != "":
				ls.item_set.create(text=newItem, complete=False)
			else:
				print("invalid")
		elif request.POST.get("delete"):
			for item in ls.item_set.all():
				 
				if item.complete == True:
					obj = get_object_or_404(Item, id=item.pk)
					obj.delete()


	return render(request, "index.html", {"ls": ls})
                 

def home(response):
	return render(response, "home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)

            return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()

    return render(response, "create.html", {"form":form})

def view(response):
    return render(response, "view.html", {})