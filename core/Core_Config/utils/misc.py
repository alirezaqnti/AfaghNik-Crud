import yaml


def yaml_coerce(value):
    # Convert value to propper Python

    if isinstance(value, str):
        # yaml.loads returns a python object (we are just creating some quick yaml data with dummy)
        # Converts string dict "{'apple':1,'bacon:2}"
        # Useful because somtimes we need to stringfy settings this way(like in Docker/files)
        return yaml.load(f"dummy: {value}", Loader=yaml.SafeLoader)["dummy"]
    return value
