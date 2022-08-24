import click

from contxt.cli.clients import Clients
from contxt.cli.utils import print_table
from contxt.utils.serializer import Serializer


@click.group()
def find() -> None:
    """Search functions"""


@find.command("client")
@click.argument("CLIENT_ID")
@click.pass_obj
def client(clients: Clients, client_id: str) -> None:
    """Find a service instance by its Client ID"""
    print(
        f"Searching all accessible orgs ({','.join([x.get('slug') for x in clients.accessible_orgs])})"
    )
    for org in clients.accessible_orgs:
        try:
            instances = clients.contxt_deployments.get_service_instances(org.get("id"))
            edges = clients.contxt_deployments.get_edge_nodes(org.get("id"))
            instances.extend(edges)
            for inst in instances:
                client = inst.client_id
                if client:
                    if client.find(client_id) > -1:
                        print(f'Found match in org {org.get("slug")}')
                        print(Serializer.to_pretty_cli(inst))
        except Exception:
            pass


@find.command("by-name")
@click.argument("NAME_MATCH")
@click.pass_obj
def by_name(clients: Clients, name_match: str) -> None:
    """Find a service instance by its name"""
    print(
        f"Searching all accessible orgs ({','.join([x.get('slug') for x in clients.accessible_orgs])})"
    )
    hits = []
    for org in clients.accessible_orgs:
        try:
            instances = clients.contxt_deployments.get_service_instances(org.get("id"))
            edges = clients.contxt_deployments.get_edge_nodes(org.get("id"))
            instances.extend(edges)
            for inst in instances:
                name = inst.name
                if name:
                    name = name.lower()
                    if name.find(name_match.lower()) > -1:
                        match = inst.__dict__
                        match["type"] = str(type(inst))
                        match["org"] = org.get("slug")
                        hits.append(match)
        except Exception:
            pass

    print_table(hits, keys=["org", "type", "id", "name", "description", "client_id"])
