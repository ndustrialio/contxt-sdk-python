

def find_organization_by_name(contxt_service, organization_name):

    organization = None
    for org in contxt_service.get_organizations():
        if org.name == organization_name:
            organization = org

    return organization
