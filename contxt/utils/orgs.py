org_id_slugs = {
    "18d8b68e-3e59-418e-9f23-47b7cd6bdd6b": "genan",
    "02efa741-a96f-4124-a463-ae13a704b8fc": "lineage",
    "2fe29680-fc3d-4888-9e9b-44be1e59c22c": "sfnt",
    "5209751f-ea46-4b3e-a5dd-b8d03311b791": "ndustrial",
    "65be9a9d-5cc1-4318-8762-da74e454ea51": "vcv",
    "bc071c66-d030-44c7-9c2a-cfe3161cdf3e": "lsc-communications",
    "5a4bbead-7208-499e-a853-9cb174a71c63": "uscold",
    "513b06ea-0169-4436-b3b2-77318bd77e94": "wlgore",
}


def get_slug_or_org_id(org_id: str):
    return org_id_slugs.get(org_id) or org_id
