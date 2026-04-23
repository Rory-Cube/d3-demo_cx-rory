# Cube configuration options: https://docs.cube.dev/reference/configuration/config

from cube import config

config.scheduled_refresh_time_zones = ["Europe/London"]

@config('semantic_layer_sync')
def semantic_layer_sync(ctx: dict) -> list[dict]:
    return [
        {
            "name": "ThoughtSpot Cube Sync",
            "type": "thoughtspot",
            "config": {
                "database": "d3-demo cx - rory",
                "org_id": "0",
                # "secret_key":"",
                "url": "https://cube-dev.thoughtspot.cloud/",
                "username": "rory",
                "password": "Vmwv*$@queozTKsn3",
            },
        }
    ]
