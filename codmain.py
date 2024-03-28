if __name__ == "__main__":
    try:
        arg_parser = set_arguments()
        config_file_path = os.path.join(project_root_directory, "pyproject.toml")
        try:
            version = None
            with open(config_file_path, "r") as f:
                data = toml.load(f)#good
                version = data["tool"]["poetry"]["version"]
        except Exception as e:
            raise Exception("unable to find version from pyproject.toml.\n", e)

        run(arg_parser, version)
    except KeyboardInterrupt:
        print("Interrupt received! Exiting cleanly...")

    if not header_tag:
        raise Exception("unable to find header")
    if not isinstance(header_tag, Tag):
        raise Exception("invalid header found")
    header = header_tag.get_text().strip()

    # parse the main content containing the IP address
    body_tag = content.find("p")
    if not body_tag:
        raise Exception("unable to find body")
    if not isinstance(body_tag, Tag):
        raise Exception("invalid body found")
    body = body_tag.get_text().strip()

    return {"header": header, "body": body}
#yes
