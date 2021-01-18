from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Customer
from django.contrib.auth.models import Group

#signals
#@receiver(post_save, sender=User)
def customer_profile(sender, instance, created, **kwargs): 
    if created:
        group = Group.objects.get(name='customers')
        instance.groups.add(group)
        Customer.objects.create(
                        user=instance,
                        name=instance.username,
                    )
        print('Profile created!')
post_save.connect(customer_profile, sender=User)

#@receiver(post_save, sender=User)
#def update_profile(sender, instance, created, **kwargs):
#    if created == False:
#        instance.customer.save()
#        print('Profile udpated')
#post_save.connect(update_profile, sender=User)