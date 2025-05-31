from chalice import Chalice, Rate

app = Chalice(app_name='scheduler')


@app.schedule(Rate(5, unit=Rate.MINUTES))
def scheduled_task(event):
    print("Scheduled task executed.")