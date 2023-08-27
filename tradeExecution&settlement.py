# listings/views.py
from django.db import transaction

@transaction.atomic
def confirm_trade(request, bid_id):
    bid = Bid.objects.get(id=bid_id)
    
    if bid.product.seller == request.user:
        bid.product.current_price = bid.amount
        bid.product.save()
        
        # Process payment logic here (e.g., deduct funds from buyer, add funds to seller)
        
        bid.delete()  # Remove bid after trade confirmation
        return redirect('dashboard')
    
    else:
        return HttpResponse("Unauthorized", status=401)
