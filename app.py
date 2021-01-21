import os

from sanic import Sanic, response


app = Sanic(name='Switch-Scrape')


@app.get("/")
async def index(request):
    return response.text('I\'m a teapot', status=418)


if __name__ == "__main__":
    app.run(
        # You can change these using environment variables
        host=os.getenv('HOST', '0.0.0.0'),
        port=os.getenv('PORT', 8881),
    )
