def create_comite(sender, instance, created, **kwargs):
    if created:
        # Send notification
        print("Comite created.")
