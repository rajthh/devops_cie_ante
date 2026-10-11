import docker
import sys

client = docker.from_env()

IMAGE = "flask-apparmor"
CONTAINER_NAME = "flask-apparmor-sdk-test"
PROFILE = "my-apparmor-profile"

try:
    print("Building Docker image...")
    client.images.build(path=".", tag=IMAGE)

    # Check whether AppArmor is available through the Docker host.
    info = client.info()
    security_options = info.get("SecurityOptions", [])
    apparmor_available = any("apparmor" in option.lower()
                             for option in security_options)

    if not apparmor_available:
        print("\nWARNING: Docker does not report AppArmor support.")
        print("The container will NOT be started with a claimed")
        print("AppArmor enforcement. Use a supported Linux host.")
        sys.exit(2)

    # Remove an old container with the same name, if present.
    try:
        old_container = client.containers.get(CONTAINER_NAME)
        old_container.remove(force=True)
    except docker.errors.NotFound:
        pass

    print("Starting container with AppArmor profile...")
    container = client.containers.run(
        IMAGE,
        name=CONTAINER_NAME,
        ports={"5000/tcp": 5000},
        security_opt=[f"apparmor={PROFILE}"],
        detach=True
    )

    container.reload()
    print(f"Container started: {container.short_id}")

    details = client.api.inspect_container(container.id)
    security_opt = details.get("HostConfig", {}).get("SecurityOpt")
    active_profile = details.get("AppArmorProfile", "")

    print(f"Requested security options: {security_opt}")
    print(f"Reported active AppArmor profile: {active_profile or 'None'}")

    if active_profile == PROFILE:
        print("AppArmor profile is reported as active.")
    else:
        print("WARNING: The requested profile is not confirmed active.")

finally:
    # Clean up only the container created by this script.
    try:
        container.stop(timeout=5)
        container.remove()
        print("Container stopped and removed.")
    except (NameError, docker.errors.NotFound):
        pass
    except docker.errors.APIError as error:
        print(f"Container cleanup note: {error}")