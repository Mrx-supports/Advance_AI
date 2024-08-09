from aiohttp import web

# Define the route table
routes = web.RouteTableDef()

# Define the root route handler
@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response({"message": "Tony Stark"})

# Create the web application and add routes
app = web.Application()
app.add_routes(routes)

# Run the application on the specified port
if __name__ == "__main__":
    web.run_app(app, port=8080)  # Adjust the port if necessary