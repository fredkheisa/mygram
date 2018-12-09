from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Picture


# Create your views here.

def profiles_today(request):
    date = dt.date.today()
    profiles = Pictures.todays_profiles()
    return render(request, 'all_profiles/today-profiles.html', {"date": date,})

def past_days_profiles(request, past_date):

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(profiles_of_day)

    return render(request, 'all_profiles/past-profiles.html', {"date": date})

def search_results(request):

    if 'picture' in request.GET and request.GET["picture"]:
        search_term = request.GET.get("picture")
        searched_picture = Picture.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all_profiles/search.html',{"message":message,"picture": searched_pictures})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_profiles/search.html',{"message":message})