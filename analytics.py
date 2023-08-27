# listings/views.py
def product_analytics(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Calculate analytics, e.g., average bids, total bids, highest bid, etc.
    return render(request, 'product_analytics.html', {'product': product, 'analytics': analytics})
