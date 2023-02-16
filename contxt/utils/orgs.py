org_id_slugs = {
    "18d8b68e-3e59-418e-9f23-47b7cd6bdd6b": "genan",
    "02efa741-a96f-4124-a463-ae13a704b8fc": "lineage",
    "2fe29680-fc3d-4888-9e9b-44be1e59c22c": "sfnt",
    "5209751f-ea46-4b3e-a5dd-b8d03311b791": "ndustrial",
}


def get_slug_or_org_id(org_id: str):
    return org_id_slugs.get(org_id) or org_id
