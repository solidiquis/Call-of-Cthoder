from .models import ContactInformation

def ContactInformationContext(request):
    """
    Allows every template to have access to contact information.
    """

    if ContactInformation.objects.all().first() is not None:
        contact_info = ContactInformation.objects.first()
    else:
        contact_info = ContactInformation.objects.create(
                email='test@gmail.com',
                github='https://github.com/',
                linkedin='https://www.linkedin.com/',
                )

    return {'contact_info': contact_info}
