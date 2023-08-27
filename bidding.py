# listings/models.py
class Bid(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    bidder = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

# listings/views.py
from .forms import BidForm

def place_bid(request, product_id):
    product = Product.objects.get(id=product_id)
    
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.product = product
            bid.bidder = request.user
            bid.save()
            return redirect('dashboard')

    else:
        form = BidForm()

    return render(request, 'listings/place_bid.html', {'form': form, 'product': product})
