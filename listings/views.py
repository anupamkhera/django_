from django.shortcuts import render

# Create your views here.
listings = Listing.objects.all()

context = {
    'listings' : listings
}
def index(request):
    return render(request, 'listings/listings.html',context)

def listing(request):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')
