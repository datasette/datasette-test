from datasette import hookimpl


@hookimpl
def permission_allowed(datasette, actor, action):
    from datasette.utils import actor_matches_allow

    if not hasattr(datasette, "_special_test_permissions"):
        return None
    special_permissions = datasette._special_test_permissions
    if action not in special_permissions:
        return None
    rule = special_permissions[action]
    return actor_matches_allow(actor, rule)
