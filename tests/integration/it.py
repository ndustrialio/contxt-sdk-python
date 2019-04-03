from contxt.auth.cli import CLIAuth
from contxt.services.assets import AssetsService
from contxt.services.contxt import ContxtService
from contxt.services.events import EventsService
from contxt.services.facilities import FacilitiesService

if __name__ == "__main__":
    auth = CLIAuth()
    c = ContxtService(auth)
    ll = c.get_organization_with_name("Lineage Logistics")
    wpe = c.get_organization_with_name("Western Plains Energy")
    # organization_id = "02efa741-a96f-4124-a463-ae13a704b8fc"  # lineage
    # organization_id = "a8e526e4-cb2d-4188-ac25-294e76f9f467"  # western plains
    batch_id = "429819e7-44cc-40aa-a8d8-721dc9a425d7"

    s = AssetsService(auth, wpe.id, types_to_fully_load="EthanolProcessBatch")
    complete_asset = s.get_complete_asset(batch_id)
    triggered_event_id = complete_asset.attributes['batch_triggered_event_id']

    event_service = EventsService(auth)
    # event_type = event_service.get_event_types()
    triggered_event = event_service.get_triggered_event(triggered_event_id)
    event_definition = event_service.get_event_definition(triggered_event.event_id)
    print("done")
