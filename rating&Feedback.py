# users/models.py
class Rating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()

class Feedback(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()

# users/views.py
def submit_feedback(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        Feedback.objects.create(user=request.user, content=feedback)
    return redirect('dashboard')
