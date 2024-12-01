from  django.core. mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


from .forms import CustomUserCreationForm

class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)

        return super().form_valid(form)
    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо за ваше доверие !'
        from_email = 'djangoskypro@yandex.ru'
        recipient_list = [user_email,]
        send_mail(subject,message,from_email,recipient_list)




