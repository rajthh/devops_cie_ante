import docker

client = docker.from_env()

IMAGE = "flask-apparmor"
CONTAINER_NAME = "flask-apparmor-security-test"
PROFILE = "my-apparmor-profile"

container = None

try:
    info = client.info()
    security_options = info.get("SecurityOptions", [])
    apparmor_available = any(
        "apparmor" in option.lower() for option in security_options
    )

    if not apparmor_available:
        print("ERROR: Docker does not report AppArmor support.")
        print("Restricted-action tests requiring AppArmor were not run.")
        print("Run this script on a supported Linux host with AppArmor enabled.")
        raise SystemExit(2)

    try:
        old_container = client.containers.get(CONTAINER_NAME)
        old_container.remove(force=True)
    except docker.errors.NotFound:
        pass

    container = client.containers.run(
        IMAGE,
        name=CONTAINER_NAME,
        security_opt=[f"apparmor={PROFILE}"],
        detach=True
    )

    container.reload()
    details = client.api.inspect_container(container.id)
    active_profile = details.get("AppArmorProfile", "")

    print(f"Container started: {container.short_id}")
    print(f"Reported active AppArmor profile: {active_profile or 'None'}")

    if active_profile != PROFILE:
        print("ERROR: The requested profile is not confirmed active.")
        raise SystemExit(2)

    tests = [
        ("Read /etc/passwd", ["cat", "/etc/passwd"]),
        ("Execute /bin/bash", ["/bin/bash", "-c", "echo execution-allowed"])
    ]

    for description, command in tests:
        result = container.exec_run(command)
        print(f"\n{description}")
        print(f"Exit code: {result.exit_code}")
        print(f"Output: {result.output.decode(errors='replace').strip()}")

        if result.exit_code != 0:
            print("Action failed; verify AppArmor audit logs to determine why.")
        else:
            print("Action succeeded; this action was not blocked.")

finally:
    if container is not None:
        try:
            container.stop(timeout=5)
            container.remove()
            print("\nContainer stopped and removed.")
        except docker.errors.APIError as error:
            print(f"Cleanup note: {error}")
